from dotenv import load_dotenv
from langchain_groq import ChatGroq
from typing import TypedDict, Annotated

# import API keys
load_dotenv()

# Initialize the model: 
model = ChatGroq(
    model = "llama-3.1-8b-instant"
) 

# Schema 
class Review(TypedDict):
    key_themes = Annotated[list[str], "Write down all the key themes discussed in the review"]
    summary :Annotated[str, "A brief summary of the review"] 
    sentiment : Annotated[str, "Return sentiment of review either Positive, Negative, Neutral"]
    

structured_model = model.with_structured_output(Review)

response = structured_model.invoke("""Good product Pros- Monster Battery, Durable body, strong performance, Lags or glitches are not there, Loud dual Speaker
Cons- ultra wide camera is missing, LCD display is there, additional noise cancellation microphone not provided,
Fingerprint reader is provided on side button ( works fast), The phone have dimensity 7300 processor which is beast at this price point
They should add 90 fps support in bgmi in next update because the phone is capable for that Overall phone is good worth to buy under 15000 category
Plus point is origin OS coming in December
""")

print(response)