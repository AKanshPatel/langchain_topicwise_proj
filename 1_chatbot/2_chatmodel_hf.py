# How to access the model using Hugging face API call
# Open Source models 
# Steps: 
# Import API key -> Hugging face inference -> Chat Support wrapper -> Invoke

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

# Create a Hugging Face endpoint (important) - Hugging Face Inference API.
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

# Wrap it with ChatHuggingFace - Treat this model as it support chat support.
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)