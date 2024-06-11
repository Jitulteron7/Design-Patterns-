from typing import Any


class Event(list):
    def __call__(self, *args: Any, **kwargs: Any):
        for item in self:
            item(*args, **kwargs)
    

class Game:
    def __init__(self):
        self.events = Event()

    def fire(self, args):
        self.events(args)

class GoalScoredInfo:
    def __init__(self, who_scored, goals_scored):
        self.goals_scored = goals_scored
        self.who_scored = who_scored
    
class Player:
    def __init__(self):
        pass 
    
    