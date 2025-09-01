class Words:
    def __init__(self, words):
        self.words = list(words)

    def __len__(self):
        return len(self.words)
    
    def count_words(self):
        count = 0
        self.validate_type()
        self.validate_space()
        try:
            for i in range(len(self.words)):
                for j in range(i + 1, len(self.words)):
                    if self.words[i] == self.words[j]:
                        count += 1
            return count     
        except ValueError as ve:
            print(ve)
            return 0


    def validate_space(self):
        for word in self.words:
            if ' ' in word:
                raise ValueError("Words should not contain spaces")

    def validate_type(self):
       if not isinstance(self.words, list):
        raise TypeError("Expected a list")
     # if one element is false it will return false in all()
       if not all(isinstance(x, str) for x in self.words): # all([True, True, True])   # True
                                                           # all([True, False, True])  # False

        raise ValueError("All elements must be strings")

       return True
