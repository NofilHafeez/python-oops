from credit import Credit
class List: 
    def __init__(self, ):
        self.list = []

    def append(self, object):
        self.list += [object]

    def remove(self, object: Credit):
        k = 0
        for i in range(len(self.list)):
            if (self.list[i].balance != object.balance):
                self.list[k] = self.list[i] # copy items
                k += 1
            
        # len(self.list) = k wrong  
        self.list = self.list[:k] # Ai arr = [10, 20, 30, 40, 50] k = 3 arr = arr[:k]   #arr = arr[0:3] , arr = [10, 20, 30]Ans

        return k

    def __len__(self):
        return len(self.list)
    
    # def __str__(self):
    #     return print(slef.list)