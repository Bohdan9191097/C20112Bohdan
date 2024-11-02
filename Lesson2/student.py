class Student:
    def  __init__(self, name:str = "Test", age: float = 0.0, gender: bool = False):
        self.Name = name
        self.Age = age
        self.Gender = gender
    def earnMoney(self):
        for i in range(365):
            if(i > 150 and i < 240):
                print(i)