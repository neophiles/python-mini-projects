import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("500x700")

        self.top_frame = tk.Frame(bg="black", width=500, height=200, pady = 3)
        self.top_frame.grid(row=0, columnspan=1)

        self.body_frame = tk.Frame(bg='gray', width=500, height=400, padx=3, pady=3)
        self.body_frame.grid(row=1, columnspan=5)

        self.bot_frame = tk.Frame(bg='yellow', width=500, height=100, padx=3, pady=3)
        self.bot_frame.grid(row=2, columnspan=5)
       



app = Calculator()
app.mainloop()