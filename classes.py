#class example
'''
class Dog():
  def __init__(self, name, age=0):
    self.name = name
    self.age = age

  def bark(self):
    print(f'{self.name} says woof!')

'''

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
    
car = Vehicle('TS123', 'Tesla', 'Model S')
print(car.running) # -> False
car.start()
print(car.running) # -> True
plane = Vehicle('X99Y', 'Boeing', '747-B')
print(plane.vin, plane.make, plane.model)


