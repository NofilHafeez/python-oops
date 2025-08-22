
class Validate:
    @staticmethod 
    def validate_len(other , other1):
        if len(other) !=  len(other1):
            raise ValueError("not same length")

    @staticmethod 
    def validate_type(other, other1):
        if (isinstance(other) and isinstance(other1)):
             return True
        else:
            raise ValueError("no same type")
    
    
        