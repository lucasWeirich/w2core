import subprocess
import os
import subprocess
from ui.window import W2CoreWindow

app = W2CoreWindow()
app.run()

mode = app.selected_mode

if mode == "trabalho":
    print("Executando modo trabalho")
    subprocess.Popen(
        ["python3", os.path.expanduser("~/.local/w2core/core/trabalho.py")]
    )

elif mode == "estudo":
    print("Executando modo estudo")
    # chama core.estudo.start()

elif mode == "pessoal":
    print("Executando modo pessoal")
    # chama core.pessoal.start()