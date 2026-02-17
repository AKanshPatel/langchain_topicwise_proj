from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


# API Key
load_dotenv()

# Model 
chat_model = ChatGroq(
    model = "llama-3.1-8b-instant"
)
    
# Parser
parser = StrOutputParser()

# Prompt 
prompt1 = PromptTemplate(
    template = "Tell me a joke in 1 line"
)

prompt2 = PromptTemplate(
    template = "Explain me the joke - {joke_text}", 
    input_variables = ["joke_text"] 
)


# Chain 

chain = RunnableSequence(prompt1, chat_model, parser)
parallel_chain = RunnableParallel(
    {
        'joke' :  RunnablePassthrough(),
        'explanation' : RunnableSequence(prompt2, chat_model, parser)
    }
)

final_chain = RunnableSequence(chain, parallel_chain)
response = final_chain.invoke({})

print(response["joke"])
print("--------------------")
print(response["explanation"])
