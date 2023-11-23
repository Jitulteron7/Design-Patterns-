import abc 
# abstract calss : class that has one or more then one absract method 
# abstract method: method inside a class that is defined but not implemented 
# interface: abstract class where all the methods are abstract method (in python we dont have interface like java or js)

# informal interface: 
# An informal Python interface is a class that defines overridable methods with no tight enforcement. An informal interface, commonly known as Protocols or Duck Typing. So, if an object can fly and quack like a duck, we classify it as a duck. This is known as "Duck Typing." We depend on duck typing to let users know that they are using an interface and should treat it as such.
# note: duck type : 
#  a type used in dynamic programming language. it means that instead replying on the explicit type or class, duck type foucs on 
# whether an objet can perform certain actions or has certain properties.  
# eg for informal interface:

# class InformalInterface:
#     def load_data(self):
#         """Load in the file for extracting text"""
#         pass 
# class PdfReader(InformalInterface):
#     pass 

# p = PdfReader()
    
# print(issubclass(PdfReader,InformalInterface))
# print(isinstance(p,InformalInterface))
# result is true which pdfrender class did not implemented the load_data and no error was thrown
    

# formal interface: 
#  an interface which give strict restriction 
# can be implemented by:
# 1: using Abstract base class 
class FormalInterface(abc.ABC):
    @abc.abstractmethod
    def load_data(self):
        """Load in the file for extracting text"""
        pass 
class PdfReader(FormalInterface):
        pass
# error will be thrown
# p = PdfReader()


# 2: Registering virtual subclass using ABC
class Bird(abc.ABC):
    @abc.abstractmethod
    def fly(self):
        pass

@Bird.register
class Robin:
    pass

r = Robin()
#Check if Robin class is a sublass of Bird class
print(issubclass(Robin, Bird))
#Check if r, obj of Robin class is a sublass of Bird class
print(isinstance(r, Bird))
# 3: ABCs and multiple inheritance
import abc

class Boat(abc.ABC):
    @abc.abstractmethod
    def swim(self):
        pass
    
class Gale(Boat):
    def swim(self):
        print("swimming")

g = Gale()
isinstance(g, Boat)

class Fish(abc.ABC):
    @abc.abstractmethod
    def swim(self):
        pass


class tuna(Fish):
    def swim(self):
        print("swimming!")

t = tuna()

#Check if t, obj of tuna class is a sublass of Boat class
print(isinstance(t, Boat))
#Check if G, obj of Gail class is a sublass of Fish class
print(isinstance(g, Fish))


# 4: Inerface declaration: "zope.interface" (read)

# print(p)
# resource: https://www.scaler.com/topics/interface-in-python/ 
    
        
     