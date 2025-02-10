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
单词: {work}
反义词: {antonym}\\n
"""

example_prompt = PromptTemplate(input_variables=["word", "antonym"], template=example_template)
few_shot_prompt = FewShotPromptTemplate(
  examples,
  example_prompt=example_template,
  prefix="给出每个单词的反义词",
  suffix="单词: {input}\\n反义词",
  input=["input"],
  example_separator="\\n"
)
