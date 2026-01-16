import subprocess
import time
import os

def run_trabalho():
    print("Modo TRABALHO iniciado")

    # Abre o Sopro
    subprocess.Popen(["python3", os.path.expanduser("~/.local/sopro/app/main.py")])
    print("Sopro aberto")

    # Aguarda 5 segundos
    time.sleep(6)

    # Executa run-studioalpha como se fosse no terminal
    subprocess.run("run-studioalpha", shell=True, executable="/bin/bash")
    print("run-studioalpha executado")

if __name__ == "__main__":
    run_trabalho()
