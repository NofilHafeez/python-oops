from birthdayParadox.birthday import BirthdayPara
from Words.words import Words
from CharPermuter.charPermuter import CharPermuter
from PositiveDivder.positiveDivider import PositiveDivider
from SimpleCalculator.calculator import SimpleCalculator
from MultipleSen.multipleSen import MultipleSen
from SimpleCalculator.handheld import HandHeldInterface

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
        interface = HandHeldInterface()
        interface.interface()

        obj =  MultipleSen("This is a sample sentence.")
        print(obj.multiple_sentences(3))



