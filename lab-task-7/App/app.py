from RationalNumber.rational import Rational
from Vector2D.vector import Vector
# from Vector2D.vectorOperationsClasses.magnitude import Magnitude
# from Vector2D.vectorOperationsClasses.dotProduct import DotProduct
from Vector2D.vectorOperationsClasses.angle import Angle



class App:
    def run(self):
        r1 = Rational(5, 10)
        r2 = Rational(10, 5)

        v = Vector(1, 3)
        v1 = Vector(1, 3)

        angle = Angle()
        

        print(angle.__angle__(v, v1))



        print(v)
        print(v + v1)
        





        # print(r1 + r2)
        # print(r1 - r2)
        # print(r1 * r2)
        # print(r1 / r2)










