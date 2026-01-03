import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

respose=client.chat.completions.create(
    model="gpt-4.1-nano",
    messages=[
        {"role": "user", "content": "Tell me a joke"}
    ],response_format={"type":"text"},
    temperature=0.8,
    top_p=1,
    max_completion_tokens=256,
)

print(respose)
print(respose.choices[0].message.content)