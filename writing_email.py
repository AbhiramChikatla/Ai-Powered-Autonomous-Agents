import os
import sys
from pathlib import Path

from browser_use.agent.views import ActionResult

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI

from pydantic import SecretStr
from dotenv import load_dotenv
load_dotenv()

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
		task='In gmail.google.com write or send a mail to the recipient with gmail lookingprofessional9@gmail.com with the subject "Thank you" and the body "Thank you for everything" and finally send the email. and mark the mail as starred Note: if you dont know the next step ask me for help after you clicked compose a gmail a small window will pop up and you can start typing the email in that window',
    llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv("GEMINI_API_KEY"))),
		browser=browser,
	)

	await agent.run()
	await browser.close()

	input('Press Enter to close...')


if __name__ == '__main__':
	asyncio.run(main())