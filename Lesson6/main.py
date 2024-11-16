'''
try:
    'code'
except:
    'handle exception'
finally:
    'code'
'''
'''

from unicodedata import digit
import requests
try:
    response = requests.get('https://httpbin.org1/get')
    digit1 = int(input("Enter digit1: "))
    digit2 = int(input("Enter digit2: "))
    print(digit1/digit2)
except Exception as ex:
    print(f'Standart exception:{ex}')
except ZeroDivisionError as zde:
    print(f'Enter the second digit is not equal zero\n{zde})')
except requests.exceptions.ConnectionError as ce:
    print(f'ConnectionError:\n{ce}')
except ValueError as ve:
    print(f'Enter please integer and not string oe any other type literal\n{ve}')
finally:
    print("Finally block")
print("End")

'''
from validator import *

limit = 20
amount = None
while(True):
    try:
        amountStr = input("Enter amount: ")
        if(amountStr.isdigit()):
            amount = int(amountStr)
        else:
            raise ValueError("You entered wrong value. It eksrcts intenger.")
        Validator.Check(amount, limit)
        print("Thank you for purchase.")
    except ValueError as ve:
        print(ve)
    except BuildError as be:
        print(be)
    except Exception as ex:
        print(ex)
    finally:
        yes = input("Wold you like to try again[Y/N]:")
        if(yes.lower() != 'y'):
            break