import os
from dotenv import load_dotenv
import dashscope

load_dotenv()
api_key=os.getenv('DASHSCOPE_API_KEY')
messages=[
  {
    "role": "system",
    "content": "请对“春天来了，大地” 这句话进行续写，来表达春天的美好和作者的喜悦之情"
  },
  # 大模型返回的内容并不包含您指定的前缀内容，您需要手动将前缀内容与返回结果拼接。
  {
    "role": "assistant",
    "content": "春天来了，大地",
    "partial": True
  }
]

response = dashscope.Generation.call(
  api_key=api_key,
  model="qwen-plus",
  messages=messages,
  result_format="message"
)

print(response.output.choices[0].message.content)