class Vector:
    def __init__(self, *items):
        if (len(items) > 2):
            raise ValueError('2dVector only')
        self.__cords = list(items)

    
    def __getitem__(self, i):
        return self.__cords[i]

    def __setitem__(self, i, value):
        self.__cords[i] = value


    def __len__(self):
        return len(self.__cords)
    

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vectors must be of the same dimension")
        
        # len(self) = dimension of the vector -
        # vector(d) will create a vector of dimension d and retrun 
        # object of vector class = [0, 0]
        
        result = Vector(0,0)  
        result[0] = self[0] + other[0]
        result[1] = self[1] + other[1]
        return result
    
    def __repr__(self):
        return f"Vector({self.__cords})"

    def __str__(self):
        return f"Vector({self.__cords})"

  