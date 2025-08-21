import math
class NthVector:
    def __init__(self, items):
        self.values = tuple(items) # or list??

    def __getitem__(self, i):
        return self.values[i]

    def __setitem__(self, items):    
        self.values = list(items)


    def __len__(self):
        return len(self.values)
    
    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("should be same length")
        
        result = [0] * len(self)
        for i in range(len(self)):
            result[i] = self[i] + other[i]
        return NthVector(result)
    
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("should be same length")
        
        result = [0] * len(self)
        for i in range(len(self)):
            result[i] = self[i] - other[i]
        return NthVector(result)
    

    def __dotProduct__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same dimension")
        
        dot_product = 0
        for i in range(len(self)):
            dot_product += self[i] * other[i]
        return dot_product
    
    def __magnitude__(self):
        magnitude = 0
        for i in range(len(self)):
            magnitude += self[i] ** 2
        return math.sqrt(magnitude)
    
    def __angle__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same dimension")
        
        dot_product = self.__dotProduct__(other)
        print(f"dot_product: {dot_product}")

        magnitude_self = self.__magnitude__()
        print(f"magnitude_self: {magnitude_self}")
        
        magnitude_other = other.__magnitude__()
        print(f"magnitude_other: {magnitude_other}")

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
        
