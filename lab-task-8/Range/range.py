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


   @property
   def start(self): return self._start
   @property
   def stop(self): return self._stop
   @property
   def step(self): return self._step

   def get_len(self):
      return self._length

   def get_item(self, k):
        #  Return entry at index k (using standard interpretation if negative).
     if k < 0:
        k += len(self) # attempt to convert negative index

     if not 0 <= k < self._length:
        raise IndexError( "index out of range" )
     return self._start + k * self._step


   def __iter__(self):
        # Allow iteration over the Range.
        for i in range(len(self)):
            yield self[i] 
   

   def __repr__(self):
        return f"Range({self._start}, {self._stop}, {self._step})"
   
   def __str__(self):
        return f"Range({self._start}, {self._stop}, {self._step})"