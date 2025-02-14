import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import HumanMessage, BaseMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.graph.message import add_messages
from typing_extensions import Annotated, TypedDict
from typing import Sequence

load_dotenv()
api_key = os.getenv("DASHSCOPE_API_KEY")

prompt_template = ChatPromptTemplate.from_messages([
  ("system", "你是一名非常有用的助手。用{language}尽力回答所有的问题"),
  MessagesPlaceholder(variable_name="messages")
])
class State(TypedDict):
  messages: Annotated[Sequence[BaseMessage], add_messages]
  language: str

model = ChatTongyi(model="qwen-max", api_key=api_key)
# model.invoke([HumanMessage(content="你好!我是小明")])
workflow = StateGraph(state_schema=State)

def call_model(state: State):
  prompt = prompt_template.invoke(state)
  response = model.invoke(prompt)

  return {"messages": response}

workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

config = { "configurable": {"thread_id": "abc123"}}
query="你好！我是小明"
input_messages=[HumanMessage(query)]
language="Chinese"
output=app.invoke({"messages": input_messages, "language": language}, config=config)
output["messages"][-1].pretty_print()

query="我叫什么名字"
input_messages=[HumanMessage(query)]
output=app.invoke({"messages": input_messages}, config=config)
output["messages"][-1].pretty_print()
