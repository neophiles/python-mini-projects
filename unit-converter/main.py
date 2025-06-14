# Tkinter Unit Converter
# Created by Marc Neil Tagle, June 2025
# For educational purposes

import tkinter as tk
from tkinter import ttk, font
from unit_converter import UnitConverter

class App(tk.Tk):

    def __init__(self):
        super().__init__() # inherits from tk.Tk
        self.title('Unit Converter') # defines window title
        self.geometry('300x300+0+0') # defines window dimensions
        self.resizable(0, 0) # disables window resizing

        # define text fonts
        self.normal_text = font.Font(family="Helvetica", size=12)
        self.bold_text = font.Font(family="Helvetica", size=12, weight='bold')

        # instantiate UnitConverter
        self.unit_converter = UnitConverter()
        self.units = self.unit_converter.get_units() # extract units

        # call layout functions
        self.create_containers()
        self.create_header_frame_widgets()
        self.create_input_frame_widgets()
        self.create_output_frame_widgets()
        self.create_footer_frame_widgets()
        self.reset_fields()

    def create_containers(self):

        # define window grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        #self.grid_columnconfigure(1, weight=1)

        # create window frames
        # highlightbackground='black', highlightthickness=1
        self.header_frame = tk.Frame(self, width=300, height=50)
        self.input_frame = tk.Frame(self, width=300, height=100)
        self.output_frame = tk.Frame(self, width=300, height=100)
        self.footer_frame = tk.Frame(self, width=300, height=50)

        # place frames on window grid
        self.header_frame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        self.input_frame.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
        self.output_frame.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')
        self.footer_frame.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')
        
        # keep frame sizes
        self.header_frame.grid_propagate(False)
        self.input_frame.grid_propagate(False)
        self.output_frame.grid_propagate(False)
        self.footer_frame.grid_propagate(False)

    def create_header_frame_widgets(self):
        # create and place title label
        self.title_label = tk.Label(self.header_frame, text='Unit Converter', font=self.bold_text)
        self.title_label.grid(row=0, column=0, sticky='nsew')

    def create_input_frame_widgets(self):

        # create input label and field
        self.input_value=tk.StringVar()
        self.input_label = tk.Label(self.input_frame, text='From:', font=self.bold_text)
        self.input_entry = tk.Entry(self.input_frame, textvariable=self.input_value, font=self.normal_text, width=20)
        
        # create input unit dropdown
        self.input_unit=tk.StringVar()
        self.input_unit_cbbx = ttk.Combobox(self.input_frame, values=self.units, textvariable=self.input_unit, width=12, state='readonly')

        # place widgets on frame grid
        self.input_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.input_entry.grid(row=2, column=0, padx=(5, 0), pady=5, sticky='nsew')
        self.input_unit_cbbx.grid(row=2, column=1, padx=(0, 5), pady=5, sticky='nsew')

        # bind combobox event
        self.input_unit_cbbx.bind('<<ComboboxSelected>>', self.input_unit_selected)

    def create_output_frame_widgets(self):

        # create output label and field
        self.output_value=tk.StringVar()
        self.output_label = tk.Label(self.output_frame, text='To:', font=self.bold_text)
        self.output_entry = tk.Entry(self.output_frame, textvariable=self.output_value, font=self.normal_text, width=20, state='readonly')

        # create output unit dropdown
        self.output_unit=tk.StringVar()
        self.output_unit_cbbx = ttk.Combobox(self.output_frame, values=self.units, textvariable=self.output_unit, width=12, state='readonly')

        # place widgets on frame grid
        self.output_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.output_entry.grid(row=2, column=0, padx=(5, 0), pady=5, sticky='nsew')
        self.output_unit_cbbx.grid(row=2, column=1, padx=(0, 5), pady=5, sticky='nsew')

        # bind combobox event
        self.output_unit_cbbx.bind('<<ComboboxSelected>>', self.output_unit_selected)
    
    def create_footer_frame_widgets(self):

        # create buttons
        self.reset_btn = tk.Button(self.footer_frame, text='Clear', command=self.reset_fields)
        self.convert_btn = tk.Button(self.footer_frame, text='Convert', command=self.convert)
        self.copy_btn = tk.Button(self.footer_frame, text='Copy Result', command=self.copy_to_clipboard)

        # place buttons on the frame grid
        self.reset_btn.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.convert_btn.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        self.copy_btn.grid(row=0, column=2, padx=5, pady=5, sticky='w')       

    def input_unit_selected(self, event):
        selected = self.input_unit_cbbx.get()
        #print(f"Selected input unit: {selected}")
    
    def output_unit_selected(self, event):
        selected = self.output_unit_cbbx.get()
        #print(f"Selected output unit: {selected}")

    def convert(self):
        try:

            # retrieves user input in fields
            input_value = self.input_value.get()
            input_unit = self.input_unit.get()
            output_unit = self.output_unit.get()

            # checks if all fields are filled
            if input_value != '' and all(unit in self.units for unit in [input_unit, output_unit]):

                # converts units
                self.result = self.unit_converter.convert(float(input_value), input_unit, output_unit)
                print(f"Successfull converted: {input_value} {input_unit} = {self.result} {output_unit}")

                # displays conversion in the output value field
                self.output_value.set(self.result)

            else:
                print("All fields not filled.")

        except Exception as e:
            print(f'Unexpected error: {e}')

    def reset_fields(self):
        # reset input and output fields
        self.input_value.set('')
        self.output_value.set('')
        self.input_unit_cbbx.set("Select unit")
        self.output_unit_cbbx.set("Select unit")
        print("Fields cleared.")

    def copy_to_clipboard(self):
        # copies converted result to clipboard
        if self.result: # checks if there is a result
            self.clipboard_clear()
            self.clipboard_append(self.result)
            self.update()
            print("Copied to clipboard!")
        else:
            print("Nothing to copy.")

if __name__ == '__main__':
    app = App()
    app.mainloop()