import tkinter as tk
import math


class AdvancedCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Advanced Calculator")
        self.geometry("400x600")

        self.entry = tk.Entry(self, width=22, font=("Arial", 24), borderwidth=2, relief="solid")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 'sin',
            '4', '5', '6', '*', 'cos',
            '1', '2', '3', '-', 'tan',
            '0', '.', '=', '+', 'log',
            '(', ')', '^', 'sqrt', 'C'
        ]

        row = 1
        col = 0
        for button in buttons:
            command = lambda x=button: self.on_button_click(x)
            if button not in ('=', 'C'):
                tk.Button(self, text=button, width=9, height=2, command=command).grid(row=row, column=col, padx=5,
                                                                                      pady=5)
            elif button == '=':
                tk.Button(self, text=button, width=9, height=2, command=self.calculate_result).grid(row=row, column=col,
                                                                                                    padx=5, pady=5)
            elif button == 'C':
                tk.Button(self, text=button, width=9, height=2, command=self.clear_entry).grid(row=row, column=col,
                                                                                               padx=5, pady=5)

            col += 1
            if col > 4:
                col = 0
                row += 1

    def on_button_click(self, char):
        self.entry.insert(tk.END, char)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def calculate_result(self):
        try:
            expression = self.entry.get()
            result = eval(self.replace_math_functions(expression))
            self.clear_entry()
            self.entry.insert(tk.END, str(result))
        except Exception as e:
            self.clear_entry()
            self.entry.insert(tk.END, "Error")

    def replace_math_functions(self, expression):
        replacements = {
            'sin': 'math.sin',
            'cos': 'math.cos',
            'tan': 'math.tan',
            'log': 'math.log10',
            'sqrt': 'math.sqrt',
            '^': '**'
        }
        for key, value in replacements.items():
            expression = expression.replace(key, value)
        return expression


if __name__ == "__main__":
    app = AdvancedCalculator()
    app.mainloop()
