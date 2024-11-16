
class Product:
    def __init__(self, name, price, availability):
        self.name = name
        self.price = price
        self.availability = availability
    def __str__(self):
        return f"{self.name}: ${self.price} - {'Available' if self.availability else 'Not Available'}"
class Cart:
    def __init__(self):
        self.items = []
    def add_product(self, product):
        self.items.append(product)
    def remove_product(self, product_name):
        self.items = [product for product in self.items if product.name != product_name]
    def total_cost(self):
        return sum(item.price for item in self.items)
    def show_cart(self):
        for item in self.items:
            print(f"{item.name}: ${item.price}")
def main():
    products = [
        Product("Шоколад", 5.0, True),
        Product("Чай", 3.5, True),
        Product("Кава", 7.0, False)
    ]
    cart = Cart()
    while True:
        print("\n1. Показати продукти")
        print("2. Додати продукт до кошика")
        print("3. Видалити продукт з кошика")
        print("4. Показати кошик")
        print("5. Підрахувати загальну вартість")
        print("6. Вихід")

        choice = input("Виберіть опцію: ")
        if choice == "1":
            for product in products:
                print(product)
        elif choice == "2":
            product_name = input("Введіть назву продукту для додавання: ")
            for product in products:
                if product.name == product_name:
                    cart.add_product(product)
                    print(f"{product_name} додано до кошика.")
                    break
            else:
                print("Продукт не знайдено або недоступний.")

        elif choice == "3":
            product_name = input("Введіть назву продукту для видалення: ")
            cart.remove_product(product_name)
            print(f"{product_name} видалено з кошика.")

        elif choice == "4":
            print("Продукти у кошику:")
            cart.show_cart()

        elif choice == "5":
            print(f"Загальна вартість: ${cart.total_cost()}")

        elif choice == "6":
            break

        else:
            print("Неправильний вибір. Спробуйте знову.")


if __name__ == "__main__":
    main()
