"""
    A System of Grades and Status
"""

from util import clear_screen
from time import sleep as tsleep

def main():
    """
    The Menu of Exercise 5
    :return: None
    """
    students_list = []
    while True:
        clear_screen()
        tsleep(1)
        print("\n -- System of Grades and Status Menu--\n")
        print(" Press 1 to: Add students\n"
              " Press 2 to: List students\n"
              " Press 3 to: Grades and Status for all students\n"
              " Press 0 to return to main menu\n")
        try:
            op = int(input())
            match op:
                case 1:
                    add_students(students_list)
                case 2:
                    list_students(students_list)
                case 3:
                    list_students_details(students_list)
                case 0:
                    print("return to main menu")
                    break
                case _:
                    print("Invalid input")
        except ValueError:
            print("Please enter a number.")

#Add students
def add_students(students_list):
    """
    Add students and their grades to the list
    :param students_list:
    :return: None
    """
    clear_screen()
    while True:
        grades = []
        max_grades = []
        grades_details = []
        print("\n -- Adding a student--")
        first_name = input("Enter student first name: ")
        last_name = input("Enter student last name: ")
        full_name = first_name + " " + last_name

        is_duplicate = False
        for student in students_list:
            if student["Name"] == full_name:
                is_duplicate = True
                print(f"\nError: A student with name {full_name.capitalize()} already exists.")

        if is_duplicate:
            tsleep(1)
            continue
        print("\n -- Adding grades for student--")
        while True:
            try:
                grade = float(input("Enter student grade: "))
                max_grade = float(input("Enter max grade: "))

                if grade > max_grade:
                    print("\nError:  Student grade cannot be greater than the max grade.")
                    continue

                grades.append(grade)
                max_grades.append(max_grade)
                grades_details.append({
                    "Grade": grade,
                    "Max Grade": max_grade,
                })
                op = input("Press N to finish or Enter to add another grade: ").upper()
                if op == "N":
                    break
            except ValueError:
                print("Invalid input")
        average, status = cal_average(grades, max_grades)

        data = {
            "Name": full_name,
            "Grades": grades_details,
            "Status": status,
            "Average": round(average, 2),
        }
        students_list.append(data)
        print("\n Successfully added student")
        tsleep(1)
        op = input("\nAdd another student? (Press N to finish or any other key to continue) \n").upper()
        if op == "N":
            break

#calculate the average
def cal_average(grades, max_grades):
    """
    Calculates the average in grades of list.
    :param grades: list of grades
    :param max_grades: list of max grades
    :return: average - float in percent and status of average in string
    """

    if not grades or sum(max_grades) == 0:
        return 0.0, "Incomplete"

    average = sum(grades) / sum(max_grades) * 100
    if average >= 70:
        stats = "Approved"
    elif average >= 50:
        stats = "Recovery"
    else:
        stats = "Failed"
    return average, stats

#list names and averages on all students in list_students
def list_students(students_list):
    """
    List Name and Average on all students in students_list
    :param students_list:
    :return:
    """

    if not students_list:
        print("\nNo students found.")
        return

    print("-₢/₢-")
    for student in students_list:

        print(f"Student: {student['Name']} Average: {student['Average']}")
        print("-₢/₢-")

    input("Press Enter to continue...")

#list details of all students in list_students
def list_students_details(students_list):
    """
    Lists all students details in students_list.
    :param students_list:
    :return:
    """

    if not students_list:
        print("-₢" * 2)
        print("No students")
        print("-₢" * 3)
        return
    for student in students_list:
        print("-₢" * 2)
        print(f" Name: {student["Name"]}")
        print(f" Grades:")
        for grades in student["Grades"]:
            grade_value = grades["Grade"]
            max_grade_value = grades["Max Grade"]
            print(f"    - Grade {grade_value}, Max Grade: {max_grade_value};")
        print(f" Status: {student["Status"]}")
        print(f" Average: {student["Average"]}")
        print("-₢" * 3)

    input("Press Enter to continue...")

if __name__ == "__main__":
    main()