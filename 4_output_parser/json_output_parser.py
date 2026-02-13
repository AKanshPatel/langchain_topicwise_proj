from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# Api key load: 
load_dotenv()

# Model Endpoint: 
llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct",
    task = "text-generation"
)

# Wrapper: 
chat_model = ChatHuggingFace(
    llm = llm
)

parser = JsonOutputParser()

template1 = PromptTemplate(
    template = "Give me the name, age and city of fictional persons \n {format_instruction}", 
    input_variables = [], 
    partial_variables = {'format_instruction': parser.get_format_instructions()})

prompt = template1.format()

response = chat_model.invoke(prompt)

final_result = parser.parse(response.content)

print(final_result)

print(type(final_result))