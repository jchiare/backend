import logging
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

    donut_name: str = Field(description="The name of a fancy donut")


llm = ChatOpenAI(
    model="gpt-4o", temperature=0.5, request_timeout=120, max_retries=3
).bind_tools([Answer], strict=True)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You work for a creative brand agency that speciliazes in creating names of baked goods."
            "The user will provide a list of existing donut names that are all lowercased."
            "Your goal is to generate 5 new fancy donuts names where at least one of the new fancy donut names will contain a substring, delimited by whitespaces, in the existing list"
            "For example, if the existing donut names are ['Raised', 'Old Fashioned'], then you can return ['Berlin Bruiser', 'New Age Classics', 'Sugar Addiction', 'VW for Villy Wonka', 'Old Fashioned Smokey']",
        ),
        (
            "user",
            "{donuts}",
        ),
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


def create_new_donut_names(existing_donuts: list[str]) -> list[str]:
    result = chain.invoke(
        {
            "donuts": existing_donuts,
        }
    )

    return [donut.donut_name for donut in result]


donut_naming_agent = (
    AgentExecutor(agent=chain, tools=[]).with_types(
        input_type=Input, output_type=Output
    )
) | (lambda x: x["output"])
