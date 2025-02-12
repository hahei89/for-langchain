import os
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import DashScopeEmbeddings
# import dashscope
import json
from http import HTTPStatus
from langchain_core.vectorstores import InMemoryVectorStore

load_dotenv()
api_key=os.getenv("DASHSCOPE_API_KEY")
documents = [
  Document(
    page_content="Dogs are great companions, known for their loyalty and friendliness",
    metadata={"source": "mammal-pets-doc"}
  ),
  Document(
    page_content="Cats are independent pets that often enjoy their own space.",
    metadata={"source": "mammal-pets-doc"}
  )
]

current_dir = os.getcwd()
file_path = os.path.join(current_dir, 'data', 'input', 'DeepSeekR1.pdf')
loader = PyPDFLoader(file_path)
docs = loader.load()
# print(len(docs))
# print(f"{docs[0].page_content[:200]}\n")
# print(docs[0].metadata)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200, add_start_index=True)
all_splits = text_splitter.split_documents(docs)
# print(len(all_splits))

embeddings = DashScopeEmbeddings(model="text-embedding-v3", dashscope_api_key=api_key)
# vector_1 = embeddings.embed_query(all_splits[0].page_content)
# vector_2 = embeddings.embed_query(all_splits[1].page_content)

vector_store=InMemoryVectorStore(embeddings)
ids=vector_store.add_documents(documents=all_splits)

results = vector_store.similarity_search("生成图文的技巧提示")

print(results[0])