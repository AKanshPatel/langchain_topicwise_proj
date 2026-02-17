from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv


# Api key
load_dotenv()

# Model
chat_model = ChatGroq(
    model = "llama-3.1-8b-instant"
)

# Prompt 
prompt = PromptTemplate(
    template = "Write a summary for the following {poem}",
    input_variables= ["poem"]
)

parser = StrOutputParser()

# Creating a loader instance
loader = TextLoader("cricket.txt", encoding = "utf-8")

# Return the document format 
docs = loader.load()

print(docs) 
print(type(docs))

chain = prompt | chat_model | parser
response = chain.invoke({"poem": docs[0].page_content})

print(response)