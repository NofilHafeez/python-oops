from NdimensionalVector.vector import NthVector
class Validate:
    @staticmethod 
    def validate_len(other: NthVector , other1: NthVector):
        if len(other) !=  len(other1):
            raise ValueError("not same length")

    @staticmethod 
    def validate_type(other: NthVector, other1: NthVector):
        if (isinstance(other, NthVector) and isinstance(other1, NthVector)):
             return True
        else:
            raise ValueError("no same type")
    
    
        