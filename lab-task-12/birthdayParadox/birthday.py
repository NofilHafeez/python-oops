import math
from random import randint

class BirthdayPara: 
    def __init__(self, n, d=365): 
        self.n = n 
        self.d = d

    # theoretical probability
    def do_permutation(self, n,): 
        # equivalent to n =  1,2,3,4,5 = (361 - 4) * (362 - 3) * (363 - 2) * (364 - 1) * 365
        try:
            r = n
            Vrn =  format(math.factorial(self.d) / math.factorial((self.d - r)))
            Vt = format(math.pow(self.d, r))
            P = float(Vrn) / float(Vt)
            return P
        except ValueError:
            return 0.0

    def get_probability(self, n):
        if n < 0 or n == 0:
            raise ValueError("should be positive and greater then zero")
        result = 1.0 - self.do_permutation(n)
        return result

    # experimental probability
    def simulate(self, n, trials=10000):
        if n < 0 or n == 0:
            raise ValueError("should be positive and greater then zero")
        # added 10000 trials to check the probability, more the trials more accurate the result
        try:
            successes = 0
            for _ in range(trials):
                # adding random birthdays - length will be n of the array
                birthdays = [randint(0, self.d - 1) for _ in range(n)]
                if len(set(birthdays)) < n:   # duplicate exists and removing
                    successes += 1
            return successes / trials
        except ZeroDivisionError:
            return 0.0
    

    def __str__(self):
        return f"BirthdayParadox(n={self.n}, d={self.d})"
    
    def __repr__(self):
        return f"BirthdayParadox(n={self.n}, d={self.d})"
    

# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 
#  n =  5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100

#   Vnr() =  n! / (n - r)!
#   Vr(total number of k people can have birthday) = 365^23 = 365 * 365 * 365 * ....(23 times)