from SimpleCalculator.calculator import SimpleCalculator
class HandHeldInterface:
   def __init__(self):
       self.calculator = SimpleCalculator()

   def interface(self):
       while True:
            cmd = input("Command: ").lower()
            if cmd == "quit":
                break
            if cmd == "start":
                num1 = float(input("Enter first number: "))
                op = input("Enter operator (+, -, *, /): ")
                num2 = float(input("Enter second number: "))

                if op == "+":
                    print("Result:", self.calculator.add(num1, num2))
                elif op == "-":
                    print("Result:", self.calculator.subtract(num1, num2))
                elif op == "*":
                    print("Result:", self.calculator.multiply(num1, num2))
                elif op == "/":
                    print("Result:", self.calculator.divide(num1, num2))
                else:
                    print("Invalid operator!")