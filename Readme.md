# 🖥️ W2 Core

**W2 Core** é um sistema de produtividade e automação para Linux, pensado para centralizar suas atividades do dia em uma interface simples e moderna.

Ao iniciar, ele abre uma janela gráfica perguntando qual **modo do dia** você quer executar: **Trabalho**, **Estudo** ou **Pessoal**, e executa ações automáticas de acordo com a escolha.

---

## ✨ O que o W2 Core faz

- Abre uma **janela gráfica limpa** ao iniciar, sem bordas e sem botões de fechar/minimizar.
- Permite selecionar o **modo do dia**: Trabalho, Estudo ou Pessoal.
- Executa scripts externos ou comandos específicos para cada modo:
  - **Trabalho**: executa `/core/trabalho.py` e depois `run-studioalpha`.
  - **Estudo**: executa `/core/estudo.py` (personalizável).
  - **Pessoal**: executa `/core/pessoal.py` (personalizável).
- Mantém a interface minimalista e moderna.
- Pode ser configurado para iniciar automaticamente junto com o sistema.
- Funciona em **Linux** com **Python 3.8+**.

---

## 🧠 Modos disponíveis

Os modos do W2 Core são pré-definidos e cada um pode executar scripts diferentes:

| Modo     | Ação                                                                 |
|----------|----------------------------------------------------------------------|
| Trabalho | Executa o script `/core/trabalho.py` e roda `run-studioalpha`       |
| Estudo   | Executa o script `/core/estudo.py`                                  |
| Pessoal  | Executa o script `/core/pessoal.py`                                 |

> Observação: Você pode personalizar os scripts dentro da pasta `/core` para alterar o que cada modo faz.

---

## 🗂️ Estrutura de diretórios

```
~/.local/w2core/
├── core/
│   ├── trabalho.py
│   ├── estudo.py
│   └── pessoal.py
├── ui/
│   └── window.py
├── assets/
│   └── logo.py
├── main.py
└── README.md
```

- **core/** → scripts de cada modo.
- **ui/** → interface gráfica do W2 Core.
- **assets/** → recursos gráficos, como o logo.
- **main.py** → ponto de entrada do W2 Core.

---

## 📦 Instalação

1️⃣ **Pré-requisitos**

- Linux  
- Python 3.8 ou superior  

Verifique o Python:

```bash
python3 --version
```

- Tkinter (normalmente já vem instalado)  

```bash
# Debian / Ubuntu
sudo apt install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Arch Linux
sudo pacman -S tk
```

2️⃣ **Clonar o repositório**

```bash
git clone https://github.com/seu-usuario/w2core.git ~/.local/w2core
cd ~/.local/w2core
```

---

## ▶️ Uso

### Execução manual

Para iniciar o W2 Core manualmente:

```bash
python3 main.py
```

A janela vai abrir e você poderá selecionar o modo do dia.

### Execução automática ao ligar o PC

Para que o W2 Core abra automaticamente na inicialização:

1. Crie um arquivo `.desktop` na pasta `~/.config/autostart/`:

```bash
nano ~/.config/autostart/w2core.desktop
```

2. Cole o conteúdo:

```ini
[Desktop Entry]
Type=Application
Name=W2 Core
Exec=python3 /home/username-pc/.local/w2core/main.py
Icon=
Comment=Inicia o W2 Core automaticamente
X-GNOME-Autostart-enabled=true
Terminal=false
```

3. Salve e saia (`Ctrl+O`, `Ctrl+X`).  
4. Garanta permissão de execução (opcional):

```bash
chmod +x ~/.config/autostart/w2core.desktop
```

Agora o W2 Core abrirá automaticamente toda vez que você iniciar a sessão do Linux.

---

## 🛠️ Personalização

Você pode:

- Alterar os scripts de cada modo dentro da pasta `/core`.
- Ajustar o layout e estilo da janela em `ui/window.py`.
- Adicionar novos modos ou comandos conforme desejar.

---

## 🧘 Filosofia

O W2 Core não força produtividade. Ele apenas centraliza e automatiza suas ações do dia, permitindo que