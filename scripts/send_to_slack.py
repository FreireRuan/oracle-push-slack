from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="credencial.env")

SLACK_TOKEN = os.getenv("SLACK_TOKEN")
SLACK_CHANNEL = os.getenv("SLACK_CHANNEL")

mensagem = """
Arquivo enviado com sucesso para o Google Drive!
Acesse o link para visualizar: https://drive.google.com/drive/folders/1UXUP3M_6Ik0zV__80Yx6HsfGrK1Uhiwv?usp=sharing
"""

def send_message():
    client = WebClient(token=SLACK_TOKEN)
    try:
        response = client.chat_postMessage(
            channel=SLACK_CHANNEL,
            text=mensagem
        )
        print("✅ Mensagem enviada com sucesso.")
    except SlackApiError as e:
        print(f"❌ Erro ao enviar mensagem: {e.response['error']}")

if __name__ == "__main__":
    send_message()