# Unit Converter

A beginner-friendly unit conversion tool built with Python and Tkinter. This GUI application now supports multiple measurement types, including **length**, **mass**, and **volume**, and is designed to be further expanded.

## Features

- Convert between units of **length**, **mass**, and **volume**
- Dropdown selector to choose the **measurement type**
- Two dropdown menus (comboboxes) to select **source** and **target** units
- Dynamic unit options update based on selected measurement type
- **Clear** button to reset all fields
- **Copy Result** button to copy the conversion output to clipboard
- Input validation for clean and error-free user interaction

## Project Structure

- `main.py` - Entry point of the program; handles all GUI components through the `App` class
- `unit_converter.py` - Contains the `UnitConverter` class, responsible for unit conversion logic

## Code Design

- Conversion factors are organized in a **dictionary of dictionaries** by measurement type inside the `UnitConverter` class
- Class-based **modular design** for a clear separation of logic and UI
- Easily **extensible**: just add new unit mappings and conversions to the `UnitConverter` class

## Future Plans

- Add support for:
  - **Temperature** (e.g., Celsius <-> Fahrenheit)
- Improve **UX/UI styling** (e.g., dark mode, responsive layout)
