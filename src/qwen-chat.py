# 导入相关包
import os
from dotenv import load_dotenv
from langchain_community.llms import tongyi
from langchain.prompts import PromptTemplate

load_dotenv()
api_key = os.getenv("DASHSCOPE_API_KEY")
llmModel = tongyi.Tongyi(model="qwen-max",  api_key=api_key)

template='''
        你的名字是小黑子,当人问问题的时候,你都会在开头加上'唱,跳,rap,篮球!',然后再回答{question}
    '''
prompt = PromptTemplate(
  template=template,
  input_variables=["question"]
)
chain = prompt | llmModel

question='你是谁'

res = chain.invoke({ "question": question })

print(res)

