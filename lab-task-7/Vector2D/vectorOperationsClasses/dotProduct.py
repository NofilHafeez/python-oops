from Vector2D.vector import Vector
class DotProduct:
    @staticmethod
    def __dotProduct__(other:Vector, other1: Vector):
        if len(other) != len(other1):
            raise ValueError("Vectors must be of the same dimension")
        
        dot_product = 0

        dot_product += other[0] * other1[0]
        dot_product += other[1] * other1[1]

        return dot_product