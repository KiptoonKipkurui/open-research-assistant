"""
MAIN module provides an entry point into the application
"""
import os
import timeit
from hashlib import md5

import box
import redis
import uvicorn
import wget
import yaml
from dotenv import find_dotenv, load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from database import build_db
from inference import LLmResponse, LLMSource, setup_dbqa

# Import config vars
with open("config/config.yml", "r", encoding="utf8") as ymlfile:
    cfg = box.Box(yaml.safe_load(ymlfile))

# Load environment variables from .env file
load_dotenv(find_dotenv())

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = redis.StrictRedis(host="localhost", port=6379, db=0)
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Default function that the app starts at
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/process_pdf")
async def process_pdf(request: Request):
    """
    Process PDF
    """
    print("Processing pdf")
    body = await request.body()
    key = md5(body).hexdigest()
    print(key)

    file_name = f"./data/{key}.pdf"
    if not os.path.exists(file_name):
        with open(file_name, "wb") as file:
            file.write(body)
        build_db(cfg)

    if db.get(key) is not None:
        print("Already processed pdf")
        return JSONResponse({"key": key})

    print("Done processing pdf")
    return JSONResponse({"key": key})


@app.post("/download_pdf")
async def download_pdf(request: Request):
    """
    Download Online PDF
    """
    data = await request.json()
    url = data.get("url")
    key = md5(str(url).encode("utf-8")).hexdigest()

    if db.get(key) is not None:
        return JSONResponse({"key": key})
    file_name = f"./data/{key}.pdf"
    if not os.path.exists(file_name):
        wget.download(url, file_name)
        build_db(cfg)

    print("Done processing pdf")
    return JSONResponse({"key": key})


@app.post("/reply")
async def reply(request: Request):
    """
    Query the open research assistant on a document
    """
    data = await request.json()
    query = data.get("query")
    dbqa = setup_dbqa(cfg)

    query = str(query)

    start = timeit.default_timer()
    response = dbqa({"query": query})
    end = timeit.default_timer()
    result = LLmResponse()
    result.result = response["result"]

    print(f'\nAnswer: {response["result"]}')
    print("=" * 50)

    # Process source documents
    source_docs = response["source_documents"]
    for i, doc in enumerate(source_docs):
        print(f"\nSource Document {i+1}\n")
        print(f"Source Text: {doc.page_content}")
        print(f'Document Name: {doc.metadata["source"]}')
        # print(f'Page Number: {doc.metadata["page"]}\n')
        result.sources.append(LLMSource(doc.page_content, doc.metadata["page"]))
        print("=" * 60)

    print(f"Time to retrieve response: {end - start}")

    return {"answer": result.result, "sources": result.sources}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
