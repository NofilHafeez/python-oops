import math
from ValidationClass.validate import Validate
class NthVector:
    def __init__(self, items):
        self.values = tuple(items) # or list??

    def get_item(self, i):
        return self.values[i]

    def set_item(self, i, value):
        self.values[i] = value

    def get_len(self):
        return len(self.values)
    
    def do_adding(self, other):
        Validate.validate_len(self, other)
        
        result = [0] * len(self)
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return NthVector(result)

    def do_subtracting(self, other):
        Validate.validate_len(self, other)

        result = [0] * len(self)
        for i in range(len(self)):
            result[i] = self[i] - other[i]
        return NthVector(result)
    
    # public
    def dot_Product(self, other):
        Validate.validate_len(self, other)

        dot_product = 0
        for i in range(len(self)):
            dot_product += self[i] * other[i]
        return dot_product
    
    def get_magnitude(self):
        magnitude = 0
        for i in range(len(self)):
            magnitude += self[i] ** 2
        return math.sqrt(magnitude)
    
    def get_angle(self, other):
        Validate.validate_len(self, other)
        
        dot_product = self.__dotProduct__(other)
        magnitude_self = self.__magnitude__()    
        magnitude_other = other.__magnitude__()

        value = dot_product / (magnitude_self * magnitude_other)

        angle = math.degrees(math.acos(value)) 
        return angle # Returns angle in dgrees

    def __eq__(self, other):
        return self.values == other.values
    
    def __ne__(self, other):
        return self.values != other.values
    
    def __repr__(self):
        return f"Vector({self.values})"
    
    def __str__(self):
        return f"Vector({self.values})"
        
