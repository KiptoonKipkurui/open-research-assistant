"""
Database module providing functionality to vectorize 
Documents and perform similarity searches
"""
import box
from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS


# Build vector database
def build_db(config: box.Box):
    """
    build the FAISS database 
    """
    loader = DirectoryLoader(config.DATA_PATH, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE, chunk_overlap=config.CHUNK_OVERLAP
    )
    print(f"availabledocuments: {len(documents)}")
    texts = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
    )

    vectorstore = FAISS.from_documents(texts, embeddings)
    vectorstore.save_local(config.DB_FAISS_PATH)

if __name__ == "__main__":
    cfg = box.box_from_file("./config/config.yml", "yaml")
    build_db(cfg)
