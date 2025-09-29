class CounterMachine:
    def __init__(self, amountCharged, amountGiven):
        self.amountCharged = amountCharged
        self.amountGiven = amountGiven

    @property
    def giveAmount(self): return self.amountGiven
    
    @property
    def chargeAmount(self): return self.amountCharged

        