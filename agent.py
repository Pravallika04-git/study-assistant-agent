import os
from groq import Groq

# Paste your API key here
API_KEY = "your-groq-api-key-here"

client = Groq(api_key=API_KEY)

conversation_history = []

def chat(user_message):
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": """You are a helpful Study Assistant Agent. 
                You help students by:
                1. Creating detailed step-by-step study plans for any topic
                2. Explaining concepts in simple easy to understand language
                3. Answering follow-up questions
                4. Giving tips to remember things better
                Always be encouraging and supportive."""
            }
        ] + conversation_history
    )
    
    assistant_message = response.choices[0].message.content
    conversation_history.append({
        "role": "assistant", 
        "content": assistant_message
    })
    
    return assistant_message

print("=== Study Assistant Agent ===")
print("Type 'quit' to exit\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    print("\nAgent:", chat(user_input))
    print()
