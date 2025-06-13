# Tkinter Unit Converter
# Created by Marc Neil Tagle, June 2025
# For educational purposes

class UnitConverter:
    
    def __init__(self):
        
        # metric conversion factors with meters as the base unit
        self.metric_conversion_factors = {
            'mm': 1000,
            'cm': 100,
            'm': 1,
            'km': 0.001
        }

        # imperial conversion factors with feet as the base unit
        self.imperial_conversion_factors = {
            'in': 12,
            'ft': 1,
            'yd': 1/3,
            'mi': 1/5280
        }

    def get_units(self):
        # returns a list of all units in all system dictionaries
        return list(self.metric_conversion_factors) + (list(self.imperial_conversion_factors))

    def convert(self, length, unit_from, unit_to):

        # metric-imperial conversion constants
        METER_TO_FOOT = 3.28084
        FOOT_TO_METER = 0.3048

        # checks the conversion system the starting unit is in
        system = self.metric_conversion_factors
        other = self.imperial_conversion_factors
        if unit_from in self.imperial_conversion_factors.keys():
            system = self.imperial_conversion_factors
            other = self.metric_conversion_factors

        basic_length = length / system[unit_from] # converts raw length to its basic unit
        
        # checks if starting and desired units are from the same or different conversion systems
        if unit_to not in system: 
            if unit_to in self.metric_conversion_factors.keys():
                converted = basic_length * FOOT_TO_METER
            else:
                converted = basic_length * METER_TO_FOOT
            converted *= other[unit_to]
        else:
            converted = basic_length * system[unit_to]

        return converted