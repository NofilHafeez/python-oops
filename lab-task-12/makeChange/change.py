from makeChange.CounterMachine.machine import CounterMachine
class MakeChange:
    def __init__(self,amountCharged=None, amountGiven=None, obj=None, aggregate_obj=None):
        if obj is not None:
            # Association: donst keep a reference
            self.amountCharged = obj.amountCharged
            self.amountGiven = obj.amountGiven
        elif aggregate_obj is not None:
            # Aggregation: keep a reference, but don’t control its lifetime
            self.aggregate_obj = aggregate_obj
            self.amountCharged = aggregate_obj.amountCharged
            self.amountGiven = aggregate_obj.amountGiven
        else:
            # Composition
            self.obj = CounterMachine(amountCharged, amountGiven)
            self.amountCharged = self.obj.amountCharged
            self.amountGiven  = self.obj.amountGiven
        
        
    # @staticmethod
    def makeChange(self):
        change = self.amountGiven - self.amountCharged
        money = [5000, 1000, 500, 100, 50, 20, 10, 5, 2, 1]
        result = {}

        # for i in money:
        #     if len(str(i)) == len(str(change)):
        #         count = change // i
        #         print(count)
        #         if count > 0:
        #             result[i] = count
        #             # print(change)
        #             change = change % i
        #             # print(change)

        for i in money:
            while len(str(i)) == len(str(change)) and change >= i:
                change -= i
                result[i] = result.get(i, 0) + 1 

        return result
        

#First time we subtract 100:
# result.get(100, 0) → since 100 not in result, it returns 0.
# 0 + 1 = 1
# Store: result[100] = 1
# Second subtraction (350 → 250):
# result.get(100, 0) → now returns 1.
# 1 + 1 = 2
# Store: result[100] = 2
# Third subtraction (250 → 150):
# result.get(100, 0) → returns 2.
# 2 + 1 = 3
# Store: result[100] = 3
# Fourth subtraction (150 → 50):
# result.get(100, 0) → returns 3.
# 3 + 1 = 4
# Store: result[100] = 4
# Now result = {100: 4}




                    


                
#    m = 5000 → len(str(m)) = 4. Compare 4 == 3 → false → skip.
# m = 1000 → len = 4. 4 == 3 → false → skip.
# m = 500 → len = 3. 3 == 3 → true.
# count = 450 // 500 = 0 → count > 0? no → nothing stored, change remains 450.
# m = 100 → len = 3. 3 == 3 → true.
# count = 450 // 100 = 4 → store result[100] = 4.
# change = 450 % 100 = 50. Now len(str(change)) = 2.
# m = 50 → len = 2. 2 == 2 → true.
# count = 50 // 50 = 1 → store result[50] = 1.
# change = 50 % 50 = 0. Now len(str(change)) = 1 ("0" has length 1).
# Remaining denominations run, but change is 0 so any counts will be 0 and nothing else is added.
# Return: {100: 4, 50: 1}