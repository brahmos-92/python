### Array implementation to store the DVD's ###
class Dvd:
   def __init__(self,name,releaseYear,director) -> None:
       self.name = name
       self.releaseYear = releaseYear
       self.director = director

   def __str__(self):
     return f"{self.name} {self.releaseYear}  {self.director}."

   def __repr__(self):
     return f"{self.name} {self.releaseYear}  {self.director}. Surprise!"
       
dvdcollections =[]
d1 = Dvd("daud",1993, "asd")
dvdcollections.append(d1)
print(dvdcollections)


import datetime
today = datetime.date.today()
print(str(today))
print(repr(today))