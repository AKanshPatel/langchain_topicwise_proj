from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import load_prompt
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage




# Import API keys
load_dotenv()

# Model Initialization
chat_model = ChatGroq(
    model = "llama-3.1-8b-instant"
)


chat_history = [
    SystemMessage(content = "You are a helpfull assistant")
]

while True: 
    user_input = input("You: ")
    if user_input == "exit" or user_input == "Exit" : 
        break
    chat_history.append(HumanMessage(content= user_input))
    response = chat_model.invoke(chat_history)
    chat_history.append(AIMessage(content = response.content))
    print(f"AI: {response.content}")
    

for chat in chat_history:
    print(chat)