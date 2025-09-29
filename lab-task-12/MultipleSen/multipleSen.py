import random
class MultipleSen:
    def __init__(self, sentences):
        self.sentences = sentences
        self.__random_typos = list("abcdefghijklmnopqrstuvwxyz.!?")  # shorter way

    def multiple_sentences(self, n):
        results = []
        for _ in range(n):
            random1 = random.choice(self.__random_typos)
            pos = random.randint(0, len(self.sentences) - 1)
            sentences = str(self.sentences)
            
            sentences = sentences[:pos] + random1 + sentences[pos:]
            results.append(sentences)       
        return results
    