class Student:
    def __init__(self, name: str = "Test", age: float = 0.0, gender: bool = False, money: float = 0.0):
        self.Name = name
        self.Age = age
        self.Gender = gender
        self.Money = money
        self.Studying = False

    def earnMoney(self):
        for i in range(365):
            if 150 < i < 240:
                self.Money += 50
                print(f"Day {i}: Earned money. Current balance: ${self.Money}")

    def spendMoney(self):
        for i in range(365):
            if i % 30 == 0:
                self.Money -= 100
                print(f"Day {i}: Spent money on necessities. Current balance: ${self.Money}")

    def study(self):
        for i in range(365):
            if i % 15 == 0:
                self.Studying = True
                print(f"Day {i}: Started studying.")

    def liveYear(self):
        for day in range(365):
            if self.Money < 200:
                self.earnMoney()
            if self.Money >= 500:
                self.study()
            self.spendMoney()

student = Student(name="Alex", age=20, gender=True, money=100.0)
student.liveYear()
