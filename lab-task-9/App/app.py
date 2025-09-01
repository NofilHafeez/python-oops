from birthdayParadox.birthday import BirthdayPara
from Words.words import Words

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








