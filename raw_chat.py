# Using Chat model for the convo

import os
from dotenv import load_dotenv
from groq import Groq
from langchain_groq import ChatGroq
load_dotenv() 

client = Groq(api_key=os.getenv("GROQ_API_KEY")
              )

conversation=client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role":"system",
            "content":"Your'e a helpful assistant."
        },
        {
            "role":"user",
            "content":"What is the capital of france?"
        }
    ],
    
)
print(conversation.choices[0].message.content)