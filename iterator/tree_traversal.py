class Node:
    def __init__(self, value, left = None, right = None):
        self.right = right 
        self.left = left 
        self.value = value 
        
        self.parent = None 
        
        if left:
            self.left.parent = self
        
        if right:
            self.right.parent = self
        
    def __iter__(self):
        return InOrderIterator(self)

class InOrderIterator:
    def __init__(self, root):
        pass 
    
    def __next__(self):
        if not self.yielded_start:
            self.yielded_start = True 
            return self.current 

        if self.cu
if __name__ == "__main__":
    
    
        