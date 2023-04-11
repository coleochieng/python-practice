#example from lesson

class Dog():
  #class attribute
  next_id = 1

  #updated __init__
  def __init__(self, name, age=0):
    self.name = name
    self.age = age
    self.id = Dog.next_id
    Dog.next_id += 1

  def bark(self):
    print(f'{self.name} says woof!')

  #updated __str__
  def __str__(self):
    return f"Dog {self.id} named {self.name} is {self.age} years old" 

'''
spot = Dog('Spot', 8)
print(spot)
pup = Dog('Lassie')
print(pup)
'''

def ShowDog(Dog):
   def __init___(self, name, age=0, total_earnings=0):
      Dog.__init__(self, name, age)
      self.total_earnings = total_earnings

  





#practice
class Vehicle():
    def __init__(self, vin, make, model, running=False):
        self.vin = vin
        self.make = make
        self.model = model
        self.running = running
    def start(self):
        self.running = True
        return self.running
    def stop(self):
        self.running = False
        return self.running
    def __str__(self):
        return f"Vehicle {self.vin} is a {self.make} model {self.model}"

'''    
car = Vehicle('TS123', 'Tesla', 'Model S')
print(car.running) # -> False
car.start()
print(car.running) # -> True
plane = Vehicle('X99Y', 'Boeing', '747-B')
print(plane.vin, plane.make, plane.model)
print(car)
'''

