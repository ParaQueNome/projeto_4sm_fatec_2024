from openai import OpenAI
import os
from dotenv import load_dotenv

class OpenAiClient:
    def __init__(self):
        load_dotenv()
        #self.openai = OpenAI(api_key= os.getenv("OPENAI_API_KEY"))
        self.openai = OpenAI(api_key= "sk-proj-KZczWi9H11DxXYqOUOXHT3BlbkFJL1eP8yhZdpvOgAtjjFsx")

    def userFinances(self, renda,user, **despesa):
        messages =  [
            {'role':'system', 'content': 'Você é um assistente Financeiro que dá dicas de economia e gerenciamento de renda com base no valor da receita e dos gastos do usuário. Pode utilizar o historico anterior como base para nova análise. Você está trabalhando em uma plataforma de DRE pessoal para gastos e o usuario já possui uma planilha de controle. Você pode dar respostas mais assertivas sobre como gastar o dinheiro restante. VOCE DEVE SER IGUAL UM HUMANO, UTILIZANDO LINGUAGEM MAIS INFORMAL E DEVE USAR EMOJIS e SEJA MAIS INFORMAL POSSIVEL PARA PASSAR EMPATIA, para que o usuario se sinta confortavel. Você receberá o nome do usuario'},
            {'role': 'user', 'content': f'A renda é de R${renda} e os gastos são: {despesa} e o usuario é {user}'}
        ]
        answer = self.openai.chat.completions.create(
            model = "gpt-4",
            messages= messages,
            max_tokens= 400,
            temperature = 0.6
        )
        messages.append({'role': 'assistant', 'content': answer.choices[0].message.content})
        return answer.choices[0].message.content
    