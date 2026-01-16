import tkinter as tk

def draw_logo(canvas):
    canvas.create_text(
        80, 28,
        text="W2",
        fill="#4CAF50",
        font=("Arial", 26, "bold")
    )
    canvas.create_text(
        80, 54,
        text="CORE",
        fill="#111",
        font=("Arial", 13, "bold")
    )
