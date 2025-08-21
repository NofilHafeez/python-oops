from Vector2D.vector import Vector

class Magnitude:
    @staticmethod
    def __magnitude__(other: Vector):
        magnitude = 0
        magnitude += other[0] ** 2
        magnitude += other[1] ** 2 
        return magnitude ** 0.5 
        









      
