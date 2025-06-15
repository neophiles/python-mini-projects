# Unit Converter

A beginner-friendly unit conversion tool built with Python and Tkinter. This GUI application now supports multiple measurement types, including **length**, **mass**, **volume**, and **temperature**.

## Features

- Convert between units of **length**, **mass**, **volume**, and **temperature**
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
- Temperature uses **custom formulas** instead of scaling factors
- Class-based **modular design** for a clear separation of logic and UI
- Easily **extensible**: just add new unit mappings and conversions to the `UnitConverter` class

## What I Learned

- How to build a GUI using Python's Tkinter library
- How to separate UI and logic using class-based design
- How to implement dropdowns (Combobox) and dynamic UI updates
- The importance of clean code, modularity, and readability
- How to use Git and write meaningful commit messages
- How to document a project with a structured and informative README
- How to perform basic temperature conversions using formulas instead of static factors

This project helped me gain more confidence in Python and GUI development. I'm excited to explore more advanced features and build new tools!
