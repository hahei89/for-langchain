import os
from dotenv import load_dotenv
import dashscope

load_dotenv()
api_key = os.getenv("DASHSCOPE_API_KEY")
messages=[
  { "role": "user", "content": "我看到这个视频后没有笑"}
]
translation_options = {
  "source_lang":"Chinese",
  "target_lang":"English"
}
response= dashscope.Generation.call(
  api_key=api_key,
  model="qwen-mt-turbo",
  messages=messages,
  result_format="message",
  translation_options=translation_options
)

print(response.output.choices[0].message.content)