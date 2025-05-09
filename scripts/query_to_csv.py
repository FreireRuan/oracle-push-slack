import os
import csv
import oracledb
from dotenv import load_dotenv
from datetime import date

# Carrega variáveis de ambiente do .env
load_dotenv(dotenv_path="credencial.env")

# inicializa Oracle Instant Client=
oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient_23_8")

# query
SQL_QUERY = """
select * from seu_bd.sua_table
"""

# data de hoje
hoje = date.today().strftime("%Y-%m-%d")

# saída do arquivo
OUTPUT_PATH = f"agendamentos_{hoje}.csv"

def fetch_to_csv(query: str, output_path: str):
    user     = os.getenv("ORACLE_USER")
    password = os.getenv("ORACLE_PASS")
    host     = os.getenv("ORACLE_HOST")
    port     = os.getenv("ORACLE_PORT", "1521")
    service  = os.getenv("ORACLE_SERVICE")

    dsn = oracledb.makedsn(host, port, service_name=service)
    conn = oracledb.connect(user=user, password=password, dsn=dsn)

    count = 0
    with conn.cursor() as cur, open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        cur.execute(query)
        # Cabeçalho
        cols = [col[0] for col in cur.description]
        writer.writerow(cols)
        # Linhas
        for row in cur:
            writer.writerow(row)
            count += 1

    conn.close()
    print(f"[OK] {count} registros exportados em {output_path}")

if __name__ == "__main__":
    # execução da query
    fetch_to_csv(SQL_QUERY, OUTPUT_PATH)
