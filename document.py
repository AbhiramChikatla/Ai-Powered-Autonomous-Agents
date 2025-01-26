import sys
from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv()

from browser_use.agent.views import ActionResult

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI

from pydantic import SecretStr

from langchain_openai import ChatOpenAI

from browser_use import Agent, Controller
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext


browser = Browser(
	config=BrowserConfig(
		# NOTE: you need to close your chrome browser - so that this can open your browser in debug mode
		chrome_instance_path='C:\Program Files\Google\Chrome\Application\chrome.exe',
	)
)


async def main():
	agent = Agent(
		task='In docs.google.com Write a letter in Google Docs to my Papa, thanking him for everything,rename the file as letter_to_papa and save the document in the  (PDF)format and download the file. Note: if you dont know the next step ask me for help',
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv("GEMINI_API_KEY"))),
		browser=browser,
	)

	await agent.run()
	await browser.close()

	input('Press Enter to close...')


if __name__ == '__main__':
	asyncio.run(main())