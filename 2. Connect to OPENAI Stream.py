import os
from openai import OpenAI

# Initialize client (reads API key from env)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4.1-nano",  # pick available model
    messages=[
        {"role": "system", "content": "You are a helpful financial assistant who can guide based on stock analysts reviews"},
        {"role": "user", "content": "Provide me summary of various analysts report in last 30 days for Tesla stock."}
    ],
    max_tokens=600,
    stream=True
)


for chunk in response:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="", flush=True)