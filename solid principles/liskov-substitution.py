class Rectanlge:
    def __init__(self,width,height):
        self._height = height
        self._width = width 
    
    @property
    def area(self):
        return self._width * self._height
    
    def __str__(self):
        return f'Width: {self.width}, Height: {self.height}'
    
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,val):
        self._width = val
        
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,val):
        self._height = val

def use_it(rc):
    w = rc.width
    print("current w",rc.width)
    rc.height = 10 
    print("new w",rc.width)
    expected = int(w*10)
    
    print(f'Expeceeted an area of :{expected}, got {rc.area}')
        
class Square(Rectanlge):
    def __init__(self, size):
        Rectanlge.__init__(self,size,size)
    
    @Rectanlge.width.setter
    def width(self,val):
        self._width = self._height = val 
    
    @Rectanlge.height.setter
    def height(self,val):
        self._width = self._height = val 

rec = Rectanlge(2,3)
sq = Square(2)
# use_it(rec)
use_it(sq)

# fixing this totally depend on your own solution
# omitting the getter and setter will or we can have if else statment to check if it is square or not
    
        

        