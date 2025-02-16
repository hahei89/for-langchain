import os
from dotenv import load_dotenv
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
load_dotenv()

# 为了翻墙后不再代理报错
os.environ['http_proxy'] = 'http://127.0.0.1:7890'
os.environ['https_proxy'] = 'http://127.0.0.1:7890'
api_key = os.getenv('OPENAI_API_KEY')
model=ChatOpenAI(model="", temperature=0, api_key=api_key)

msg = [
  SystemMessage(content="请将以下的内容翻译成英文"),
  HumanMessage(content="你好，请问你要去哪里")
]

res = model.invoke(msg)
print(res)