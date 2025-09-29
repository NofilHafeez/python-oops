
# import  math
import random
# from Range.range import Range
# from File.file import File
from makeChange.change import MakeChange
from makeChange.CounterMachine.machine import CounterMachine
from Words.words import Words
from Words.List.list import List

class App:
    def run(self):
        def is_multiple(n, m):
            # if n = 4 a m =2
            m = 2*m
            # n = 2*n
            if (n == m) :
                return True
            else:
                return False
        boolean = is_multiple(8, 4)
        # print(boolean)


        def is_even(k):
            for i in range(2, 11, 2): # only runs from 2 to 10 and checks it from this range
                if (k == i):    # if true will stop
                    return True
            return False 
        # false if there is no true will stop
        # if there is true then it runs again and checks and then it become true
        # like for 4 integer the first loop check 2 == 4 not satisfy again loop check 4 == 4 true
        # if there is an odd number like 3 if will run from 2 to 10 if it will not find will return false
        boolean = is_even(10)
        # print(boolean)


        # def minmax(data):
        #     if(not isinstance(data, list)):
        #         data = list(data)

        #     min = 0
        #     max = 0

        #     for i in range(len(data)):
        #         for k in range(len(data)):
        #             if (data[i] < data[k]):
        #                 min = data[i]
        #             if (not min == 0):
        #                 break

        #     for i in range(len(data)):
        #         for k in range(len(data)):
        #             if (data[i] > data[k]):
        #                 max = data[i]
        #             if (not max == 0):
        #                 break

        #     tuple = (min, max)
        #     return tuple

            
        
        # min = minmax([1, 4, 3, 10, 42])
        # # print(min)


    def positievSqSum(n):
        if n <= 0:
            raise ValueError("Should be positive")
        
        squareSum = 0
        # array = []
        for i in range(n):
            squareSum += (i ** 2) # 1 option

            # array.append(i ** 2)
            # squareSum = sum(array, start=0) # 2 option


        return squareSum
    

    sum1 = positievSqSum(4)
    # print(sum1)

    # comprehension syntax in one line
    squareSum = sum((int(i) ** 2) for i in range(4))
    # print(squareSum)


    def OddSqSum(n):
        if n <= 0:
            raise ValueError("Should be positive")
        
        squareSum = 0
        # array = []
        for i in range(1, n, 2):
            print(i)
            squareSum += (i ** 2) # 1 option

            # array.append(i ** 2)
            # squareSum = sum(array, start=0) # 2 option


        return squareSum
    
    # oddsum = OddSqSum(10)
    # print(oddsum)

    # comprehension syntax in one line
    oddsum2 = sum((int(i) ** 2) for i in range(1, 10, 2))
    # print(oddsum2)

    # negative index
    string = 'hello'
    # print(string[-1])

    # positive index
    j = len(string) + (-1)
    # print(string[j])


    # for i in range(50, 90, 10):
    #     print(i)


    # for i in range(-8, 9, 2):
        # print(i)


    list1 = [2 ** i for i in range(1, 9)]
    print(list1)


    def choice(data):
        list1 = data
        # it takes start and end (total length of list) number and then give random number
        #  and give me that number as a index in list to get random element.
        random1 = random.randrange(0, len(list1))
        return list1[random1]

    r1 = choice(list1)
    # print(r1)

    # random.choice()

    # range = Range(5)
    # print(range)

    # my range class
    # for i in Range(0, 10, 2):
    #     print("my", i)

    # for i in range(2, 10, -2):
    #     print(i)


 


class Even:
    @staticmethod
    def is_even(k):
        for i in range(2, 11, 2): # only runs from 2 to 10 and checks it from this range
            if (k == i):    # if true will stop
                return k
        return False 
    # false if there is no true will stop
    # if there is true then it runs again and checks and then it become true
    # like for 4 integer the first loop check 2 == 4 not satisfy again loop check 4 == 4 true
    # if there is an odd number like 3 if will run from 2 to 10 if it will not find will return false

class SqSum:
 @staticmethod 
 def positievSqSum(n):
        if n <= 0:
            raise ValueError("Should be positive")
        
        squareSum = 0
        # array = []
        for i in range(n):
            squareSum += (i ** 2) # 1 option

            # array.append(i ** 2)
            # squareSum = sum(array, start=0) # 2 option


        return  squareSum


even = Even.is_even(4)
print(even)

sqSum = SqSum.positievSqSum(even)
print(sqSum)

# print(sum)

# Association ex





class Even:
    def __init__(self, k):
        self.k = k

    def is_even(self, ):
        for i in range(2, 11, 2): # only runs from 2 to 10 and checks it from this range
            if (self.k == i):    # if true will stop
                return self.k
        return False 
    # false if there is no true will stop
    # if there is true then it runs again and checks and then it become true
    # like for 4 integer the first loop check 2 == 4 not satisfy again loop check 4 == 4 true
    # if there is an odd number like 3 if will run from 2 to 10 if it will not find will return false

class SqSum:
    def __init__(self, n: Even):
        self.n = n
 
    def positievSqSum(self):
        if self.n.k <= 0:
            raise ValueError("Should be positive")
        
        squareSum = 0
        # array = []
        for i in range(self.n.k):
            squareSum += (i ** 2) # 1 option

            # array.append(i ** 2)
            # squareSum = sum(array, start=0) # 2 option


        return  squareSum
    


even = Even(4)
# print(even)
sqSum = SqSum(even)
sum = sqSum.positievSqSum()

print(sum)

# if we delete SqSum the Even will still exists

# Aggregation



class Even:
    def __init__(self, k):
        self.k = k

    def is_even(self):
        for i in range(2, 11, 2): # only runs from 2 to 10 and checks it from this range
            if (self.k == i):    # if true will stop
                return True
        return False 
    # false if there is no true will stop
    # if there is true then it runs again and checks and then it become true
    # like for 4 integer the first loop check 2 == 4 not satisfy again loop check 4 == 4 true
    # if there is an odd number like 3 if will run from 2 to 10 if it will not find will return false

class SqSum:
    def __init__(self, even):
        self.even = Even(even)
 
    def positievSqSum(self):
        if  not self.even.is_even():     # Ai help
            raise ValueError("Not an even number")
        
        squareSum = 0
        # array = []
        k = self.even.k
        for i in range(k):
            squareSum += (i ** 2) # 1 option

            # array.append(i ** 2)
            # squareSum = sum(array, start=0) # 2 option


        return  squareSum



sqSum = SqSum(4)
sum = sqSum.positievSqSum()
print(sum)

# if we delete SqSum the Even will also be deleted because we are making its instance inside the SqSum

# Composition



# Association
counter = CounterMachine(1550, 2000)
change = MakeChange(obj=counter)
print(change.makeChange())


# Composition
counter = CounterMachine(1550, 2000)
change = MakeChange(counter.amountCharged, counter.amountGiven)
print(change.makeChange())


# Aggregation
counter = CounterMachine(1550, 2000)
change = MakeChange(aggregate_obj=counter)
print(change.makeChange())

# did by constucter overloading




# Association
list3 = List(["hi", "bye", "bye"])
words = Words(asso=list3.list[2])
print(words.count_words())


# Composition
list2 = ["hi", "bye", "bye"]
words = Words(comps=list2)
print(words.count_words())

# Aggregation

list1 = List(["hi", "bye", "bye"])
words = Words(aggreg=list1)
print(words.count_words())

# did by constucter overloading










    
 
