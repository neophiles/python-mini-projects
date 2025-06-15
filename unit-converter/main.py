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
        self.normal_text = font.Font(family='Helvetica', size=12)
        self.bold_text = font.Font(family='Helvetica', size=12, weight='bold')

        # define unit measurement types
        self.measurement_types = ['length', 'mass', 'volume', 'temperature']

        # initialize list of units that will be updated based on selected measurement type
        self.units = []

        # instantiate UnitConverter
        self.unit_converter = UnitConverter()

        # call layout functions
        self.create_containers()
        self.create_header_frame_widgets()
        self.create_type_frame_widgets()
        self.create_input_frame_widgets()
        self.create_output_frame_widgets()
        self.create_footer_frame_widgets()
        self.reset()

    def create_containers(self):

        # define window grid layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4 , weight=1)
        self.grid_columnconfigure(0, weight=1)

        # create window frames
        # view frame border: highlightbackground='black', highlightthickness=1
        self.header_frame = tk.Frame(self, width=300, height=45)
        self.type_frame = tk.Frame(self, width=300, height=45)
        self.input_frame = tk.Frame(self, width=300, height=80)
        self.output_frame = tk.Frame(self, width=300, height=80)
        self.footer_frame = tk.Frame(self, width=300, height=50)

        # place frames on window grid
        self.header_frame.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        self.type_frame.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
        self.input_frame.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')
        self.output_frame.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')
        self.footer_frame.grid(row=4, column=0, padx=5, pady=5, sticky='nsew')
        
        # keep frame sizes
        self.header_frame.grid_propagate(False)
        self.type_frame.grid_propagate(False)
        self.input_frame.grid_propagate(False)
        self.output_frame.grid_propagate(False)
        self.footer_frame.grid_propagate(False)

    def create_header_frame_widgets(self):
        # create and place title label
        self.title_label = tk.Label(self.header_frame, text='Unit Converter', font=self.bold_text)
        self.title_label.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        
    def create_type_frame_widgets(self):
        
        # create measurement type label
        self.measurement_type_label = tk.Label(self.type_frame, text='Measurement:', font=self.normal_text)
        
        # create measurement type dropdown
        self.measurement_type = tk.StringVar()
        self.measurement_type_cbbx = ttk.Combobox(self.type_frame, values=self.measurement_types, textvariable=self.measurement_type, width=12, state='readonly')

        # place widgets on frame grid
        self.measurement_type_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.measurement_type_cbbx.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')
        
        # bind combobox event to corresponding action function
        self.measurement_type_cbbx.bind('<<ComboboxSelected>>', self.measurement_type_selected)

    def create_input_frame_widgets(self):

        # create input label and field
        self.input_value = tk.StringVar()
        self.input_label = tk.Label(self.input_frame, text='From:', font=self.normal_text)
        self.input_entry = tk.Entry(self.input_frame, textvariable=self.input_value, font=self.normal_text, width=20)
        
        # create input unit dropdown
        self.input_unit = tk.StringVar()
        self.input_unit_cbbx = ttk.Combobox(self.input_frame, values=self.units, textvariable=self.input_unit, width=12)

        # place widgets on frame grid
        self.input_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.input_entry.grid(row=2, column=0, padx=(5, 0), pady=5, sticky='nsew')
        self.input_unit_cbbx.grid(row=2, column=1, padx=(0, 5), pady=5, sticky='nsew')

        # bind combobox event to corresponding action function
        self.input_unit_cbbx.bind('<<ComboboxSelected>>', self.input_unit_selected)

    def create_output_frame_widgets(self):

        # create output label and field
        self.output_value = tk.StringVar()
        self.output_label = tk.Label(self.output_frame, text='To:', font=self.normal_text)
        self.output_entry = tk.Entry(self.output_frame, textvariable=self.output_value, font=self.normal_text, width=20, state='readonly')

        # create output unit dropdown
        self.output_unit = tk.StringVar()
        self.output_unit_cbbx = ttk.Combobox(self.output_frame, values=self.units, textvariable=self.output_unit, width=12)

        # place widgets on frame grid
        self.output_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.output_entry.grid(row=2, column=0, padx=(5, 0), pady=5, sticky='nsew')
        self.output_unit_cbbx.grid(row=2, column=1, padx=(0, 5), pady=5, sticky='nsew')

        # bind combobox event to corresponding action function
        self.output_unit_cbbx.bind('<<ComboboxSelected>>', self.output_unit_selected)
    
    def create_footer_frame_widgets(self):

        # create buttons
        self.reset_btn = tk.Button(self.footer_frame, text='Clear', command=self.reset)
        self.convert_btn = tk.Button(self.footer_frame, text='Convert', command=self.convert)
        self.copy_btn = tk.Button(self.footer_frame, text='Copy Result', command=self.copy_to_clipboard)

        # place buttons on the frame grid
        self.reset_btn.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        self.convert_btn.grid(row=0, column=1, padx=5, pady=5, sticky='w')
        self.copy_btn.grid(row=0, column=2, padx=5, pady=5, sticky='w')

    def measurement_type_selected(self, event):
        selected = self.measurement_type_cbbx.get()
        self.unit_converter.set_measurement_type(selected) # sets self.type in self.unit_converter 
        self.units = self.unit_converter.get_units() # gets units based on measurement type
        print(f'Selected measurement type: {selected}') 

        self.clear_fields() # clears and prepares fields for new user input

        # enables fields only after selecting measurement type
        self.input_entry.config(state='normal')
        self.input_unit_cbbx.config(values=self.units, state='readonly')
        self.output_unit_cbbx.config(values=self.units, state='readonly')

    def input_unit_selected(self, event):
        selected = self.input_unit_cbbx.get()
        print(f'Selected input unit: {selected}')
    
    def output_unit_selected(self, event):
        selected = self.output_unit_cbbx.get()
        print(f'Selected output unit: {selected}')

    def convert(self):
        try:

            # retrieves user input in fields
            input_value = self.input_value.get()
            input_unit = self.input_unit.get()
            output_unit = self.output_unit.get()

            # checks if all fields are filled
            if input_value != '' and all(unit in self.units for unit in [input_unit, output_unit]):
                
                # converts units
                output_value = self.unit_converter.convert(float(input_value), input_unit, output_unit)
                print(f'Successfully converted: {input_value} {input_unit} = {output_value} {output_unit}')

                # displays conversion in the output value field
                self.output_value.set(output_value)

            else:
                print('All fields not filled.')

        except Exception as e:
            self.output_value.set('Invalid starting value') # displays error message in the output value field
            print(f'Unexpected error: {e}')

    def reset(self):
        self.clear_fields()
        self.measurement_type_cbbx.set('Select type') # clears measurement type field

        # disables other fields until a measurement type is selected
        self.input_entry.config(state='disabled')
        self.input_unit_cbbx.config(state='disabled')
        self.output_unit_cbbx.config(state='disabled')
        print('Fields cleared.')
    
    def clear_fields(self):
        # resets input and output fields
        self.input_value.set('')
        self.output_value.set('')
        self.input_unit_cbbx.set('Select unit')
        self.output_unit_cbbx.set('Select unit')
        
    def copy_to_clipboard(self):
        # copies converted result to clipboard
        result = self.output_value.get()
        if result: # checks if there is a result
            self.clipboard_clear()
            self.clipboard_append(result)
            self.update() # keeps copied result after program/window is closed
            print('Copied to clipboard!')
        else:
            print('Nothing to copy.')

if __name__ == '__main__':
    app = App()
    app.mainloop()