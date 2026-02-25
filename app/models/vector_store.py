#document must be stored in vectore data base. here embedding model is loaded. initialize the vectore data base

#document -> vector embedding -> stored in vector db

import chromadb  # vector db can be replaced by pinecone , fiass, weviate 
from langchain.vectorestores import Chroma
from langchain.embedding.openai import OpenAIEmbeddings

class vectorStore:
    def __init__(self, path):
        self.embeddings = OpenAIEmbeddings()
        self.vector_store = Chroma(
            persist_directory=path,
            embedding_function=self.embeddings
        )

def add_documents(self,documents):
    self.vectore_store.add_documents(documents)

def similarity_search(self,qury,k=4):
    return self.vectore_store.similarity_search(query, k=k)