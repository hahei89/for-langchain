# 导入相关包
import os
from dotenv import load_dotenv
from langchain_community.llms import tongyi
from langchain.prompts import PromptTemplate
load_dotenv()
api_key = os.getenv("DASHSCOPE_API_KEY")
llmModel = tongyi.Tongyi(model="qwen-max",  api_key=api_key)
template='''
        用50个字描述{question}
    '''
prompt = PromptTemplate(
  template=template,
  input_variables=["question"]
)
chain = prompt | llmModel

question='生命的意义在于什么'

res = chain.invoke({ "question": question })

print(res)

