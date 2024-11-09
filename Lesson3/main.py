from Lesson3.car import Car
from Lesson3.person import Person
python1 = Car('Python1')
python1.add_driver(Person('Kapitanskiy'))
python1.add_passenger(Person('Polischtschuk'))
python1.add_passenger(Person('Oborskyi'))
python1.add_passenger(Person('Andriienko'))
python1.add_passenger(Person('Kiselow'))
print(python1)