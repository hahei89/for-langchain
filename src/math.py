import os
from dotenv import load_dotenv
import dashscope

load_dotenv()
api_key=os.getenv("DASHSCOPE_API_KEY")

messages=[
  {"role":"user", "content": "Find the value of $x$ that satisfies the equation $4x+5 = 6x+7$."}
]

response = dashscope.Generation.call(
  api_key=api_key,
  model="qwen-math-turbo",
  messages=messages,
  result_format="message"
)

print(response)