import random
class CharPermuter:
    def __init__(self, chars):
        if isinstance(chars, str):
            self.possible_chars = list(chars)
        else:
            self.possible_chars = chars

    def check(self):
        results = []
        permutation = self.__factorial__(len(self.possible_chars))# 6! = 720
        for i in range(permutation):
            string = ''.join(random.sample(self.possible_chars, len(self.possible_chars)))
            if string not in results:
                results.append(string)
        return results
    
    def __factorial__(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.__factorial__(n - 1) # recursive call
        
        
    
                    
                    
