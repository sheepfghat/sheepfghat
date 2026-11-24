#7 лекция
#Classy Extensions
from preloaded import Animal

class Cat(Animal):
    def speak (self):
        return self.name + " meows."
#Color Ghost
import random
class Ghost(object):
    def __init__(self):
        self.color=random.choice(["white","yellow","purple","red"])
#Basic subclasses - Adam and Eve
class Human: pass
class Man(Human): pass
class Woman(Human): pass

def God():
    return [Man(), Woman()]
