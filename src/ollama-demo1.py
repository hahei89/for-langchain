from ollama import chat
from ollama import ChatResponse
from langchain.chains import retrieval_qa
from langchain.chains.retrieval_qa.base
# response: ChatResponse = chat(model='DeepSeek-R1-Distill-Qwen-14B-GGUF:latest', messages=[
#   {
#     'role': 'user',
#     'content': 'Why is the sky blue?',
#   }
# ])
# print(response['message']['content'])
# # or access fields directly from the response object
# print(response.message.content)

stream = chat(
  model='DeepSeek-R1-Distill-Qwen-14B-GGUF:latest',
  messages=[{'role': 'system', 'content': '请用中文回答'}, {'role': 'user', 'content': 'Why is the sky blue?'}],
  stream=True
) 
for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)
