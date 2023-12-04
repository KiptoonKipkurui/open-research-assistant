from langchain.llms import CTransformers
from dotenv import find_dotenv, load_dotenv
from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import box
import json


qa_template = """Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""


def build_llm(cfg:box.Box):
    # Local CTransformers model
    llm = CTransformers(model=cfg.MODEL_BIN_PATH,
                        model_type=cfg.MODEL_TYPE,
                        config={'max_new_tokens': cfg.MAX_NEW_TOKENS,
                                'temperature': cfg.TEMPERATURE}
                        )

    return llm
def set_qa_prompt():
    """
    Prompt template for QA retrieval for each vectorstore
    """
    prompt = PromptTemplate(template=qa_template,
                            input_variables=['context', 'question'])
    return prompt


def build_retrieval_qa(cfg:box.Box,llm, prompt, vectordb):
    dbqa = RetrievalQA.from_chain_type(llm=llm,
                                       chain_type='stuff',
                                       retriever=vectordb.as_retriever(search_kwargs={'k': cfg.VECTOR_COUNT}),
                                       return_source_documents=cfg.RETURN_SOURCE_DOCUMENTS,
                                       chain_type_kwargs={'prompt': prompt}
                                       )
    return dbqa


def setup_dbqa(cfg:box.Box):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                                       model_kwargs={'device': 'cpu'})
    vectordb = FAISS.load_local(cfg.DB_FAISS_PATH, embeddings)
    llm = build_llm(cfg=cfg)
    qa_prompt = set_qa_prompt()
    dbqa = build_retrieval_qa(cfg,llm, qa_prompt, vectordb)

    return dbqa

class LLMSource:
    Text:str
    Page:int

    def __init__(self,text,page) -> None:
        self.Text=text
        self.Page=page
class LLmResponse:
    result:str
    sources=[]

    def __init__(self) -> None:
        self.sources=[]
        self.result=None
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
        sort_keys=True, indent=4)
class LLmResponseEncoder(json.JSONEncoder):
        def default(self, o):
            return o.__dict__

if  __name__=='__main__':
    build_llm()