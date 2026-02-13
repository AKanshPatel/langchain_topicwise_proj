from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


# APi Keys 
load_dotenv()

# Model Endpoint
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

# Wrapper
chat_model = ChatHuggingFace(
    llm = llm
)

# 1st template: 
template1 = PromptTemplate(
    template= """ Write detailed report on {topic}""",
    input_variables= ['topic']
)

# 2nd template: 
template2 = PromptTemplate(
    template = """Write the 5 line summary on following text. /n{text}""",
    input_variables= ['text']  
) 

parser = StrOutputParser()

chain = template1 | chat_model | parser | template2 | chat_model | parser

results = chain.invoke({'topic': 'Black hole'})

print(results)