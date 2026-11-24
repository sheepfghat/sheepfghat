#6 лекция
#Playing with cubes II
class Cube(object):
    
    def __init__(self,side=0):
        self.__side=abs(side)
        
    def get_side(self):
        """Return the side of the Cube"""
        return self.__side

    def set_side(self, new_side):
        """Set the value of the Cube's side."""
        self.__side = abs(new_side)
#Refactored Greeting
class Person(object):
    def __init__(self,name):
        self.name=name

    def greet(self, your_name):
        return "Hello %s, my name is %s" % (your_name, self.name)
#Finish Guess the Number Game
class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives
  
    def guess(self,n):
        if self.lives<=0:
            raise Exception('No more lives')
        if n==self.number:
            return True
        self.lives-=1
        return False
#Santa'sNaughty List
def find_children(santas_list, children):
    return sorted(set(santas_list) & set(children))