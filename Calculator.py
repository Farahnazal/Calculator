import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        
        self.expression = ""
        self.result_var = tk.StringVar()

        self.create_display()
        self.create_buttons()

    def create_display(self):
        display_frame = ttk.Frame(self.root, padding=(10, 10))
        display_frame.pack(fill=tk.BOTH, expand=True)

        display_entry = ttk.Entry(display_frame, textvariable=self.result_var, font=('Arial', 14), justify='right')
        display_entry.pack(fill=tk.BOTH, expand=True)

    def create_buttons(self):
        buttons_frame = ttk.Frame(self.root)
        buttons_frame.pack(fill=tk.BOTH, expand=True)

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('=', 3, 2), ('+', 3, 3),
            ('(', 4, 0), (')', 4, 1), ('C', 4, 2), ('<-', 4, 3)
        ]

        for (text, row, column) in buttons:
            button = ttk.Button(buttons_frame, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

    def on_button_click(self, char):
        if char == '=':
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        elif char == 'C':
            self.expression = ""
        elif char == '<-':
            self.expression = self.expression[:-1]
        else:
            self.expression += char

        self.result_var.set(self.expression)

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
