from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


# Chat Template
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpfull support agent'),
    MessagesPlaceholder(variable_name= 'chat_history'),
    ('human' , '{query}')
    ])

# Load Chat history 
chat_history = []
with open ('chat_history.txt') as f: 
    chat_history.extend(f.readline())

# Create prompt
prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'Where is my refund' })

print(prompt)