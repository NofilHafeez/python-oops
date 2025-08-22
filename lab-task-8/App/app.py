from NdimensionalVector.vector  import NthVector
from Range.range import Range

class App:
    def run(self):
        v = NthVector([2, 3, 5, 3, 2])
        v1 = NthVector([2, 3, 9, 10, 2])

        r1 = Range(2,4,1)
        
        # print(list(r1))
        # print(r1[1])

        for i in r1:
            print(i)

        print(v.get_angle(v1))


        # print(range(1, 30, 3))


        # print (v == v1)
        # print (v != v1)

        # print(v + v1)
        # print(len(v))










