from openai import OpenAI
import os
from dotenv import load_dotenv

class OpenAiClient:
    def __init__(self):
        load_dotenv()
        self.openai = OpenAI(api_key= os.getenv("OPENAI_API_KEY"))

   def userFinances(self, **renda, **despesa):
        