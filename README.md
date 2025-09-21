VenomForge-v1

**VenomForge-v1** é uma poderosa ferramenta em **Python** desenvolvida para **pesquisadores de segurança**, utilizando **msfvenom** e **nmap**.  
Este guia explica como configurar e executar o VenomForge-v1 no **Termux (Android)** e como resolver erros comuns.


## Índice
1. [Pré-requisitos](#pré-requisitos)
2. [Instalação](#instalação)
3. [Executando a Ferramenta](#executando-a-ferramenta)
4. [Resolução de Erros Comuns](#resolução-de-erros-comuns)
5. [Uso Ético](#uso-ético)
6. [Suporte](#suporte)



## Pré-requisitos
Para rodar o **VenomForge-v1**, você precisa ter no Termux:
- **Python** – executa o script principal.
- **msfvenom** – gera payloads (Metasploit Framework).
- **nmap** – varredura de rede.
- **which** – verifica programas instalados.


## Instalação

### 1. Atualizar Termux
```bash
pkg update && pkg upgrade
```
### 2. Instalar dependências
```
pkg install python
pkg install which
pkg install nmap
pkg install wget curl
pip install prettytable
```

3. Instalar Metasploit (inclui msfvenom)
```bash
curl -LO https://github.com/rapid7/metasploit-framework/raw/master/scripts/termux/install.sh
chmod +x install.sh
./install.sh
```
### Verificar:
```
msfvenom --version

Saída esperada: Framework Version: 6.x.x
```
4. Conceder permissão de armazenamento
```
termux-setup-storage
```



## Executando a Ferramenta
```
cd ~/VenomForge-v1
python VenomForge.py
```
### Se der erro de permissão:
```
chmod +x VenomForge.py
```



## Resolução de Erros Comuns
```
Erro: which: not found

pkg install which

Erro: Dependências ausentes: msfvenom, nmap

which nmap
which msfvenom
```
Se o msfvenom não aparecer:
```
export PATH=$PATH:$HOME/metasploit-framework
echo 'export PATH=$PATH:$HOME/metasploit-framework' >> ~/.bashrc
source ~/.bashrc

Erro: msfvenom: version unknown

pkg install ruby
ruby --version
pkg uninstall metasploit-framework
rm -rf $HOME/metasploit-framework
curl -LO https://github.com/rapid7/metasploit-framework/raw/master/scripts/termux/install.sh
chmod +x install.sh
./install.sh


```
## Uso Ético
```
> ATENÇÃO: O VenomForge-v1 deve ser usado apenas para testes de segurança autorizados.
O uso indevido pode violar leis e princípios éticos.




```
## Suporte
```
📌 Repositório Oficial: https://github.com/Mtx-rng/VenomForge-v1
Abra uma issue no GitHub informando:

Mensagem de erro completa

Saída dos comandos executados

Sistema e versão do Termux
```



Créditos
```
Desenvolvido por Mtx-rng
Feito para pesquisa e estudo de segurança cibernética.

