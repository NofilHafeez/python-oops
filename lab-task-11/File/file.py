# Approach 1 (in-place copy) → modifies the same object (self).
# Approach 2 (hard-coded class) → returns new File object, but inflexible for subclasses.
# Approach 3 (cls param) → returns new object, flexible but requires passing cls.
# Best practice → self.__class__, because it returns a new object of the same class without extra params.


# When you would need deepCopy
# Only if your class has mutable attributes (list, dict, set, custom objects).
# Then you’d duplicate them to avoid shared references.

class File:
    def __init__(self, fileName, fileSize):
        self.fileName = fileName
        self.fileSize =fileSize

    def __getFileName__(self):
        return self.fileName
    
    def __getFileSize__(self):
        return self.fileSize
    
    def shalowCopy(self, obj):
            #shallow
            self.fileName = obj.fileName
            self.fileSize = obj.fileSize

    
    def deepCopy(self, obj):
         self.fileName = str(obj.fileName) 
         self.fileSize = int(obj.fileSize)
         

    def shalowCopy1(self, obj):
        #shallow
        return File(obj.fileName, obj.fileSize)

    
    def deepCopy1(self, obj):
         return File( str(obj.fileName) ,int(obj.fileSize))
         

    def shalowCopy2(self, obj, cls):
        #shallow
        return cls(obj.fileName, obj.fileSize)

    
    def deepCopy2(self, obj, cls):
        return cls( str(obj.fileName) ,int(obj.fileSize))
    

    def shallowCopy3(self):
        return self.__class__(self.fileName, self.fileSize)

    # if out obj contains mutable types then add deepcopy
    # def deepCopy3(self):
    #     return self.__class__(str(self.fileName), int(self.fileSize))
    
#     Both are possible, but they solve different problems:
# In-place copy (overwrite self) → f1.copyFrom(f2) - ( equality one)
# "Make me look like f2."
# Useful when you don’t want to create a new object, just reuse the existing one.
# Return new copy object → f2 = f1.copy() ( return its obj and we can palce to other obj)
# "Give me a new object just like me."
# This is more common (and what Python’s copy module does).



    def __str__(self):
         return f'{self.fileName, self.fileSize}'
         



