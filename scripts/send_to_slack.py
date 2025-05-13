import slack_sdk
from slack_sdk.errors import SlackApiError
import os
from dotenv import load_dotenv
from datetime import date

load_dotenv(dotenv_path="credencial.env")

SLACK_TOKEN = os.getenv("SLACK_TOKEN")
SLACK_CHANNEL = os.getenv("SLACK_CHANNEL")

client = slack_sdk.WebClient(SLACK_TOKEN)

# data de hoje
hoje = date.today().strftime("%Y-%m-%d")

# saída do arquivo
file_path = f"agendamentos_{hoje}.csv"

try:

    response = client.files_upload_v2(
        file=file_path,
        title="Arquivo csv",
        channel=SLACK_CHANNEL,
        initial_comment="Arquivo com os agendamentos no dia de hoje",
    )

# TRATAMENTO DE EXCECAO
except Exception as e:
    print(f"Error: {e}")
