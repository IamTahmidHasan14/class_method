class Profile:
  location = "Rajshahi"

  def details(self):
    print(f"My name is {self.name}, I lives in {self.location}")

  @classmethod  #by adding this, it also change class variables
  def change(cls, newlocation):
    cls.location = newlocation


p = Profile()
p.name = "Tahmid"
p.details()
p.change("Bangladesh")
p.details()
print(Profile.location)