import os
from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI
# 加载环境变量
load_dotenv()
# 获取环境变量中的api_key
api_key = os.getenv("DASHSCOPE_API_KEY")
# 获取模型client
client = OpenAI(
  api_key=api_key,
  base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
# 创建文件路径
current_dir = Path.cwd()
file_path = current_dir / "README.md"
# 创建文件对象
file_object = client.files.create(
  file=file_path,
  purpose="file-extract"
)
# 初始化messages列表
completion = client.chat.completions.create(
  model="qwen-long",
  messages=[
    {"role":"system", "content": "你是有个有用的助手"},
    {"role":"system", "content": f"fileid://{file_object.id}"},
    {"role": "user", "content": "这篇文章讲了什么"}
  ],
  stream=True,
  stream_options={"include_usage": True}
)

full_content=""
for chunk in completion:
  if chunk.choices and chunk.choices[0].delta.content:
    full_content += chunk.choices[0].delta.content
    print(chunk.model_dump())
print({full_content})