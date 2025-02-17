import os
from dotenv import load_dotenv
import dashscope

load_dotenv()
api_key=os.getenv("DASHSCOPE_API_KEY")

messages=[
  {"role":"user", "content": "在一元方程$4x+5 = 6x+7$中，$x$的值是多少?"}
]

response = dashscope.Generation.call(
  api_key=api_key,
  model="qwen-math-turbo",
  messages=messages,
  result_format="message"
)

print(response)