from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client = MultiServerMCPClient(
        {"math":{
            "command":"python",
            "args":["Mathserver.py"],
            "transport":"stdio"
        },"weather":{
            "url":"http://localhost:8000/mcp",
            "transport":"streamable-http"
        }}
    )
    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools=await client.get_tools()
    model=ChatGroq(model="qwen/qwen3-32b")

    agent=create_agent(model,tools)

 #   math_response=await agent.ainvoke(
 #       {"messages":[{"role":"user","content":"What is (10 + 20)/2?"}]})
#
 #   print("Maths response:",math_response['messages'][-1].content)
 #   print(math_response)

    weather_response=await agent.ainvoke(
        {"messages":[{"role":"user","content":"What is temperature in Rocky hill CT 06067 ?"}]})

    print("Weather response:",weather_response['messages'][-1].content)
    print(weather_response)


asyncio.run(main())