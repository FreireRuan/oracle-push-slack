import subprocess
import signal

# caminhos dos aqrquivos das credenciais
OVPN_CONFIG = "credencial_vpn_amorsaude.ovpn"
AUTH_FILE   = "credencial_vpn_amorsaude.txt"

OPENVPN_EXE = r"C:\Program Files\OpenVPN\bin\openvpn.exe"

# função que inicia a VPN
def connect_vpn():
    cmd = [OPENVPN_EXE, "--config", OVPN_CONFIG]
    if AUTH_FILE:
        cmd += ["--auth-user-pass", AUTH_FILE]

    print(f"Iniciando VPN: {' '.join(cmd)}")
    proc = subprocess.Popen(cmd)
    return proc

# entrada
def main():
    vpn_proc = connect_vpn()
    try:
        vpn_proc.wait(timeout=180)  # espera no máximo 3 minutos
    except subprocess.TimeoutExpired:
        print("⚠️ Tempo limite atingido. Continuando com o pipeline…")
    except KeyboardInterrupt:
        print("Interrompendo VPN…")
        vpn_proc.send_signal(signal.SIGINT)
        vpn_proc.wait()

if __name__ == "__main__":
    main()


# entrada
# def main():
#     vpn_proc = connect_vpn()
#     try:
#         vpn_proc.wait()
#     except KeyboardInterrupt:
#         print("Interrompendo VPN…")
#         vpn_proc.send_signal(signal.SIGINT)
#         vpn_proc.wait()

# if __name__ == "__main__":
#     main()