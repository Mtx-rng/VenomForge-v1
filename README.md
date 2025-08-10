```markdown
# 🔥 Venom Forge - Advanced Android Payload Generator

![Banner](https://img.shields.io/badge/Version-1.0-blue) 
![Platform](https://img.shields.io/badge/Platform-Termux-green)
![License](https://img.shields.io/badge/License-MIT-orange)

Venom Forge é uma solução completa para pentesting em dispositivos móveis, oferecendo automação avançada para criação de payloads Android diretamente no Termux.

## 🌟 Recursos Premium

- 🚀 **Instalação 1-Click** do Metasploit Framework
- 🛠️ **Geração de Payloads** APK altamente configuráveis:
  - Meterpreter Reverse TCP
  - Bind Shell
  - Persistência automática
- 🔄 **Tunelamento Integrado** (Ngrok/Localhost)
- 🎨 **Interface Moderna** com:
  - Menus interativos
  - Visualização em tempo real
  - Códigos de cores intuitivos
- 📊 **Gerenciamento de Sessões** avançado

## 🖥️ Demonstração
```
[+] Configurando LHOST: 192.168.1.105
[+] Configurando LPORT: 4444
[+] Construindo payload evasivo...
[✔] Payload gerado: venom_payload.apk (3.2MB)
```

## 🛠️ Instalação Rápida

```bash
# Clone o repositório
git clone https://github.com/Mtx-rng/VenomForge-v1.git

# Acesse o diretório
cd VenomForge-v1

# Execute o instalador
python3 venomforge.py --install
```

## 📌 Guia de Uso

1. **Configuração Inicial**:
   ```bash
   python3 venomforge.py --setup
   ```

2. **Geração de Payload**:
   ```bash
   python3 venomforge.py --generate
   ```

3. **Opções Avançadas**:
   ```bash
   python3 venomforge.py --advanced
   ```

## 🧩 Requisitos do Sistema

| Componente | Versão Mínima |
|------------|---------------|
| Termux     | 0.118+        |
| Python     | 3.9+          |
| Storage    | 500MB livres  |
| RAM        | 2GB+          |

## ⚠️ Aviso Legal
Este projeto destina-se **exclusivamente** para:
- Testes de penetração autorizados
- Pesquisa em segurança cibernética
- Educação em defesa digital

**O uso indevido é estritamente proibido.**

## 🤝 Contribuição
Contribuições são bem-vindas! Siga nosso guia:
1. Fork o repositório
2. Crie sua branch (`git checkout -b feature/incrivel`)
3. Commit suas mudanças (`git commit -am 'Add incrível feature'`)
4. Push para a branch (`git push origin feature/incrivel`)
5. Abra um Pull Request

## 📌 Roadmap 2024
- [X] Suporte a múltiplos payloads
- [ ] Integração com Cloudflare Tunnels
- [ ] Builder Web embutido
- [ ] Modo Stealth avançado

## 📜 Licença
Distribuído sob licença MIT. Veja `LICENSE` para mais informações.

---
Desenvolvido com ❤️ por [Therac-25](https://github.com/Mtx-rng) | Mantido pela comunidade de segurança
```