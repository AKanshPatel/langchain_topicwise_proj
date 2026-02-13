# Simple Chain
# User -> Prompt -> LLM -> Response display

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Api key 
load_dotenv()


# Model Initialization: 
chat_model = ChatGroq(
    model = "llama-3.1-8b-instant"
)

# Prompt: 
prompt = PromptTemplate(
    template = "generate 2 interesting facts about {topics}",
    input_variable = ["topics"]
)

# Parser 
parser = StrOutputParser()

# Chain: We use pipe operator to declare the steps of chain
# We use LCEL - Langchain expression language 
chain = prompt | chat_model | parser

chain.get_graph().print_ascii()

response = chain.invoke({'topics': 'Black hole'})

print(response)