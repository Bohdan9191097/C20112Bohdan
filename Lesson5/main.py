import requests
'''
payload = {
    'group' : 'S20112'
}
response = requests.post('https://httpbin.org/post', payload)
if(response.status_code == 200):
    print(response.status_code)
    print(response.content)
    print(response.text)
'''

class Car:
    def __init__(self, brand):
        self.Brand = brand
class BMW(Car):
    def __init__(self, brand):
        super().__init__( brand)
class Animal:
    def __init__(self, breed):
        self.Breed = breed
bmw = BMW('BMW')
animal = Animal('Pig')
print(isinstance(bmw, BMW))
print(isinstance(bmw, Car))
print(isinstance(animal, Animal))
print(isinstance(animal, Car))

brand = 'Brand'
breed = 'Breed'
print(hasattr(bmw, brand))
print(hasattr(bmw, breed))
print(hasattr(animal, brand))
print(hasattr(animal, breed))
print(getattr(bmw, brand))