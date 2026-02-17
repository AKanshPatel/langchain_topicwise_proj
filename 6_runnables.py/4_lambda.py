from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough, RunnableParallel, RunnableSequence
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

# function:
def word_count(text):
    return len(text.split())

# Api key
load_dotenv()

# Model
chat_model = ChatGroq(
    model = "llama-3.1-8b-instant"
)


# Prompt 
prompt1 = PromptTemplate(
    template = "Tell me a 1 line joke of topic: {topic}",
    input_variables = ["topic"] 
)

# prompt2 = PromptTemplate(
#     template = "Explain me the joke {joke}", 
#     input_variables = ["joke"] 
    
# )

parser = StrOutputParser()

# Chain 
joke_generate_chain = RunnableSequence(prompt1, chat_model, parser)

paralle_chain = RunnableParallel(
    {
        'joke' : RunnablePassthrough(),
        'count_words' : RunnableLambda(word_count), 
        # 'explain' : RunnableSequence(prompt2, chat_model, parser), 
        
    }
)

final_chain = RunnableSequence(joke_generate_chain, paralle_chain)
response = final_chain.invoke({"topic": "AI"})
print(response)