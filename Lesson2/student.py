import random


class Student:
    def __init__(self, name: str = "Test", age: float = 0.0, gender: bool = False, money: float = 0.0):
        self.Name = name
        self.Age = age
        self.Gender = gender
        self.Money = money
        self.Studying = False

    def earnMoney(self, day: int):
        if 150 <= day < 240:
            self.Money += 50
            print(f"Day {day + 1}: Earned money. Current balance: ${self.Money}")

    def spendMoney(self, day: int):
        if day % 30 == 0:
            self.Money -= 100
            print(f"Day {day + 1}: Spent money on necessities. Current balance: ${self.Money}")

    def study(self, day: int):
        if self.Money >= 500:
            self.Studying = True
            print(f"Day {day + 1}: Started studying.")

    def liveYear(self):
        for day in range(365):
            print(f"\n--- Day {day + 1} ---")
            self.spendMoney(day)
            if random.randint(140, 180) <= day:
                days_to_earn = random.randint(30, 60)
                self.earnMoney(day)
            if self.Money >= 500:
                days_to_study = random.randint(5, 10)
                self.study(day)

        print(f"\nYear completed for student {self.Name}. Final balance: ${self.Money}")


student = Student(name="Alex", age=20, money=100.0)
student.liveYear()
