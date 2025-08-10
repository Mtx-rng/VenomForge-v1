#!/usr/bin/env python3
# VenomForge 2.0 - Modern Metasploit Payload Generator
# Author: Therac-25 
# GitHub: https://github.com/Mtx-rng

import os
import sys
import random
from time import sleep
from prettytable import PrettyTable

# Cores melhoradas
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

# Arte ASCII personalizada
def show_banner():
    print(f"""{colors.PURPLE}
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
{colors.RESET}""")
    print(f"{colors.YELLOW}          VenomForge 2.0 - Advanced Payload Generator{colors.RESET}")
    print(f"{colors.BLUE}          ---------------------------------------{colors.RESET}\n")

# Menu principal modernizado
def main_menu():
    while True:
        show_banner()
        print(f"""{colors.ORANGE}
[1] {colors.GREEN}Generate Payload{colors.ORANGE}
[2] {colors.GREEN}Start Listener{colors.ORANGE}
[3] {colors.GREEN}Payload Utilities{colors.ORANGE}
[4] {colors.GREEN}Session Management{colors.ORANGE}
[5] {colors.RED}Exit{colors.RESET}""")
        
        try:
            choice = int(input(f"\n{colors.BLUE}Select an option: {colors.RESET}"))
            if choice == 1:
                payload_menu()
            elif choice == 2:
                listener_menu()
            elif choice == 3:
                utilities_menu()
            elif choice == 4:
                session_menu()
            elif choice == 5:
                print(f"\n{colors.YELLOW}Goodbye! Happy hacking!{colors.RESET}\n")
                sys.exit(0)
            else:
                print(f"{colors.RED}\nInvalid option! Please try again.{colors.RESET}")
                sleep(1)
        except ValueError:
            print(f"{colors.RED}\nPlease enter a valid number!{colors.RESET}")
            sleep(1)

# Menu de payloads com animação
def payload_menu():
    os.system('clear')
    show_banner()
    print(f"{colors.PURPLE}\n>>> PAYLOAD GENERATION MENU <<<{colors.RESET}")
    
    targets = {
        1: "Windows",
        2: "Linux",
        3: "Android",
        4: "MacOS",
        5: "iOS",
        99: "Back to Main Menu"
    }
    
    # Mostrar opções com cores
    for key, value in targets.items():
        if key == 99:
            print(f"{colors.RED}[{key}] {value}{colors.RESET}")
        else:
            print(f"{colors.GREEN}[{key}] {colors.BLUE}{value}{colors.RESET}")
    
    try:
        target = int(input(f"\n{colors.YELLOW}Select target OS: {colors.RESET}"))
        if target in targets:
            if target == 99:
                return
            else:
                generate_payload(targets[target])
        else:
            print(f"{colors.RED}Invalid option!{colors.RESET}")
            sleep(1)
            payload_menu()
    except ValueError:
        print(f"{colors.RED}Please enter a number!{colors.RESET}")
        sleep(1)
        payload_menu()

# Função para mostrar endereços de rede
def show_network_interfaces():
    table = PrettyTable()
    table.field_names = [f"{colors.GREEN}Interface{colors.RESET}", 
                         f"{colors.BLUE}IP Address{colors.RESET}", 
                         f"{colors.PURPLE}Status{colors.RESET}"]
    
    # Simulação - na implementação real usar os.popen ou netifaces
    table.add_row(["eth0", "192.168.1.100", "Up"])
    table.add_row(["wlan0", "10.0.0.15", "Up"])
    table.add_row(["tun0", "172.16.0.1", "Up"])
    
    print(f"\n{colors.YELLOW}Available Network Interfaces:{colors.RESET}")
    print(table)

# Efeito de digitação (opcional)
def type_effect(text, color=colors.WHITE, delay=0.05):
    for char in text:
        print(color + char, end='', flush=True)
        sleep(delay)
    print(colors.RESET)

# Verificação de dependências
def check_dependencies():
    required = ['msfvenom', 'msfconsole', 'nmap']
    missing = []
    
    for tool in required:
        if not os.popen(f"which {tool}").read():
            missing.append(tool)
    
    if missing:
        print(f"{colors.RED}Missing dependencies:{colors.RESET}")
        for tool in missing:
            print(f"- {tool}")
        return False
    return True

# Inicialização
if __name__ == "__main__":
    try:
        if not check_dependencies():
            print(f"\n{colors.RED}Some required tools are missing. Please install them first.{colors.RESET}")
            sys.exit(1)
        
        # Limpar tela e iniciar
        os.system('clear')
        type_effect("Initializing Paybag 2.0...", colors.PURPLE)
        sleep(1)
        main_menu()
        
    except KeyboardInterrupt:
        print(f"\n{colors.RED}Interrupted by user. Exiting...{colors.RESET}")
        sys.exit(0)