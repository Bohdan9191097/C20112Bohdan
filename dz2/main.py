class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.energy = 100
        self.hunger = 0
    def feed(self, amount):
        self.hunger -= amount
        self.energy += amount
        print(f"{self.name} поїв {amount} одиниць їжі. Голод: {self.hunger}, Енергія: {self.energy}")
    def sleep(self, hours):
        self.energy += hours * 10
        self.hunger += hours * 5
        print(f"{self.name} спав {hours} годин. Енергія: {self.energy}, Голод: {self.hunger}")
    def play(self):
        if self.energy >= 20:
            self.energy -= 20
            self.hunger += 15
            print(f"{self.name} грався. Енергія: {self.energy}, Голод: {self.hunger}")
        else:
            print(f"{self.name} занадто втомлений для гри.")
    def status(self):
        print(f"{self.name} ({self.species}) - Енергія: {self.energy}, Голод: {self.hunger}")
def main():
    pet_name = input("Введіть ім'я вашого улюбленця: ")
    species = input("Введіть вид (котик чи собачка): ")
    pet = Pet(pet_name, species)
    while True:
        print("\n1. Нагодувати")
        print("2. Вкласти спати")
        print("3. Погратися")
        print("4. Перевірити стан")
        print("5. Вихід")
        choice = input("Виберіть опцію: ")
        if choice == "1":
            amount = int(input("Скільки одиниць їжі дати? "))
            pet.feed(amount)
        elif choice == "2":
            hours = int(input("Скільки годин він спатиме? "))
            pet.sleep(hours)
        elif choice == "3":
            pet.play()
        elif choice == "4":
            pet.status()
        elif choice == "5":
            break
        else:
            print("Неправильний вибір. Спробуйте знову.")

if __name__ == "__main__":
    main()
