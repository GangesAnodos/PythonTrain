"""
This module contains all the logic for Exercise 4: Student Grades.

It includes functions to calculate a student's average grade, evaluate their
status (Approved, Recovery, Failed), and a main function to run the
user interaction loop for this exercise.
"""

from time import sleep as tsleep
from util import clear_screen

def cal_average(note1, note2, note3):
    """Calculates the average of three grades."""
    average = (note1 + note2 + note3) / 3
    return average

def validate_grade():
    """Gets student grades, calculates the average, and displays the status."""
    tsleep(1)
    clear_screen()

    while True:
        print("\n--Exercise 4: Validate Grade--")
        try:
            note1 = float(input("Note 1: "))
            note2 = float(input("Note 2: "))
            note3 = float(input("Note 3: "))

            result = cal_average(note1, note2, note3)
            tsleep(1)
            if result >= 7:
                print(f"Approved. The average grade is { result:.2f}.")
            elif result >= 5:
                print(f"Recovery. The average grade is { result:.2f}.")
            else:
                print(f"Failed. The average grade is { result:.2f}.")
            tsleep(3)
        except ValueError:
            print("Invalid input. Please enter a number only.")
            tsleep(3)

        op = input("Do you wish to continue? Press Y to continue: ").upper()
        if op == "Y":
            print("Continuing")
            tsleep(1)
        else:
            print("Returning to main menu..")
            tsleep(1)
            break


if __name__ == '__main__':
    validate_grade()