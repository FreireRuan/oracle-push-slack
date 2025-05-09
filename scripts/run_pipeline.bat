@echo off
REM 1) Vai para a pasta do projeto
cd /d "C:\Users\ruan.morais\Desktop\sandbox_freire\business-analytics\projects\amei-agendamentos-push-slack"

REM 2) Ativa a venv
call ".\.venv\Scripts\activate.bat"

REM 3) Vai para a pasta dos scripts
cd /d "%CD%\scripts"

REM 3) Conecta na VPN
start "" /B python connect_vpn.py

REM 4) Aguarda alguns segundos para garantir que a VPN subiu
timeout /t 10 /nobreak > nul

REM 5) Executa a query e salva o CSV
python query_to_csv.py

REM 6) Executa o script para enviar os dados para o Google Drive
python upload_to_google_drive.py

REM 7) Envia para o Slack
python send_to_slack.py

REM 8) Fechar a VPN após tudo
taskkill /IM openvpn.exe /F

exit /B 0