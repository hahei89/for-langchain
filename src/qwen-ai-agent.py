from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()
api_key=os.getenv("DASHSCOPE_API_KEY")

client = OpenAI(
  api_key=api_key,
  base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)


def basic_agent(query):
  response = client.chat.completions.create(
    model="qwen-max",
    messages=[
      {"role": "system", "content": "你是一个具有工具调用能力的智能助手"},
      {"role": "user", "content": query}
    ]
  )

  return response.choices[0].message.content

TOOLS={
  "web_search": {
    "description": "访问互联网获取实时信息",
    "params": {"query": "string"}
  },
  "math_solver": {
    "description": "执行复杂数学计算",
    "params": {"expression": "string"}
  }
}

def tool_dispatcher(tool_name, params):
  if tool_name == "web_search":
    return "web_search"
    # return search_engine(params["query"])
  elif tool_name == "math_solver":
    return eval(params["expression"])
  else:
    return "Tool not found"

#自动工具选择
def auto_agent(query):
  response = client.chat.completions.create(
    model="qwen-max",
    messages = [
      {"role": "user", "content": query}
    ],
    tools=[
      {
        "type": "function", "function": defs
      } for defs in TOOLS.values()
    ]
  )

  if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    return tool_dispatcher(tool_call.function.name, 
                           json.loads(tool_call.function.arguments)
                          )
  else:
    return response.choices[0].message.content
  
def customer_service(query):
  # context = [
  #     {"role": "system", "content": "你是一个专业客服，用中文回答"},
  #     {"role": "user", "content": query}
  # ]
  return basic_agent(query)

query = "我怎么才能让你帮我分析本地向量数据库中的数据"

response =customer_service(query)
print(response)