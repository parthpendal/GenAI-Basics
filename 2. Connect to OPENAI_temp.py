import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

respose=client.chat.completions.create(
    model='gpt-4.1-nano',
    messages=[
        {"role":"system","content":"You are a helpful assistant."},
        {"role":"user","content":"Hello, tell a new joke."}
    ],response_format={"type":"text"},temperature=1,top_p=1,
     max_completion_tokens=256)

print(respose)
print(respose.choices[0].message.content)