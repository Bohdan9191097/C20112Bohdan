from human import Human
from student import Student
from worker import Worker
from human import Human


prymenko = Worker("Andrii")
kapitanskiy = Student("Roman")
print(str(prymenko))
print(str(kapitanskiy))
defaultHuman = Human()
print(defaultHuman.greeting)
print(defaultHuman._greeting)
print(str(defaultHuman))