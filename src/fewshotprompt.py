import os
from dotenv import load_dotenv
from langchain_community.llms.tongyi import Tongyi
from langchain.prompts import FewShotPromptTemplate, PromptTemplate

load_dotenv()
api_key = os.getenv('DASHSCOPE_API_KEY')

examples = [
  {
    "word": "大",
    "antonym": "小"    
  },
  {
    "word": "左",
    "antonym": "右"    
  },
  {
    "word": "上",
    "antonym": "下"    
  }
]

example_template = """
单词: {word}
反义词: {antonym}\n
"""

example_prompt = PromptTemplate(input_variables=["word", "antonym"], template=example_template)
few_shot_prompt = FewShotPromptTemplate(
  examples = examples,
  example_prompt=example_prompt,
  prefix="给出每个单词的反义词",
  suffix="单词: {input}\n反义词",
  input_variables=["input"],
  example_separator="\n"
)

prompt_text = few_shot_prompt.format(input = '粗')
llmModel = Tongyi(model="qwen-max",  api_key=api_key)
# fewshot提示不支持langchain的管道操作符|的写法
# chain = few_shot_prompt | llmModel

res = llmModel.invoke(prompt_text)
print(res)