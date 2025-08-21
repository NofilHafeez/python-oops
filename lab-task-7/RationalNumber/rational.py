class Rational:
    def __init__(self, num, deno):
        self.num = num
        self.deno = deno

    @property
    def numerator(self):
        return self.num
    
    @numerator.setter
    def numerator(self, new):
        self.num = new

    @property
    def denominator(self):
        return self.num
    
    @denominator.setter
    def denominator(self, new):
        self.num = new

    def __add__(self, other):
        num = (self.num * other.deno) + (other.num * other.deno)
        deno = self.deno * other.deno
        return Rational(num, deno)
    
    def __sub__(self, other):
        num = (self.num * other.deno) - (other.num * other.deno)
        deno = self.deno * other.deno
        return Rational(num, deno)
    
    def __mul__(self, other):
        num  = self.num * other.num  
        deno = self.deno * other.deno
        return Rational(num, deno)
    
    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError("Denominator Cannot Be Zero")
        num  = self.num * other.deno  
        deno = self.deno * other.num
        return Rational(num, deno)
    
    def __str__(self):
        return f"{self.num}/{self.deno}"