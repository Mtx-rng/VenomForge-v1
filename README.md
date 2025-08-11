# VenomForge 2.0

VenomForge é um gerador moderno e interativo de payloads para Metasploit, desenvolvido para facilitar a criação rápida de arquivos maliciosos para pentest e testes de segurança. Com interface colorida, menus intuitivos e suporte a múltiplos sistemas operacionais, o VenomForge torna o processo de geração de payloads simples e eficiente.

## Características

- **Interface interativa e colorida no terminal**
- **Geração de payloads para Windows, Linux, Android, MacOS e iOS**
- **Validação automática de dependências**
- **Simulação de gerenciamento de sessões e utilitários**
- **Compatível com Termux, Linux e ambientes Unix-like**
- **Pronto para expansão de funcionalidades**

## Pré-requisitos

- **Python 3.x**
- **Metasploit Framework** (`msfvenom` e `msfconsole` disponíveis no PATH)
- **nmap** instalado
- **prettytable** (instale com `pip install prettytable`)

## Instalação

```bash
# Clone o repositório
git clone https://github.com/Mtx-rng/VenomForge-v1.git
cd VenomForge-v1

# Instale o prettytable
pip install prettytable

# No Termux ou Linux, instale o Metasploit e nmap:
pkg install unstable-repo
source <(curl -fsSL https://kutt.it/msf) instalador metasploit
pkg install nmap
```

## Uso

```bash
python VenomForge.py
```

Siga os menus interativos para gerar payloads.  
Ao escolher um alvo, insira o IP (`LHOST`) e a porta (`LPORT`) para o payload.  
O arquivo será salvo na pasta atual com o nome informado.

### Exemplos de geração de payload

- **Windows**: Gera um `.exe` Meterpreter Reverse TCP
- **Linux**: Gera um `.elf` Meterpreter Reverse TCP
- **Android**: Gera um `.apk` Meterpreter Reverse TCP
- **MacOS**: Gera um binário `.macho`
- **iOS**: Gera um binário `.bin` (experimenta, depende do suporte do msfvenom)

## Segurança

**ATENÇÃO:**  
Este projeto é exclusivamente para fins educacionais e de testes em ambientes autorizados.  
Não utilize o VenomForge para atividades ilegais ou sem permissão explícita dos donos dos sistemas alvo.

Nunca compartilhe ou publique arquivos gerados em ambientes públicos não controlados!

## Contribuição

Sinta-se à vontade para abrir issues, sugerir melhorias ou enviar pull requests!

## Licença

MIT

---

**Autor:** Therac-25  
**GitHub:** [Mtx-rng](https://github.com/Mtx-rng)