def get_integer_input():
    try:
        user_input = input("Please enter a number: ")

        number = float(user_input)

        integer_number = int(number)
        print(f"The integer you entered (or its integer part if it was a float) is: {integer_number}")
    except ValueError:
        print("Error: The input cannot be converted to a number. Please enter a valid number.")

get_integer_input()
