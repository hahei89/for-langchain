# 多轮对话
import os
from dotenv import load_dotenv
import dashscope

load_dotenv()
api_key = os.getenv("DASHSCOPE_API_KEY")

def get_response(messages):
  response=dashscope.Generation.call(
    api_key=api_key,
    model="qwen-plus",
    messages=messages,
    result_format="message"
  )

  return response

# 初始化一个 messages 数组
messages = [
    {
        "role": "system",
        "content": """你是一名百炼手机商店的店员，你负责给用户推荐手机。手机有两个参数：屏幕尺寸（包括6.1英寸、6.5英寸、6.7英寸）、分辨率（包括2K、4K）。
        你一次只能向用户提问一个参数。如果用户提供的信息不全，你需要反问他，让他提供没有提供的参数。如果参数收集完成，你要说：我已了解您的购买意向，请稍等。""",
    }
]

assistant_output="欢迎光临百联手机商店，您需要购买什么尺寸的手机"

while "我已了解您的购买意向" not in assistant_output:
  user_input=input("请输入： ")
  #将用户问题信息添加到mesages中
  messages.append({"role": "user", "content": user_input})
  assistant_output=get_response(messages).output.choices[0].message.content
  #将大模型的回复信息添加到messages列表中
  messages.append({"role":"assistant", "content": assistant_output})
  print(f"模型输出: {assistant_output}")
  print("\n")