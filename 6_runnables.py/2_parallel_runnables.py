from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel
from langchain_core.output_parsers import StrOutputParser


# API Key
load_dotenv()

# Model 
chat_model = ChatGroq(
    model = "llama-3.1-8b-instant"
)

# Praser
parser = StrOutputParser()

# Prompt 
prompt1 = PromptTemplate(
    template = "Generate a 1 line tweet about the {topic}", 
    input_variables = ["topic"]
)

prompt2 = PromptTemplate(
    template = "Generate a Linkedin post (short) about the {topic}", 
    input_variables = ["topic"]
)

parallel_chain = RunnableParallel(
    {
        'tweet' : RunnableSequence(prompt1, chat_model, parser), 
        'post' : RunnableSequence(prompt2, chat_model, parser)
    }
)

response = parallel_chain.invoke({'topic': 'AI'})

print(response["tweet"])
print(response["post"])