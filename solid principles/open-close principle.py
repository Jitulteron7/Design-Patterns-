from enum import Enum
from typing import List

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3 

class Size(Enum):
    SMALL = 1
    MEDIUM = 2 
    LARGE = 3

class Product:
    def __init__(self,name,color,size):
        self.size = size
        self.name = name
        self.color = color

class ProductFilter:
    def filter_by_color(self,products:List[Product],color:Color):
        for p in products:
            if p.color==color:
                yield p 
            
            
    def filter_by_size(self,products:List[Product],size:Size):
        for p in products:
            if p.size == size:
                yield p
    
    def filter_by_size_and_color(self,products:List[Product],size:Size,color:Color):
        for p in products:
            if p.size == size and p.color ==color:
                yield p
    
    # as we keep on growing the filter categories we have to modify the Class ProductFilter again and again


# Enterprice patterns: Specification

class Specification:
    def is_satisfied(self,items):
        pass 
    def __and__(self,other):
        return AndSpecification(self,other)
    
class Filter:
    def filter(self,items,spec):
        pass 

class ColorSpecification(Specification):
    def __init__(self,color):
        self.color = color 
        
    def is_satisfied(self,item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self,size):
        self.size = size 
        
    def is_satisfied(self,item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self,spec1,spec2):
        self.spec1 = spec1
        self.spec2 = spec2
        
    def is_satisfied(self, item):
        return self.spec1.is_satisfied(item) and  self.spec2.is_satisfied(item)
            
    
class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item 



apple = Product("Apple",Color.GREEN,Size.SMALL)
tree = Product("Tree",Color.GREEN,Size.LARGE)
house = Product("House",Color.BLUE,Size.LARGE)

products = [apple,tree,house]

#  old way of filtering 
# pf = ProductFilter()

# for p in pf.filter_by_color(products,Color.GREEN):
#     print(f' - {p.name} is green')


# better way of filtering 

pf = BetterFilter()

color_green = ColorSpecification(Color.GREEN)
for p in pf.filter(products,color_green):
    print(f' - {p.name} is green')

size_large = SizeSpecification(Size.LARGE)
for p in pf.filter(products,size_large):
    print(f' - {p.name} is large')
    
# large_and_green = AndSpecification(color_green,size_large)
large_and_green = color_green and size_large #syntax suger implementation
for p in pf.filter(products,large_and_green):
    print(f' - {p.name} is large and green')
    

