from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

def main():
    llm = Ollama(model="llama2")
    systm_request = "List the key subtopics to learn any skill or topic, each as a separate string, formatted for easy parsing in Python. Don't say anything before or after the list and don't make the list numbered but keep it ordered. The items in the list should be sentences you can paste into youtube search bar"
    prompt = ChatPromptTemplate.from_messages([
    ("system", systm_request),
    ("user", "{input}")
    ])
    chain = prompt | llm 
    res = chain.invoke({"input": "How to learn finance to be able to get into investment banking?"})
    print(res)


# Entry point for the script
if __name__ == "__main__":
    main()
