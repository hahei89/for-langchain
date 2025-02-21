import json
import os
from dotenv import load_dotenv
from http import HTTPStatus
import dashscope
import env_settings as env_settings

# load_dotenv()
# api_key=os.getenv("DASHSCOPE_API_KEY")
api_key=env_settings.API_KEY
# 创建一个新的空线程
thread = dashscope.Threads.create(api_key=api_key)
# 检查线程创建是否成功
# if thread.status_code == HTTPStatus.OK:
#     print(f"线程创建成功。线程 ID：{thread.id}")
#     print("现在你可以开始与AI助手进行绘画对话了。")
# else:
#     print(f"线程创建失败。状态码：{thread.status_code}")
#     print(f"错误码：{thread.code}")
#     print(f"错误信息：{thread.message}")
# 创建一条消息，告诉助手需要做什么
message = dashscope.Messages.create(
  thread_id=thread.id,
  api_key=api_key,
  content='请帮我画一幅布偶猫的画'
)
# 检查消息创建是否成功
# if message.status_code == HTTPStatus.OK:
#     print('消息创建成功！消息 ID：%s' % message.id)
# else:
#     print('消息创建失败。状态码：%s，错误码：%s，错误信息：%s' % (message.status_code, message.code, message.message))
# 使用Qwen-Max创建一个新的绘画助手
painting_assistant = dashscope.Assistants.create(
  model="qwen-max",
  api_key=api_key,
  name="Art Maestro 艺术大师", #助手名称
  descriptions="一个专注于绘画和艺术知识的AI助手",
  instructions='''你是一个专家级的绘画助手。请提供关于绘画技巧、艺术史和创意指导的详细信息。
    使用 夸克搜索 查找关于艺术主题的准确信息，并在需要时利用图像生成工具创建视觉示例。''',
  tools=[
    {
      'type': 'quark_search', #用于搜索广泛信息的工具
      'description': '使用此工具查找关于绘画技巧、艺术史和艺术家的详细信息。'
    },
    {
      'type': 'text_to_image', # 用于根据描述生成图像的工具
      'description': '使用此工具创建绘画风格、技巧或艺术概念的视觉示例。'
    }
  ]
)

# 打印助手的ID以确认创建成功
# print(f"绘画助手 'Art Maestro' 创建成功，ID：{painting_assistant.id}")

run = dashscope.Runs.create(thread_id=thread.id,assistant_id=painting_assistant.id,api_key=api_key)

if run.status_code != HTTPStatus.OK:
    print('创建助手失败，状态码：%s，错误码：%s，错误信息：%s' % (run.status_code, run.code, run.message))
else:
    print('创建助手成功，ID：%s' % run.id)

# 等待运行完成或需要操作
run = dashscope.Runs.wait(run.id, thread_id=thread.id, api_key=api_key)

if run.status_code != HTTPStatus.OK:
    print('获取运行状态失败，状态码：%s，错误码：%s，错误信息：%s' % (run.status_code, run.code, run.message))
else:
    print(run)

msgs = dashscope.Messages.list(thread_id=thread.id,api_key=api_key)
if msgs.status_code != HTTPStatus.OK:
    print('获取消息失败，状态码：%s，错误码：%s，错误信息：%s' % (msgs.status_code, msgs.code, msgs.message))
else:
    print(json.dumps(msgs, default=lambda o: o.__dict__, sort_keys=True, indent=4))