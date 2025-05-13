 # AMEI-AGENDAMENTOS-PUSH-SLACK

## 🎯 Objetivos

Automatizar a coleta de dados de agendamentos do sistema (via banco Oracle acessado por VPN) e enviá-los periodicamente para um canal do Slack, em formato CSV, para facilitar o acompanhamento e simular os pacientes conforme a rotina operacional.

---

## Automatiza o fluxo de:

1. Conectar via VPN a um Oracle Database  
2. Executar uma query e exportar resultado em CSV  
3. Enviar o CSV para o Slack
4. Encerrar a VPN ao final

Tudo isso pode ser agendado no Windows Task Scheduler usando o script `run_pipeline.bat`.

---

## 📋 Pré-requisitos
 
- Python 3.10+ instalado  
- OpenVPN instalado e configurado  
- Conta e workspace no Slack com permissão para criar Apps  
- Git Bash ou PowerShell para testes manuais

---

## 🧩 Estrutura do Projeto
```
amei-agendamentos-push-slack/
├── scripts/
│ ├── connect_vpn.py # Conecta à VPN
│ ├── extract_query.py # Executa a query Oracle e gera o CSV
│ ├── push_to_slack.py # Envia o evento para o Slack
│ └── main.py # Orquestra os scripts
├── .venv # Variáveis (não versionado)
├── requirements.txt # Dependências do projeto
└── README.md # Documentação
```
---

## ⚙️ Requisitos
Arquivo de variáveis (".env" ou "credencial.env")
Na raiz do projeto, crie um arquivo chamado credencial.env com as seguintes chaves:

---

## 🚀 Como usar
```
# Oracle Database
ORACLE_USER=seu_usuario
ORACLE_PASS=sua_senha
ORACLE_HOST=seu_host
ORACLE_PORT=sua_porta
ORACLE_SERVICE=nome_do_servico

# Slack
SLACK_TOKEN=xoxb-XXXXXXXXXXXXXXXX
SLACK_CHANNEL=id_canal
```

---

## 🧙 Autor

Feito com café ☕, Python 🐍 e umas ideias insanas 🛠️ por **Ruan Freire**  
🔗 [LinkedIn](https://www.linkedin.com/in/ruanfreire) • [GitHub](https://github.com/FreireRuan)
