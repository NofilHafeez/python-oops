
# import  math
import random
from Range.range import Range
from File.file import File

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


        def minmax(data):
            if(not isinstance(data, list)):
                data = list(data)

            min = 0
            max = 0

            for i in range(len(data)):
                for k in range(len(data)):
                    if (data[i] < data[k]):
                        min = data[i]
                    if (not min == 0):
                        break

            for i in range(len(data)):
                for k in range(len(data)):
                    if (data[i] > data[k]):
                        max = data[i]
                    if (not max == 0):
                        break

            tuple = (min, max)
            return tuple

            
        
        min = minmax([1, 4, 3, 10, 42])
        # print(min)


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


    file = File('hi', 20)
    file1 = File('ho', 10)

    # --- Shallow Copy and Deep copy ----- (Understanding)

    # with equality and it changes the object - when we want to copy someone obj
    # file.shalowCopy(file1)
    # print(file.fileName, file.fileSize)
    # file.deepCopy(file1)
    # print(file.fileName, file.fileSize)

    # NOT BETTER APPROACH
    # with File class name and does not change the obj just return the copy obj - it returns the class object and we can place to other obj
    # d = file.deepCopy1(file1)
    # print(d)
    # s = file.shalowCopy1(file1)
    # print(s)

    # with cls and does not change the obj just return the copy obj -it returns the class object and we can place to other obj
    # d1 = file.deepCopy2(file1, File)
    # print(d1)
    # s1  = file.shalowCopy2(file1, File)
    # print(s1)

    # with __class__ better approach - it returns the class object and we can place to other obj
    # file = file1.deepCopy3()
    # print(file)
    # print(file1.fileName is file.fileName)  # False for deep

    # file  = file1.shallowCopy3()
    # print(file)

    # # print(file1 is file)   # False  (different objects)
    # print(file1.fileName is file.fileName)  # True for shallow, False for deep



# Association: Just a connection (Teacher ↔ Student)
# Aggregation: Whole-part, but parts can live without the whole (Library → Book).
# Composition: Whole-part, parts die with the whole (House → Room).

# Association: Just linked.
# Aggregation: "Has-a" but weak.
# Composition: "Has-a" but strong (lifetime tied).



# Association 
# class Teacher:
#     def __init__(self, name):
#         self.name = name

#     def teach(self, student):
#         print(f"{self.name} is teaching {student.name}")


# class Student:
#     def __init__(self, name):
#         self.name = name


# # Example
# teacher = Teacher("Mr. Ali")
# student = Student("Nofil")

# teacher.teach(student)   # Mr. Ali is teaching Nofil
# Teacher and student can be exist independently


# Aggregation
# class Book:
#     def __init__(self, title):
#         self.title = title


# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []   # aggregation

#     def add_book(self, book):
#         self.books.append(book)

#     def show_books(self):
#         print(f"{self.name} has these books:")
#         for book in self.books:
#             print(f"- {book.title}")


# # Example
# book1 = Book("Python Basics")
# book2 = Book("OOP in Depth")

# library = Library("City Library")
# library.add_book(book1)
# library.add_book(book2)

# library.show_books()

# # Books still exist even without the library
# print(book1.title)  # Python Basics
# Books exist independently of the Library.




# Composition:
# class Room:
#     def __init__(self, name):
#         self.name = name


# class House:
#     def __init__(self, address):
#         self.address = address
#         self.rooms = [Room("Bedroom"), Room("Kitchen")]  # composition

#     def show_rooms(self):
#         print(f"House at {self.address} has rooms:")
#         for room in self.rooms:
#             print(f"- {room.name}")


# # Example
# house = House("123 Street")
# house.show_rooms()

# # If the house is deleted, rooms are also gone
# del house
# # Now rooms can't exist independently



# In summary, what i understand is that, in association is just linked with each other like the teacher and with student one more example: Mother and child as a link and brother and sister, lawyer and client and more, in this the linked relation can also be treated individual, if there is no link between treacher and student they will be treated individually. if we talk about the Aggregation in this we use has-a relation just like the library and books example the books can also be exist if we remove the library the books will still exist and it is a aggregation, in more simple the child can be exist without the parent. In Compositioin, the child can not be exist without the parent if we remove the parent the child can also be gone. take the Mother and child ex. without the mother there is no child. and this relation is made inside the parent class, unlike the aggregation we make relations outside the class.


# ----------- Classes Understanding deep -----------
# object → the root parent class of all classes.
# type → the class of all classes (meta-class).
# Classes are objects of type.
# Instances are objects created via object.



# Classes → created by type class ( meta class in python implicitly calls it)
# Objects (instances) → created using the object base class ( parent class implicity calls object class to create objects )

# object  → the root of all instances
# type    → the root of all classes



#         type        ( instance of itself)
#          ↑
#          |
#        object       print(type(object))  # <class 'type'>
#          ↑
#          |
#    MyClass (class)  print(type(MyClass))  # <class 'type'>
#          ↑
#          |
#    obj = MyClass()   (instance)

# And type itself is both a class and an object (self-referential).



# Now — in CPython (the default Python implementation), these two are not written in Python but in C. However, Python exposes them so you can inspect and use them. Let me show you how they look conceptually.

# class object:
#     def __new__(cls, *args, **kwargs):
#         # allocates memory for a new instance
        # comes from type class allocate memory and create the ob
#         ...

#     def __init__(self):
#         # default initializer (does nothing)
#         return None

#     def __str__(self):
#         # default string representation
#         return f"<{self.__class__.__name__} object>"

#     def __repr__(self):
#         return self.__str__()
# all special methods comes from this class




# class type(object):
#     def __new__(cls, name, bases, namespace):
#         # creates a new class
#         # name = class name
#         # bases = tuple of parent classes
#         # namespace = dict of attributes/methods
#         ...

#     def __call__(self, *args, **kwargs):
#         # when you "call" a class (MyClass()), this runs
#         # it creates an instance by calling __new__ and __init__
#         ...


# When you do class MyClass: ..., Python internally calls type("MyClass", (object,), {...}) to build it.


# When you call your class, Python triggers type.__call__.
# Inside __call__, it uses object.__new__ (from the base object class) to allocate the raw object in memory, unless you define your own __new__.
# Then it calls your __init__ to initialize.


# ------------ More Deep understanding ----------------
# Normal objects (like 10, "hello") are from their respective classes (int, str).
# Those classes (int, str) are from the metaclass type.

# So everything in python is objects which is in the meta class "type" class

# Actually object class subclass hai type class

# type ── creates ──> classes (including object)
#  ↑                     ↓
#  └───────────── object <──

# type khud apni hi instance hai.







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

    
 
