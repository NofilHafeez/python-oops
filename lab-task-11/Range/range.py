class Range:
    def __init__(self, start, stop=None, step=1):
        if step == 0:
            raise ValueError("cannot be zero")
        
        if stop is None:
            start, stop = 0, start

        self.start = start
        self.stop = stop
        self.step = step

        ## self.length becoming zero when step < 0 and step > 0
        # so we take abs values
        if (step > 0 and start >= stop ) or (step < 0 and start <= stop):
            self.length = 0
        else:
            self.length = ((abs(stop - start) + abs(step) - 1) // abs(step))

    

    def __len__(self):
        return self.length

    def __getitem__(self, k):
        if k < 0 :
            k += len(self)
            # k = -1 + 2 = 1
            # k = -1 + 4 = 3
            # k = -2 + 5 = 3 

        if not 0 <= k < self.length: # if not less then length and greater then zero k out of range
            raise IndexError("out of range")

        return self.start + k * self.step
                # 3 + 1 * 2 = 8
                # 4 + 1 * 2 = 10
                # 5 + 1 * 2 = 12


# better approach and simple and concise. (Ai suggestion)

# def __iter__(self):
#     i = 0
#     while i < len(self):
#         yield self[i]
#         i += 1



#A function with yield automatically becomes a generator.
#A generator object implements both __iter__ and __next__ internally.
#That’s why for worked without you writing __next__.
        
    # good if you want more control of what you doing.
    def __iter__(self): 
        # reset index whenever new iteration starts
        self._index = 0
        return self # returns the object

    def __next__(self): # Each time the for loop needs a new value, it calls your __next__.
        if self._index >= self.length:
            raise StopIteration
        value = self[self._index]
        self._index += 1
        return value
    
#     Execution trace for Range(0, 10, 2)
# __iter__ → resets _index = 0.
# next(it) → calls __next__: returns 0.
# next(it) → returns 2.
# next(it) → returns 4.
# next(it) → returns 6.
# next(it) → returns 8.
# next(it) → raises StopIteration. Loop ends.
    
    
        
    def __repr__(self):
        return f"Range({self.start}, {self.stop}, {self.step})"
