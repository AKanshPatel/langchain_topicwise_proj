# How to access the model using model's official API
# Closed Source models
# Steps: 
# Import API keys -> Initialization -> Invoke -> response parse. 

from langchain_groq import ChatGroq 
from dotenv import load_dotenv

load_dotenv() # Load from .env

# Initialization: 
model = ChatGroq(
    model = "llama-3.1-8b-instant",
    temperature= 0.1, # Randomness in 0.0 to 0.3 are deterministic/code generation if Temperature is close to 0 then the LLM will give similar output.
    max_completion_tokens = 5, # Tokens = Words roughly
)

result = model.invoke("lets say Delhi somehow disappear then what else can be the capital of India, give me just one")

print(result.content)
