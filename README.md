# Venom Forge

**Venom Forge** é um script automatizado para Termux que facilita a instalação do framework Metasploit e a geração de payloads Android (APK) utilizando o `msfvenom`.

## Funcionalidades

- Instalação automática do Metasploit no Termux, configurando o ambiente para uso imediato;
- Geração automatizada de payloads Android com parâmetros personalizados (`LHOST` e `LPORT`);
- Criação de arquivos `.apk` prontos para testes de invasão com payloads Meterpreter reverse TCP;
- Interface amigável com banners ASCII coloridos para melhor experiência visual;
- Opção para iniciar o console do Metasploit (`msfconsole`) diretamente após a instalação;
- Ideal para pentesters e entusiastas de segurança que atuam em ambientes Android.

## Como usar

1. Baixe e execute o script para instalar o Metasploit.
2. Configure o `LHOST` (IP local ou público) e `LPORT` (porta de escuta).
3. Gere seu payload `.apk` pronto para uso em testes.
4. Utilize o `msfconsole` para iniciar o listener e controlar as sessões.

## Requisitos

- Termux atualizado no Android;
- Conexão estável com a internet para download do Metasploit;
- Permissões necessárias para execução do script.

---

> ⚠️ **Aviso Legal:** Utilize esta ferramenta apenas para fins legais e autorizados, como testes de penetração em sistemas que você possui ou tem permissão expressa para testar.

---

Qualquer dúvida ou contribuição, abra uma issue ou faça um pull request!

---

*Desenvolvido por Therac-25*
