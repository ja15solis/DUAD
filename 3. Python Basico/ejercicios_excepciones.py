import os

def clear_screen():
    #Clears the screen and the terminal
    os.system('clear' if os.name != 'nt' else 'cls')

def sum_number (actual_number):
    while True: 
        print(f'The actual number is {actual_number}')
        number_to_sum = input('Please enter the number you want to sum to the current number: ')
        try:
            number_to_sum = float(number_to_sum)
            actual_number += number_to_sum
            break
        except ValueError as error:
            print(f'The input was not a valid number: {error}')
    print(f"The result is: {actual_number} ")
    return menu(actual_number)


def subtract_number (actual_number):
    while True:
        print(f'The actual number is {actual_number}')
        number_to_sub = input('Please enter the number you want to subtract to the current number: ')
        try:
            number_to_sub = float(number_to_sub)
            actual_number -= number_to_sub
            break
        except ValueError as error:
            print(f'The input was not a valid number: {error}')
    print(f"The result is: {actual_number} ")
    return menu(actual_number)


def multiply_number (actual_number):
    while True:
        print(f'The actual number is {actual_number}')
        number_to_multiply = input('Please enter the number you want the \"current number\" to be multiplied by: ')
        try:
            number_to_multiply = float(number_to_multiply)
            actual_number *= number_to_multiply
            break
        except ValueError as error:
            print(f'The input was not a valid number: {error}')
    print(f"The result is: {actual_number} ")
    return menu(actual_number)


def divide_number (actual_number):
    while True:
        print(f'The actual number is {actual_number}')
        denominator = input('Please enter the number you want the \"current number\" to be divided into: ')
        try:
            denominator = float(denominator)
            actual_number /= denominator
            break
        except ValueError as error:
            print(f'The input was not a valid number: {error}')
        except ZeroDivisionError:
            print('Error: Cannot divide by zero. Please enter a different number.')
    print(f"The result is: {actual_number} ")
    return menu(actual_number)


def change_default_number (actual_number):
    while True:
        print(f'The actual number is {actual_number}')
        actual_number = input('Please enter the new default number: ')
        try:
            actual_number = float(actual_number)
            break
        except ValueError as error:
            print(f'The input was not a valid number: {error}')
    print(f"The actual number now is: {actual_number} ")
    return menu(actual_number)



def menu (actual_number):
    clear_screen()
    print("=" * 50)
    print("          CALCULATOR MENU")
    print("=" * 50)
    print(f"Current number: {actual_number}")
    print("-" * 50)
    print("1. Sum")
    print("2. Subtract")
    print("3. Multiplication")
    print("4. Division")
    print("5. Change default value (clear result)")
    print("6. Exit")
    print("=" * 50)
    while True:
        menu_value = input('Please select an option in the menu: ')
        try:
            menu_value = int(menu_value)
            if 0 < menu_value < 7:
                break
            else:
                raise ValueError()
        except ValueError as error:
            print("Please enter a valid number from the menu")
    match menu_value:
        case 1:
            result = sum_number(actual_number)
        case 2:
            result = subtract_number(actual_number)
        case 3:
            result = multiply_number (actual_number)
        case 4:
            result = divide_number (actual_number)
        case 5:
            result = change_default_number(actual_number)
        case 6:
            print("Thank you for using this calculator!")


def main ():
    actual_number = 1.0
    menu(actual_number)

if __name__ == '__main__':
    main()