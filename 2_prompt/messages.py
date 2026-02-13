from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv


# Import API keys
load_dotenv()

# Model Initialization
chat_model = ChatGroq(
    model = "llama-3.1-8b-instant"
)


messages = [
    SystemMessage(content = "You are a helpfull assistant"),
    HumanMessage(content = "Tell me about LangChain")
]

response = chat_model.invoke(messages)
messages.append(AIMessage(content = response.content))

print(messages)
