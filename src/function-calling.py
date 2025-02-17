import os
from dotenv import load_dotenv
import random
from openai import OpenAI
from datetime import datetime
import json

load_dotenv()
api_key=os.getenv("DASHSCOPE_API_KEY")

# 模拟天气查询工具 返回结果实例:北京今天是雨天
def get_current_weather(arguments):
  # 定义备选的天气条件列表
  weather_conditions=["晴天", "雨天", "多云"]
  # 随机选择一个天气条件
  random_weather=random.choice(weather_conditions)
  # 从JSON中提取位置信息
  location=arguments["location"]
  # 返回格式化的天气信息
  return f"{location}今天是{random_weather}"

# 查询当前时间的工具 返回结果示例: “当前时间：2024-04-15 17:15:18。“
def get_current_time():
  # 获取当前日期和时间
  current_datetime=datetime.now()
  # 格式化当前日期和时间
  formatted_time=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
  # 返回格式化的当前时间
  return f"当前时间:{formatted_time}。"

# 测试工具函数并输出结果，运行后续步骤时可以去掉以下四句测试代码
# print("测试工具输出：")
# print(get_current_weather({"location": "上海"}))
# print(get_current_time())
# print("\n")

# 步骤2：创建tools数组
tools=[{
  "type": "function",
  "function": {
    "name": "get_current_time",
    "description": "当你想知道现在的时间时非常有用"
  }
},{
  "type": "function",
  "function": {
    "name": "get_current_weather",
    "description": "当你想知道现在的天气时非常有用",
    "parameters": {
      "type": "object",
      "properties": {
        "location": {
          "type": "string",
          "description": "城市或县区"
        }
      },
      "required": ["location"]
    }
  }
}]

# 步骤3：创建messages数组
messages=[
  {
    "role": "system",
    "content": """你是一个很有帮助的助手。如果用户提问关于天气的问题，请调用 ‘get_current_weather’ 函数;
     如果用户提问关于时间的问题，请调用‘get_current_time’函数。
     请以友好的语气回答问题。""",
  },
  {
    "role": "user",
    "content": "上海天气"
  }
]

# 步骤4: 发起function calling
client = OpenAI(
  api_key=api_key,
  base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

def function_calling():
  completion=client.chat.completions.create(
    model="qwen-plus",
    messages=messages,
    tools=tools
  )
  return completion

completion=function_calling()
# 从返回的结果重化工获取函数名称和入参
function_name=completion.choices[0].message.tool_calls[0].function.name
arguments_string=completion.choices[0].message.tool_calls[0].function.arguments

arguments = json.loads(arguments_string)
function_mapper = {
  "get_current_weather": get_current_weather,
  "get_current_time": get_current_time
}

function = function_mapper[function_name]
if arguments == {}:
  function_output=function()
else:
  function_output=function(arguments)
print(function_output)