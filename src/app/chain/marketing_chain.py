import logging
from openai import APIError
from langchain.agents import AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai.chat_models import ChatOpenAI
from langchain.output_parsers.openai_tools import PydanticToolsParser


class Input(BaseModel):
    donuts: list[str]


class Output(BaseModel):
    output: str


class Answer(BaseModel):
    """Response from the LLM model"""
    donut_name: str = Field(description="fancy donut name")

# Please use a free OpenAI API key while working on the challenge and remove the key before sending us the challenge
OPENAI_API_KEY = ""

llm = ChatOpenAI(model="gpt-4o", temperature=0, request_timeout=120, openai_api_key=OPENAI_API_KEY).bind_tools([Answer])

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an excellent in creating fancy names for a round-shaped food."),
        ("user", "You are marketing director of a donut shop and you need to come up "
                 "with a fancy name for our new donut."
                 "Here is our list of donut names for inspiration: {donuts}."),
    ]
)

chain = (
        {
            "donuts": lambda x: x["donuts"],
        }
        | prompt
        | llm
        | PydanticToolsParser(tools=[Answer])
)


def create_new_donut_name(existing_donuts: list[str]) -> str:
    answer = chain.invoke({
        'donuts': existing_donuts,
    })

    return answer.donut_name


donut_naming_agent = (AgentExecutor(agent=chain, tools=[])
                      .with_types(input_type=Input, output_type=Output)) | (lambda x: x["output"])

