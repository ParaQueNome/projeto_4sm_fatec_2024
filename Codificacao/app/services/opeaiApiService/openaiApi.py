from openai import OpenAI
import os
from dotenv import load_dotenv


class OpenAiClient:
    def __init__(self):
        load_dotenv()
        self.openai = OpenAI(api_key= os.getenv("OPENAI_API_KEY"))
        #self.openai = OpenAI(api_key= "sk-proj-8k1wdSxKS3DdhvhHqJtAT3BlbkFJaSMrm4k6m4dUs7d8FnM9")

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
    
    def userExchanges(self, renda, gastos,user, **exchanges):
        messages = [
            {'role': 'system', 'content': 'Você é um assistente Financeiro que vai analisar com base nos dados de receita, gastos e lucro/prejuizo do usuario se é valido ele investir em alguma ação na bolsa de valores. Para isso, receberá o resultado da previsao de preço de fechamento de uma rede neural de determinada ação, assim como o nome da empresa. Você DEVE ser o mais pessoal possível, imitando o comportamento de um humano, sem parecer que é uma máquina falando'},
            {'role': 'user', 'content': f'A renda é de R${renda} e os gastos são R$ {gastos}, usuario: {user}. As informacoes de nome da empresa e valor de fechamento : {exchanges}'}
        ]
        answer = self.openai.chat.completions.create(
            model = "gpt-4",
            messages= messages,
            max_tokens= 400,
            temperature = 0.6
        )
        messages.append({'role': 'assistant', 'content': answer.choices[0].message.content})
        return answer.choices[0].message.content
        
