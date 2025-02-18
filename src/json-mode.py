import os
from dotenv import load_dotenv
import dashscope

load_dotenv()
api_key=os.getenv("DASHSCOPE_API_KEY")
# dashscope.base_http_api_url='https://dashscope.aliyuncs.com/api/v1'

messages=[
  {
    "role": "system",
    "content": """你需要提取出name（名字，为string类型）、age（年龄，为string类型）与email（邮箱，为string类型），请输出JSON 字符串，不要输出其它无关内容。
     示例：
     Q：我叫张三，今年25岁，邮箱是zhangsan@example.com
     A：{"name":"张三","age":"25岁","email":"zhangsan@example.com"}
     Q：我叫李四，今年30岁，我的邮箱是lisi@example.com
     A：{"name":"李四","age":"30岁","email":"lisi@example.com"}
     Q：我叫王五，我的邮箱是wangwu@example.com，今年40岁
     A：{"name":"王五","age":"40岁","email":"wangwu@example.com"}"""
  },
  {
    "role": "user",
    "content": "大家好，我叫刘五，今年34岁，邮箱是liuwu@example.com",
  }
]

response=dashscope.Generation.call(
  api_key=api_key,
  model="qwen-plus",
  messages=messages,
  result_format="message",
  response_format={'type': 'json_object'}
)
print(response.output.choices[0].message.content)