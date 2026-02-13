from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import PydanticOutputParser 
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from typing import Literal

# API key 
load_dotenv()

# Model:
chat_model = ChatGroq(
    model = "llama-3.1-8b-instant"
)  

# Base class - Pydantic class
class Feedback(BaseModel): 
    sentiment : Literal["positive", "negative"] = Field(description = "Give me the sentiment of the given feedback" )

# Parser - Setup parser + inject the instructions 
parser = PydanticOutputParser(pydantic_object = Feedback)

# prompt
prompt1 = PromptTemplate(
    template = "Analyze the following feedback and classify it strictly as positive or negative.\n {format_instructions} \n Feedback {feedback}",
    input_variables = ["feedback"], 
    partial_variables = {"format_instructions": parser.get_format_instructions()} 
)

# Chain 
sentiment_chain = prompt1 | chat_model | parser

response = sentiment_chain.invoke([{'feedback': "Terrible product Cons- ultra wide camera is missing, LCD display is there, additional noise cancellation microphone not provided"}]).sentiment

print(response)
