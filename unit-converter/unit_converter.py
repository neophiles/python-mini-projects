# Tkinter Unit Converter
# Created by Marc Neil Tagle, June 2025
# For educational purposes

import math

class UnitConverter:
    
    def __init__(self):
        
        # list of dictionaries containg basic units of measurements
        self.measurement_types = [

            # length metric units
            {
                'mm': 1000,
                'cm': 100,
                'm': 1,
                'km': 0.001
            },

            # length imperial units
            {
                'in': 12,
                'ft': 1,
                'yd': 1/3,
                'mi': 1/5280
            },

            # weight metric units
            {
                'mg': 1000,
                'g': 1,
                'kg': 1/1000,
                't': 1/1000000
            },

            # weight imperial units
            {
                'oz': 16,
                'lb': 1,
                'st': 1/14
            },

            # volume metric units
            {
                'mL': 1000,
                'L': 1
            },

            # volume imperial units
            {
                'fl oz': 128,
                'pt': 8,
                'qt': 4,
                'gal': 1
            }

        ]

        # initialize other class attributes
        self.type = ''
        self.type_systems = []
        self.CONVERSION_CONSTANT = 0
    
    def set_measurement_type(self, type):
        self.type = type # sets measurement type

        # determines corresponding index in self.measurement_types and cross-system conversion constant
        if self.type == 'length':
            self.type_systems = self.measurement_types[0:2]
            self.CONVERSION_CONSTANT = 3.280839895013123 
        elif self.type == 'mass':
            self.type_systems = self.measurement_types[2:4]
            self.CONVERSION_CONSTANT = 453.59237
        elif self.type == 'volume':
            self.type_systems = self.measurement_types[4:6]
            self.CONVERSION_CONSTANT = 3.785411784

    def get_units(self):
        # returns a list of all units in all system dictionaries
        return list(unit for system in self.type_systems for unit in system.keys())        
    
    def identify_measurement_system(self, unit):
        # determines the system of selected unit based on the measurement type
        for system in self.type_systems:
            if unit in system.keys():
                return system

    def convert(self, value, unit_from, unit_to):

        # gets measurement system of starting unit
        system = self.identify_measurement_system(unit_from)

        # converts raw length to its basic system unit value
        basic_value = value / system[unit_from] 
        
        # checks if starting and desired units are from the same or different conversion systems
        if unit_to not in system:
            other = self.identify_measurement_system(unit_to)

            # i don't know if this is big brain move (i just found a way)
            ''' if product of system's conversion values > that of counterpart system, basic unit value divided by constant;
                otherwise, it is multiplied by the constant '''
            if math.prod(other.values()) > math.prod(system.values()):
                converted = basic_value / self.CONVERSION_CONSTANT
            else:
                converted = basic_value * self.CONVERSION_CONSTANT

            converted *= other[unit_to] # converts cross-system converted value to user's desired unit

        else:
            converted = basic_value * system[unit_to] # directly converts basic unit value to user's desired unit

        # removes trailing zero decimal if result is a whole number
        if converted % 1 == 0:
            converted = int(converted)

        return converted