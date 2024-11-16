
class Device:
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} увімкнено")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} вимкнено")

    def __str__(self):
        return f"{self.name}: {'Увімкнено' if self.is_on else 'Вимкнено'}"


class Television(Device):
    pass


class Computer(Device):
    pass


class Lamp(Device):
    pass


def main():
    devices = {
        "телевізор": Television("Телевізор"),
        "комп'ютер": Computer("Комп'ютер"),
        "лампа": Lamp("Лампа")
    }

    while True:
        print("\n1. Показати пристрої")
        print("2. Увімкнути пристрій")
        print("3. Вимкнути пристрій")
        print("4. Вихід")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            for device in devices.values():
                print(device)

        elif choice == "2":
            device_name = input("Введіть назву пристрою для увімкнення: ").lower()
            if device_name in devices:
                devices[device_name].turn_on()
            else:
                print("Пристрій не знайдено.")

        elif choice == "3":
            device_name = input("Введіть назву пристрою для вимкнення: ").lower()
            if device_name in devices:
                devices[device_name].turn_off()
            else:
                print("Пристрій не знайдено.")

        elif choice == "4":
            break

        else:
            print("Неправильний вибір. Спробуйте знову.")


if __name__ == "__main__":
    main()
