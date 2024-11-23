from collections.abc import Generator

from Lesson2.student import Student

students = ["Student1","Student2","Student3","Student4"]
#print(isinstance(students, Iterable))
#print(isinstance(2, Iterable))
#1
'''
for item in students:
    print(item)
i=0
while i < len(students):
    print(students[i])
    i += 1
'''
#2
'''
while True:
    print(next(students))
'''
'''
#2.1
iter_students = iter(students)
while True:
    try:
        print(next(iter_students))
    except StopIteration:
        break
print("Hello World 1")
while True:
    try:
        print(next(iter_students))
    except StopIteration:
        break
print("Hello World 2")
'''
'''
#3 counter
from counter import *
counter = Counter(0,20)
while True:
    try:
        print(next(counter))
    except StopIteration:
        break
print("Hello Counter")
'''
from generator import Generator
generator = Generator(students)
for i in generator.GetStudent():
    try:
        print(i)
    except TypeError:
        break