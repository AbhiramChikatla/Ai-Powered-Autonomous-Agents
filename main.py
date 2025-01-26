from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from pydantic import SecretStr
from dotenv import load_dotenv
import os
load_dotenv()
import asyncio

# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv("GEMINI_API_KEY")))

# Create agent with the model
async def main():
    agent = Agent(
        task="Write a letter in Google Docs to my Papa, thanking him for everything, and save the document as a PDF.",
        llm=llm
    )
    result=await agent.run()   
    print(result)
asyncio.run(main())
