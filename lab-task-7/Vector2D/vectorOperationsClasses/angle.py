from Vector2D.vector import Vector
from Vector2D.vectorOperationsClasses.dotProduct import DotProduct
from Vector2D.vectorOperationsClasses.magnitude import Magnitude

import math

class Angle:
    @staticmethod
    def __angle__(other:Vector, other1: Vector):
        if len(other) != len(other1):
            raise ValueError("Vectors must be of the same dimension")
        
        # dot_product = DotProduct()
        dot_product = DotProduct().__dotProduct__(other, other1)
        print(f"dot_product: {dot_product}")

        magnitude = Magnitude()

        magnitude_other = magnitude.__magnitude__(other)
        print(f"magnitude_self: {magnitude_other}")

        magnitude_other1 = magnitude.__magnitude__(other1)
        print(f"magnitude_other: {magnitude_other1}")

        value = dot_product / (magnitude_other * magnitude_other1)

        angle = math.degrees(math.acos(value)) 
        return angle # Returns angle in dgrees