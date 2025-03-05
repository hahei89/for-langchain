from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
import env_settings
from pathlib import Path

api_key = env_settings.API_KEY
# 创建文件路径
current_dir = Path.cwd()
file_path = current_dir/ "src" / "data.txt"

with open(file_path, encoding='utf-8') as f:
  str = f.read()
text_spliter = CharacterTextSplitter(chunk_size=100, chunk_overlap=5)
texts=text_spliter.split_text(str)
embedd = DashScopeEmbeddings(dashscope_api_key=api_key)
docsearch = Chroma.from_texts(texts, embedd)

query='说一下布朗尼本场的数据'
result=docsearch.similarity_search(query)
print(result)
print(len(result))