from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableBranch, RunnablePassthrough

# Api key
load_dotenv()

# Model
chat_model = ChatGroq(
    model = "llama-3.1-8b-instant"
)

# Prompts
prompt1 = PromptTemplate(
    template = "Write a detailed report on {topic}", 
    input_variables = ["topic"]
)

prompt2 = PromptTemplate(
    template = "Summarize the following report \n {text}", 
    input_variables = ["text"]
)

parser = StrOutputParser()

report_generation_chain = RunnableSequence(prompt1, chat_model, parser)

branch_chain = RunnableBranch(
    (lambda x :len(x.split()) > 500, RunnableSequence(prompt2, chat_model, parser)),
    RunnablePassthrough() 
)

final_chain = RunnableSequence(report_generation_chain, branch_chain)
response = final_chain.invoke({"topic": 'Machine learning'})
 
print(response)