import subprocess
import time
import sys
import os

def run():
    print("Modo TRABALHO iniciado")

    # Caminho para o sopro
    sopro_path = os.path.expanduser("~/.local/bin/sopro")

    try:
        # Abre o sopro
        subprocess.Popen([sopro_path])
        print("Sopro aberto")
    except FileNotFoundError:
        print("Erro: comando 'sopro' não encontrado")
        return

    # Aguarda 5 segundos
    print("Aguardando 5 segundos...")
    time.sleep(5)

    # Executa o comando final
    try:
        subprocess.Popen(["run-studioalpha"])
        print("run-studioalpha executado")
    except FileNotFoundError:
        print("Erro: comando 'run-studioalpha' não encontrado")
