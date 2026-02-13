# user -> Topic -> prompt -> LLM -> report -> prompt -> LLM -> Respose

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# API
load_dotenv()

# Model: 
chat_model = ChatGroq(
    model = "llama-3.1-8b-instant"
)

# Prompt : 
prompt1 = PromptTemplate(
    template = "Tell me something about {topics}", 
    input_variables = ["topics"]
)

prompt2 = PromptTemplate(
    template = "Give me the 4 keywords in the article : {text}",
    input_variables= ["text"]
)

# Parser: 
parser = StrOutputParser()

# Chain: 
chain = prompt1 | chat_model | parser | prompt2 | chat_model | parser 

response = chain.invoke({"topics": "Black hole"})

chain.get_graph().print_ascii()

print(response)