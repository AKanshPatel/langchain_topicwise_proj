from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import load_prompt, ChatPromptTemplate
from langchain.messages import AIMessage

chat_template = ChatPromptTemplate([
    ('system', "You are a helpful {domain} expert."),
    ('human', 'Explain in simple terms, what is {topic}')
])


prompt = chat_template.invoke({
    'domain': 'Artifical intelligence', 
    'topic' : 'LangChain'   
})

print(prompt)

