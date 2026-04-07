# Multiple Inheritance and interface and mixins
# Python supports multiple inheitance 
class Duck:
  def walk(self):
    print("waddle")
    
class Trombonist:
  def noise(self):
    print("blat!")
class DuckBonist(Duck, Trombonist): # this child inherits all features of the parent 
  pass
db = DuckBonist()
db.walk()
# the other use of multiple inherintance is to define mixin classes:
# mixin classes is class the extends the functionality of other class
class Duck:
  def noise(self):
    return "quack"
  def waddle(self):
    return "Waddle"
  
class Trombonist:
  def noise(self):
    print("blat!")

class Cyclist:
  def noise(self):
    return "On your left"
  def pedal(self):
    return "Pedaling"
class Car:
    def noise(self):
        return "vroom"  
# all of these classess are completely unrelated meaning they implement diffent methods
# they share one thing which is noise() method
class LoudMixin:
  def noise(self):
    return super().noise().upper()
class AnnoyingMixin:
  def noise(self):
    return  3*super().noise()

class LoudDuck(LoudMixin, Duck):
  pass

class AnnoyingCyclist(AnnoyingMixin, Cyclist):
    pass

class ReallyAnnoyingDuck(AnnoyingMixin, LoudMixin, Duck):
    pass
class LoudCar(LoudMixin, Car): pass

print(LoudDuck().noise())           # "QUACK"
print(AnnoyingCyclist().noise())    # "On your leftOn your leftOn your left"
print(ReallyAnnoyingDuck().noise()) # "QUACKQUACKQUACK"
print(LoudCar().noise()) 