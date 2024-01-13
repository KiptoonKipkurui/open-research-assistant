"""
Module providing helper functions to build LLMs
"""
import json

import box
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.vectorstores import FAISS
from langchain.llms import LlamaCpp


QA_TEMPLATE = """Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""


def build_llm(config: box.Box):
    """
    Builds an LLM given the configuration
    """
    llm = LlamaCpp(
        model_path=config.MODEL_BIN_PATH,
        temperature=0.75,
        max_tokens=2000,
        top_p=1,
        verbose=True)

    return llm


def set_qa_prompt():
    """
    Prompt template for QA retrieval for each vectorstore
    """
    prompt = PromptTemplate(
        template=QA_TEMPLATE, input_variables=["context", "question"]
    )
    return prompt


def build_retrieval_qa(config: box.Box, llm, prompt, vectordb):

    """
    Sets up the build and retrival QA chain
    """
    dbqa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectordb.as_retriever(search_kwargs={"k": config.VECTOR_COUNT}),
        return_source_documents=config.RETURN_SOURCE_DOCUMENTS,
        chain_type_kwargs={"prompt": prompt},
    )
    return dbqa


def setup_dbqa(config: box.Box,llm=None):
    """
    Sets the the whole inference pipeline
    """
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
    )
    vectordb = FAISS.load_local(config.DB_FAISS_PATH, embeddings)

    if not llm:
        llm = build_llm(config=config)
    qa_prompt = set_qa_prompt()
    dbqa = build_retrieval_qa(config, llm, qa_prompt, vectordb)

    return dbqa


class LLMSource:
    """
    Defines the source that an LLM uses to answer a query
    """
    text: str
    page: int

    def __init__(self, text, page) -> None:
        """
        init function, takes in the text and the page
        """
        self.text = text
        self.page = page


class LLmResponse:
    """
    Represents a response from the LLM
    """

    result: str
    sources = []

    def __init__(self) -> None:

        """
        Init function,
        ::Param source: A source that the LLM used for referencing
        ::Param result: The response from the LLM
        """
        self.sources = []
        self.result = None

    def to_json(self):
        """
        Converts the response to JSON format
        """
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class LLmResponseEncoder(json.JSONEncoder):
    """
    LLM Response Encoder, encodes LLMResponse to valid json
    """
    def default(self, o):
        """
        Encodes the received object in JSON
        """
        return o.__dict__


if __name__ == "__main__":
    cfg = box.box_from_file("./config/config.yml", "yaml")
    build_llm(cfg)
