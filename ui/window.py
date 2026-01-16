import tkinter as tk
from assets.logo import draw_logo

class W2CoreWindow:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("W2 Core")
        self.root.geometry("340x380")
        self.root.resizable(False, False)
        self.root.configure(bg="#f4f4f4")

        self.selected_mode = None

        self.build_ui()

    def build_ui(self):
        # Logo
        canvas = tk.Canvas(
            self.root,
            width=160,
            height=90,
            bg="#f4f4f4",
            highlightthickness=0
        )
        canvas.pack(pady=12)
        draw_logo(canvas)

        # Texto
        title = tk.Label(
            self.root,
            text="Olá Lucas, o que você vai fazer agora?",
            bg="#f4f4f4",
            fg="#111",
            font=("Arial", 11, "bold")
        )
        title.pack(pady=12)

        # Botões
        self.create_button("💼 Trabalho", self.action_trabalho)
        self.create_button("🧠 Estudo", self.action_estudo)
        self.create_button("🌱 Pessoal", self.action_pessoal)

    def create_button(self, text, command):
        btn = tk.Button(
            self.root,
            text=text,
            command=command,
            width=26,
            height=2,
            bg="#ffffff",
            fg="#111",
            relief="solid",
            borderwidth=1,
            font=("Arial", 10)
        )
        btn.pack(pady=6)

    def action_trabalho(self):
      self.selected_mode = "trabalho"
      self.root.destroy()

    def action_estudo(self):
      self.selected_mode = "estudo"
      self.root.destroy()

    def action_pessoal(self):
      self.selected_mode = "pessoal"
      self.root.destroy()

    def run(self):
        self.root.mainloop()
