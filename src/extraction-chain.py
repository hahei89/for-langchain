import os
from dotenv import load_dotenv
from typing import Optional
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatTongyi

load_dotenv()
api_key = os.getenv("DASHSCOPE_API_KEY")
class Person(BaseModel):
  name: Optional[str] = Field(default=None, description="人物名称")
  hair_color: Optional[str]=Field(
    default=None, description="人物的头发颜色"
  )
  height_in_meters: Optional[str]=Field(
    default=None,
    description="人物的身高,单位为米"
  )

prompt_template = ChatPromptTemplate.from_messages(
  [
    (
      "system",
      """
      你是一名专业的提取算法专家。只需从文本中提取相关信息即可。
      如果你不知道需要提取的属性的值,请返回该属性值为空。
      """
    ),
    ("human", "{text}")
  ]
)

llm = ChatTongyi(model="qwen-max", api_key=api_key)
structured_llm = llm.with_structured_output(Person)
text = "小明身高1.88米,头发颜色为黑色。"
prompt = prompt_template.invoke({"text": text})
res = structured_llm.invoke(prompt)

print(res)