from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from datetime import date

# Configurações
SERVICE_ACCOUNT_FILE = 'service_account.json'
SCOPES = ['https://www.googleapis.com/auth/drive']
FOLDER_ID = '1UXUP3M_6Ik0zV__80Yx6HsfGrK1Uhiwv'

# data de hoje
hoje = date.today().strftime("%Y-%m-%d")

# saída do arquivo
FILE_PATH = f"agendamentos_{hoje}.csv"

# FILE_PATH = 'resultado.csv'

# Autenticação
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

drive_service = build('drive', 'v3', credentials=credentials)

# Upload do arquivo
file_metadata = {
    'name': FILE_PATH,
    'parents': [FOLDER_ID]
}
media = MediaFileUpload(FILE_PATH, mimetype='text/csv')

file = drive_service.files().create(
    body=file_metadata,
    media_body=media,
    fields='id'
).execute()

print(f"✅ Arquivo enviado! ID do arquivo: {file.get('id')}")

# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive

# # ============================
# # 🔐 Autenticação
# # ============================
# gauth = GoogleAuth()
# gauth.LocalWebserverAuth()  # Abre navegador para autenticação

# drive = GoogleDrive(gauth)

# # ============================
# # 📁 Envio de Arquivo
# # ============================

# file_path = "resultado.csv"  # Nome do arquivo local
# folder_id = "1UXUP3M_6Ik0zV__80Yx6HsfGrK1Uhiwv"  # ID da pasta compartilhada

# file_to_upload = drive.CreateFile({
#     "title": file_path,
#     "parents": [{"id": folder_id}]
# })

# file_to_upload.SetContentFile(file_path)
# file_to_upload.Upload()

# print("✅ Arquivo enviado para o Google Drive com sucesso.")