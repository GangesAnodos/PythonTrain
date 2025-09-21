from util import clear_screen
from time import sleep as tsleep
import exercise4, exercise5

def menu_choice():
    """Displays the menu and handles exercise selection."""
    while True:
        tsleep(0.5)
        clear_screen()
        print("Menu:\n",
              "Options:\n")
        print(" Press 1 to: run exercise 1 - Name and Age\n"
              " Press 2 to: run exercise 2 - Sum of two Numbers\n"
              " Press 3 to: run exercise 3 - Even or Odd\n"
              " Press 4 to: run exercise 4 - Grades and Status\n"
              " Press 5 to: run exercise 5 - System of Grades and Status\n"
              " Press 0 to finish")
        try:
            option = int(input("Option: "))
            match option:
                case 1:
                    exercise_1()
                case 2:
                    exercise_2()
                case 3:
                    exercise_3()
                case 4:
                    exercise4.validate_grade()
                case 5:
                    exercise5.main()
                case 0:
                    break
                case _:
                    print("Invalid option")
        except ValueError:
            print("Invalid option")
            tsleep(1)

#Get user's name and age and prints them in the screen.
def exercise_1():
    """Get user's name and age and prints them in the screen."""
    tsleep(0.5)
    clear_screen()
    name = input("Enter your name: ")
    while True:

        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Invalid age")
    print(f"Your name is {name} and your age is {age}")
    input("Press enter to continue")

#Gets two numbers from the user and prints their sum.
def exercise_2():
    """Gets two numbers from the user and prints their sum."""
    tsleep(0.5)
    clear_screen()
    print("exercise 2: get two numbers and print their sum")
    while True:
        try:
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
            break

        except ValueError:
            # A simpler error message is often better for the user
            print("Invalid input. Please enter numbers only.")
            tsleep(2)
    result = number1 + number2
    print(f"\nThe sum of {number1:.2f} + {number2:.2f} is: {result:.2f}")
    input("Press enter to continue")

#Par is Even and Impar is Odd
#Get a number, whole number only, and print if is Even or Odd
def exercise_3():
    """Get whole number from the user and print if is Even or Odd"""
    tsleep(0.5)
    clear_screen()
    while True:
        try:
            number = int(input("Enter the whole number: "))
            break
        except ValueError:
            print("Invalid input. Please enter whole numbers only.")
    print(f"The whole number is Even" if number % 2 == 0
          else f"The whole number is Odd")
    input("Press enter to continue")

if __name__ == '__main__':
    menu_choice()