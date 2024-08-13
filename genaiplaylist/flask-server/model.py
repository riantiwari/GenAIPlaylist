from langchain_community.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI
import os

def main():
    # Load the OpenAI API key from an environment variable
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

    # Set up the OpenAI model using the correct class and parameter
    llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo", openai_api_key=api_key)

    # Define a prompt template
    template = """
You are an AI that generates lists based on specific queries. 
Given the following query, generate a list of items that are relevant to the query.

Query: {query}

List:
"""

    prompt = PromptTemplate(template=template, input_variables=["query"])

    # Example queries
    query1 = "Top 5 books on finance"
    query2 = "Best programming languages to learn in 2024"

    # Generate lists
    list1 = generate_list(llm, prompt, query1)
    list2 = generate_list(llm, prompt, query2)

    # Print the results
    print("List 1:", list1)
    print("List 2:", list2)

def generate_list(llm, prompt, query):
    # Format the prompt with the query
    formatted_prompt = prompt.format(query=query)
    
    # Run the prompt through the LLM
    response = llm(formatted_prompt)
    
    return response

# Entry point for the script
if __name__ == "__main__":
    main()
