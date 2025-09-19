class Credit:
    def __init__(self, cardName, bankNo, cardHolder, balance):
        self.cardName = cardName
        self.bankNo = bankNo
        self.cardHolder = cardHolder
        self.balance = balance

    def get_balance(self):
        return self.balance
