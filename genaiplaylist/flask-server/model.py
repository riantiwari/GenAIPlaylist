from langchain_community.llms import Ollama
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
import os

def main():
    llm = Ollama(model="llama2")
    response = llm.invoke("What is the capital of Russia?")
    print(response)
    # prompt = ChatPromptTemplate.from_messages([
    # ("system", "You are a world class technical documentation writer."),
    # ("user", "{input}")
    # ])
    #chain = prompt | llm 
    #chain.invoke({"input": "how can langsmith help with testing?"})
    #output_parser = StrOutputParser()
    #chain = prompt | llm | output_parser
    #chain.invoke({"input": "how can langsmith help with testing?"})chain.invoke({"input": "how can langsmith help with testing?"})


# Entry point for the script
if __name__ == "__main__":
    main()
