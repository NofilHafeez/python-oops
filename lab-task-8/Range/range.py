class Range:
   def __init__ (self, start, stop=None, step=1):
     if step == 0:
        raise ValueError( 'step cannot be 0')

     if stop is None: # special case of range(n)
        start, stop = 0, start # should be treated as if range(0,n)

     if (not isinstance(start, int) or  not isinstance(step, int) or not isinstance(stop, int)):
        return ValueError("not integer type")
        
     self._length = max(0, (stop - start + step - 1) // step)
     self._start = start
     self._step = step
     self._stop = stop


   @property
   def start(self): return self._start
   @property
   def stop(self): return self._stop
   @property
   def step(self): return self._step

   def __len__(self):
      return self._length

   def __getitem__(self, k):
        #  Return entry at index k (using standard interpretation if negative).
     if k < 0:
        k += len(self) # attempt to convert negative index

     if not 0 <= k < self._length:
        raise IndexError( "index out of range" )
     return self._start + k * self._step


   def __iter__(self):
    i = 0
    while i < len(self):
        yield self[i] # use __getitem__ to access element
        i += 1

   

   def __repr__(self):
        return f"Range({self._start}, {self._stop}, {self._step})"
   
   def __str__(self):
        return f"Range({self._start}, {self._stop}, {self._step})"