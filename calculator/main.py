import tkinter as tk

class Calculator(tk.Tk):

    def __init__(self):
        super().__init__()

        # window settings
        self.title('Calculator')
        self.geometry('400x500+0+0')
        self.resizable(0, 0)

        # define window grid
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.create_containers()
        self.create_display_widgets()
        self.create_button_widgets()


    def create_containers(self):

        # define main containers/frames
        self.display_frame = tk.Frame(bg='lightgray', width=400, height=100, padx=5, pady=5)
        self.buttons_frame = tk.Frame(bg='black', width=400, height=400, padx=5, pady=5)

        # position containers
        self.display_frame.grid(row=0, column=0, sticky='nsew')
        self.buttons_frame.grid(row=1, column=0, sticky='nsew')

        self.display_frame.grid_propagate(False)
        self.buttons_frame.grid_propagate(False)

        # define button frame grid
        for r in range(5):
            self.buttons_frame.rowconfigure(r, weight=1, uniform='row')
            for c in range(5):
                 self.buttons_frame.columnconfigure(c, weight=1, uniform='col')


    def create_display_widgets(self):
        self.display_text = ''
        self.display_label = tk.Label(self.display_frame, height=4, text=self.display_text, font=('Helvetica 12'), bg='lightgray')
        self.display_label.pack(side='right')
        

    def create_button_widgets(self):

        self.buttons = {}
        button_texts = [
            ['7', '8', '9', 'DEL', 'AC'],
            ['4', '5', '6', '+', '-'],
            ['1', '2', '3', 'x', '/'], 
            ['0', '.', '^', '(', ')'],
            ['ANS', '=']
        ]
    
        for r, row in enumerate(button_texts):
            for c, text in enumerate(row):
                if r == 4:
                    c += 3

                btn = tk.Button(self.buttons_frame, text=text, font=('Helvetica 12'), 
                                borderwidth=3, cursor='hand2', command=lambda t=text: self.on_button_click(t))
                btn.grid(row=r, column=c, sticky='nsew')

                self.buttons[text] = btn


    def on_button_click(self, value):
        self.display_text += value
        self.display_label.config(text=self.display_text)

        print(f"You clicked: {value}")

       
app = Calculator()
app.mainloop()