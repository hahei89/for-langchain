import os
from dotenv import load_dotenv
import dashscope

load_dotenv()
api_key=os.getenv("DASHSCOPE_API_KEY")

messages=[
  {"role":"system","content":"你是有用的助手"},
  {"role":"user","content":"你是谁?"}
]
responses = dashscope.Generation.call(
  model="qwen-plus",
  api_key=api_key,
  messages=messages,
  result_format="messages",
  stream=True,
  # 增量式输入输出
  incremental_output=True
)

full_content=""
for response in responses:
  content = response.output.text
  full_content += content
  print(content)
print(f"完整内容为: {full_content}")