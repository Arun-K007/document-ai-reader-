import ollama

# Get question from the user
question = input("Ask your question: ")

# Send question to local LLM
response = ollama.chat(
    model="gemma3",
    messages=[
        {
            "role": "user",
            "content": question
        }
    ]
)

# Display the response
print("\nAI Response:")
print(response["message"]["content"])