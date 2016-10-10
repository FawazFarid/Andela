class Car(object):
  
  
  def __init__(self, name = "General", model = "GM" , *car_type):
      
    self.num_of_doors = 4 if not(name =='Porshe' or name == 'Koenigsegg') else 2
    self.num_of_wheels = 8 if 'trailer' in car_type else 4
    self.speed = 0
    self.name = name
    self.model = model
    self.car_type = car_type


  def drive(self, knot):
    if self.is_saloon():
      self.speed = 10**knot
    else:
      self.speed = knot*11
    return self

  def is_saloon(self):
    return "trailer" not in self.car_type