# Unit Converter

A simple unit conversion tool built with Python and Tkinter. This beginner-friendly GUI application currently supports length conversions and is designed to be expanded for additional measurement types such as weight, temperature, and volume.

## Features
- Length conersion between common metric and imperial units
- Graphical user interface (GUI) using Tkinter
- Two dropdown menus (comboboxes) to select source and target units
- Clear button to reset all fields
- Input validation for clean and error-free user intreraction

## Project Structure
- 'main.py' - Entry point of the program; handles all user interface components through the 'App' class
- 'unit_converter.py' - Contains the 'UnitConverter' class, responsible for handling conversion logic

## Code Design
- Conversion factors are organized as dictionaries inside the UnitConverter constructor
- Module class-based design for clean separation of logic and UI
- Easily extendable: additional dictionaries for other unit types can be added in the future

## Future Plans
- Add support for:
    - Weight (e.g., grams <-> pounds)
    - Temperature (e.g., Celsius <-> Fahrenheit)
    - Volume (e.g., liters <-> gallons)
- Improve error handling and UX feedback