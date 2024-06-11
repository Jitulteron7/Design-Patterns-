from typing import List, Optional
class Person:
    def __init__(self, name):
        self.name = name
        self.chat_log = []
        self.room:Optional[ChatRoom] = None 
    
    def receive(self, sender:str, message: str):
        s = f'{sender}: {message}'
        print(f'[{self.name}\'s chat session] {s}')
        self.chat_log.append(s)
    
    def say(self, message):
        self.room.broadcast(self.name, message)
    
    def private_message(self, who, message):
        self.room.message(self.name, who, message)

# Mediator
class  ChatRoom:
    def __init__(self):
        self.people:List[Person] = []
    
    def broadcast(self, src: str, msg: str):
        for p in self.people:
            if p.name != src:
                p.receive(src, msg)
    
    def join(self, person:Person):
        join_msg = f'{person.name} joins the chat'
        self.broadcast('room', join_msg)
        person.room = self
        self.people.append(person)
    
    def message(self, src: str, destination: str, msg: str):
        for p in self.people:
            if p.name == destination:
                p.receive(src, msg)



if __name__ == '__main__':
    room = ChatRoom()
    john = Person('John')
    jane = Person('Jane')
    
    room.join(john)
    room.join(jane)
    
    john.say('Hi room')
    jane.say('Oh, Hey john')
    
    simon = Person('simon')
    room.join(simon)
    
    simon.say('Hi everyone')
    
    jane.private_message(simon.name,'Hello Simon')
    
    
    
        