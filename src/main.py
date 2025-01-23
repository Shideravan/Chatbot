from apikey import API_KEY
from dados import encomendas, boletos, promocoes, protocolo
import requests
import json

class ChatBot:
    def __init__(self):
        self.headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
        self.link = "https://api.openai.com/v1/chat/completions"
        self.id_modelo = "gpt-3.5-turbo"
        self.conversation = []
        self.menu = {
            "protocolo": protocolo,
            "encomendas": encomendas,
            "boletos": boletos,
            "promocoes": promocoes
        }


    def mostrar_menu(self):
        print("\nATENDIMENTO EMPRESA X\n")
        print("Você pode a qualquer momento escolher uma das opções:")
        print("[protocolo] Fornece a qualquer momento o protocolo de atendimento atual")
        print("[encomendas] Dúvidas a respeito de encomendas")
        print("[boletos] Dúvidas a respeito de cobrança de boletos")
        print("[promocoes] Promoções disponíveis")
        print("[sair] Encerrar o chat\n")

    def receber_input_usuario(self):
        input_usuario = input("Usuário: ")
        return input_usuario

    def gerar_resposta(self, input_usuario):
        if input_usuario in self.menu:
            return self.menu[input_usuario]
        elif "IA" in input_usuario:
            return "Sim, eu sou uma IA e é um prazer ajudar você. Gostaria de falar com um atendente humano? Siga esse link: www.atendentehumano.com"
        else:
            self.conversation.append({"role": "user", "content": input_usuario})

            body_mensagem = {
                "model": self.id_modelo,
                "messages": self.conversation
            }

            body_mensagem = json.dumps(body_mensagem)

            requisicao = requests.post(self.link, headers=self.headers, data=body_mensagem)
            resposta = requisicao.json()
            mensagem = resposta["choices"][0]["message"]["content"]

            self.conversation.append({"role": "assistant", "content": mensagem})

            return mensagem

    def chat(self):
        self.mostrar_menu()
        while True:
            input_usuario = self.receber_input_usuario()
            if input_usuario.lower() == "sair":
                print(f"ChatBot: Obrigado por utilizar nosso atendimento. Seu número de protocolo é: {protocolo}. Conte sempre com a gente!")
                break
            response = self.gerar_resposta(input_usuario)
            print(f"ChatBot: {response}")

if __name__ == "__main__":
    bot = ChatBot()
    bot.chat()
