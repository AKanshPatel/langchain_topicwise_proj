# Template of prompt is loaded from json file
# prompt-generator.py : Execute to create json file.

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import load_prompt
import streamlit as st

# Import API keys
load_dotenv()

# Model Initialization
chat_model = ChatGroq(
    model = "llama-3.1-8b-instant"
)
## For invokation: chat_model.invoke()


# Streamlit UI 
st.header("Research paper summarizer")

paper_name = st.text_input("Enter the name of the paper")

length_type = st.selectbox("Length of the summary:", ["Short", "Medium", "Long"])


# Prompt Template: Loaded from the json file.
template = load_prompt(
    "template.json"
)

if st.button("Summarize"): 
    # Create chain
    chain = template | chat_model
    # Invoke Chain 
    response = chain.invoke( {
        "paper_input" : paper_name,
        "lengh_input" : length_type
    })
    st.write(response.content)
