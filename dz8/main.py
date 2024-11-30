def login():
    correct_username = input("Задайте правильне ім'я користувача: ")
    correct_password = input("Задайте правильний пароль: ")

    try:
        username = input("Введіть ім'я користувача: ")
        password = input("Введіть пароль: ")

        assert username == correct_username, "Невірне ім'я користувача або пароль"
        assert password == correct_password, "Невірне ім'я користувача або пароль"

    except AssertionError as e:
        print(e)
        return False
    else:
        print("Вхід виконано успішно")
        return True


login()
