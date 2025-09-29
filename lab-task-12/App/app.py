from birthdayParadox.birthday import BirthdayPara
from Words.words import Words
from CharPermuter.charPermuter import CharPermuter
from PositiveDivder.positiveDivider import PositiveDivider
from SimpleCalculator.calculator import SimpleCalculator
from MultipleSen.multipleSen import MultipleSen

class App:
    def run(self):
        n = 23
        b = BirthdayPara(n)
        print(f"Probability of {n} people having same birthday is: {b.get_probability(n)}")
        print(f"Stimulation: {b.simulate(n)}")


        words = ["apple", "banana", "orange", "apple", "kiwi", "banana"]
        w = Words(words)
        print(f"Number of words: {len(w)}")
        print(f"Number of duplicate words: {w.count_words()}")

        check = CharPermuter( ["c", "a", "t", "d", "o", "g"])
        ans = check.check()
        print(ans)

        divider = PositiveDivider(10)
        # print(divider.divide())

        calculator = SimpleCalculator()
        # a = input("Enter first number: ")
        # b = input("Enter second number: ")
        # addition = input("add the numbers (+): ")
        # if addition.lower() == '+':
        #     calculator.add(int(a), int(b))
        #     print(f"Addition: {calculator.add(int(a), int(b))}")

        # subtraction = input("subtract the numbers (-): ")
        # if subtraction.lower() == '-':
        #     calculator.subtract(int(a), int(b))
        #     print(f"Subtraction: {calculator.subtract(int(a), int(b))}")


        # handheld calculator
        # while True:
        #     cmd = input("Command: ").lower()
        #     if cmd == "quit":
        #         break
        #     if cmd == "start":
        #         num1 = float(input("Enter first number: "))
        #         op = input("Enter operator (+, -, *, /): ")
        #         num2 = float(input("Enter second number: "))

        #         if op == "+":
        #             print("Result:", calculator.add(num1, num2))
        #         elif op == "-":
        #             print("Result:", calculator.subtract(num1, num2))
        #         elif op == "*":
        #             print("Result:", calculator.multiply(num1, num2))
        #         elif op == "/":
        #             print("Result:", calculator.divide(num1, num2))
        #         else:
        #             print("Invalid operator!")


        obj =  MultipleSen("This is a sample sentence.")
        print(obj.multiple_sentences(3))



