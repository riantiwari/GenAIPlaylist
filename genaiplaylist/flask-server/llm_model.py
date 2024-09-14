import os
import langchain
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Function to parse the list
def parseable_list(step_list):
    topics_list = step_list.split('• ')[1:]
    topics_list = [topic.strip() for topic in topics_list]
    return topics_list

class llm_response():
    llm = Ollama(model="llama2")
    systm_request = "List key subtopics to learn any skill or topic as single-line bullet points, with each bullet point being a standalone search query suitable for YouTube. Ensure there is no additional text, context, or subtopics. Each bullet should be a concise, clear search term that can be directly copied and pasted into the YouTube search bar, formatted as a single line for easy parsing. Do this without repeats."
    prompt = ChatPromptTemplate.from_messages([
        ("system", systm_request),
        ("user", "{input}")
    ])
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    # Now accept a dynamic query
    @classmethod
    def get_response(cls, query):
        res = cls.chain.invoke({"input": query + "?"})
        return parseable_list(res)
