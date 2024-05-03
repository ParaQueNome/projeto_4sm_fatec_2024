from openai import OpenAI
import os
from dotenv import load_dotenv

class OpenAiClient:
    def __init__(self):
        load_dotenv()
        self.openai = OpenAI(api_key= os.getenv("API_KEY"))

    def userFinances(self, renda, **despesa):
        messages =  [
            {'role':'system', 'content': 'Você é um assistente Financeiro que dá dicas de economia e gerenciamento de renda com base no valor da renda e dos gastos do usuário'},
            {'role': 'user', 'content': f'A renda é de R${renda} e os gastos são: {despesa}'}
        ]
        answer = self.openai.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages= messages,
            max_tokens= 400,
            temperature = 0.6
        )
        messages.append({'role': 'assistant', 'content': answer.choices[0].message.content})
        return answer.choices[0].message.content
    
