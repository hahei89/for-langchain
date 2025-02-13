import os
import dotenv
from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI   qwen-max不兼容ChatOpenAi
from langchain_community.chat_models import ChatTongyi
from pydantic import BaseModel, Field

dotenv.load_dotenv()
api_key = os.getenv("DASHSCOPE_API_KEY")
base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
tagging_prompt = ChatPromptTemplate.from_template(
  """
  从以下段落中提取所需的信息。仅提取“分类”功能中提到的属性。
  Passage:
  {input}
  """
)

class Classifycation(BaseModel):
  sentiment:str = Field(description="The sentiment of the text.")
  aggresiveness: int = Field(description="How aggressive the txet is on a scale from 1 to 10.")
  language: str = Field(description="The language the text is written in.")
llm = ChatTongyi(temperature=0, model="qwen-max", api_key=api_key).with_structured_output(Classifycation)

inp = "我非常高兴认识你！我相信我们会是非常好的朋友！"
prompt = tagging_prompt.format(input=inp)

response = llm.invoke(input=prompt)
print(response)