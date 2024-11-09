import random

class Student:
    def __init__(self, name: str = "Test", age: float = 0.0, gender: bool = False, money: float = 0.0):
        self.Name = name
        self.Age = age
        self.Gender = gender
        self.Money = money
        self.Studying = False

    def earnMoney(self, days_to_earn: int):
        for day in range(days_to_earn):
            if 150 <= day < 240:  # Inclusive range for earning period
                self.Money += 50
                print(f"Day {day+1}: Earned money. Current balance: ${self.Money}")

    def spendMoney(self):
        for day in range(365):
            if day % 30 == 0:
                self.Money -= 100
                print(f"Day {day+1}: Spent money on necessities. Current balance: ${self.Money}")

    def study(self, days_to_study: int):
        for day in range(days_to_study):
            if self.Money >= 500:
                self.Studying = True
                print(f"Day {day+1}: Started studying.")

    def liveYear(self):
        for day in range(365):
            # Prioritize spending to maintain basic needs
            self.spendMoney()

            # Earn money during summer break (randomly adjust days)
            if random.randint(140, 180) <= day:  # Variable summer duration
                days_to_earn = random.randint(30, 60)  # Variable earning period
                self.earnMoney(days_to_earn)

            # Study only when financially secure
            if self.Money >= 500:
                days_to_study = random.randint(5, 10)  # Variable study duration
                self.study(days_to_study)

        print(f"\nYear completed for student {self.Name}. Final balance: ${self.Money}")


# Create a student instance and simulate a year
student = Student(name="Alex", age=20, money=100.0)
student.liveYear()