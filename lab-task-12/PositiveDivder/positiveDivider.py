class PositiveDivider:
    def __init__(self, number):
        self.number = number 

    def divide(self):
        if  self.number < 2 or self.number <= 0:
            raise ValueError("Number must be greater than 2 ans should be positive")
        
        count = 0
        results = []
        new = self.number

        while new > 2:
            new = new / 2
            if not new < 2:
                results.append(new)
                count += 1
        return results 