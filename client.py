from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
## For running asyncio
import asyncio

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

async def main(query: str):
    client = MultiServerMCPClient(
    {
        "weather": {
        "url": "http://127.0.0.1:8001/mcp",  # Replace with the remote server's URL
        "transport": "streamable_http"
    }
    }
    ) 
    tools = await client.get_tools()
    agent = create_react_agent(model, tools)
    response = await agent.ainvoke({"messages": query})
    return response
    

if __name__ == "__main__":
    response=asyncio.run(main("what is 4+4"))
    print('------------')
    print(response)

