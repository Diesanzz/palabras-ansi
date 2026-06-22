import tkinter as tk
from tkinter import ttk


class DFAVisualizer:
    def __init__(self, history):
        self.history = history
        self.index = 0

        self.root = tk.Tk()
        self.root.title("Visualizador DFA - Palabras Reservadas ANSI C")
        self.root.geometry("900x500")

        self.title_label = tk.Label(
            self.root,
            text="Ejecución del Autómata Finito Determinista",
            font=("Arial", 18, "bold")
        )
        self.title_label.pack(pady=10)

        self.canvas = tk.Canvas(self.root, width=850, height=260, bg="white")
        self.canvas.pack(pady=10)

        self.info_label = tk.Label(
            self.root,
            text="Presiona 'Siguiente paso' para iniciar.",
            font=("Arial", 12),
            justify="left"
        )
        self.info_label.pack(pady=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.next_button = ttk.Button(
            self.button_frame,
            text="Siguiente paso",
            command=self.next_step
        )
        self.next_button.grid(row=0, column=0, padx=10)

        self.auto_button = ttk.Button(
            self.button_frame,
            text="Ejecutar automático",
            command=self.auto_run
        )
        self.auto_button.grid(row=0, column=1, padx=10)

        self.reset_button = ttk.Button(
            self.button_frame,
            text="Reiniciar",
            command=self.reset
        )
        self.reset_button.grid(row=0, column=2, padx=10)

        self.draw_base("q0", "", "")

    def draw_base(self, previous_state, symbol, next_state):
        self.canvas.delete("all")

        x1, y1 = 200, 130
        x2, y2 = 650, 130

        self.canvas.create_oval(x1 - 55, y1 - 55, x1 + 55, y1 + 55, width=3)
        self.canvas.create_text(x1, y1, text=previous_state, font=("Arial", 16, "bold"))

        if next_state:
            self.canvas.create_oval(x2 - 55, y2 - 55, x2 + 55, y2 + 55, width=3)
            self.canvas.create_text(x2, y2, text=next_state, font=("Arial", 16, "bold"))

            self.canvas.create_line(x1 + 60, y1, x2 - 60, y2, arrow=tk.LAST, width=3)
            self.canvas.create_text(
                (x1 + x2) // 2,
                y1 - 25,
                text=f"lee '{symbol}'",
                font=("Arial", 14)
            )
        else:
            self.canvas.create_text(
                430,
                130,
                text="Estado inicial del autómata",
                font=("Arial", 15)
            )

    def next_step(self):
        if self.index >= len(self.history):
            self.info_label.config(text="La ejecución del DFA ha terminado.")
            return

        step = self.history[self.index]

        if step.get("closed"):
            text = (
                f"Fin de token: {step['token']}\n"
                f"Estado final: {step['from']}\n"
                f"Regreso al estado inicial: {step['to']}"
            )

            self.draw_base(step["from"], "delimitador", step["to"])

        else:
            text = (
                f"Línea: {step['line']} | Columna: {step['column']}\n"
                f"Token parcial: {step['token']}\n"
                f"Caracter leído: {step['char']}\n"
                f"Transición: {step['from']} -> {step['to']}"
            )

            self.draw_base(step["from"], step["char"], step["to"])

        self.info_label.config(text=text)
        self.index += 1

    def auto_run(self):
        if self.index < len(self.history):
            self.next_step()
            self.root.after(500, self.auto_run)

    def reset(self):
        self.index = 0
        self.info_label.config(text="Presiona 'Siguiente paso' para iniciar.")
        self.draw_base("q0", "", "")

    def run(self):
        self.root.mainloop()