import random
class MultipleSen:
    def __init__(self, sentences):
        self.sentences = sentences
        self.random_typos = list("abcdefghijklmnopqrstuvwxyz.!?")  # shorter way

    def multiple_sentences(self, n):
        results = []
        for i in range(n):
            random1 = random.choice(self.random_typos)
            pos = random.randint(0, len(self.sentences) - 1)
            
            self.sentences = self.sentences[:pos] + random1 + self.sentences[pos:]
            results.append(self.sentences)  
        return results
    