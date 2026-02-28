# logic related to menu options
import csv
import os
from pathlib import Path #for removing the extension of the file
import json
import actions
import data
def clear_screen():
    #Clears the screen and the terminal
    os.system('clear' if os.name != 'nt' else 'cls')


def menu (students_info = []):
    clear_screen()
    print("=" * 50)
    print("          STUDENT SYSTEM MENU")
    print("=" * 50)
    print(f"You have {len(students_info)} students entries")
    print("-" * 50)
    print("1. Manual Entry of Student Grades")
    print("2. Check Students Info")
    print("3. Top 3 Students")
    print("4. Average grade per student-subject")
    print("5. Export data in CSV")
    print("6. Import data via CSV")
    print("7. Exit")
    print("=" * 50)
    while True:
        menu_value = input('Please select an option in the menu: ')
        try:
            menu_value = int(menu_value)
            if 0 < menu_value < 8:
                break
            else:
                raise ValueError()
        except ValueError as error:
            print("Please enter a valid number from the menu")
    match menu_value:
        case 1:
            actions.add_student_info (students_info)
        case 2:
            actions.print_students_info (students_info)
        case 3:
            actions.top_3_students (students_info)
        case 4:
            actions.average_grade_all_students(students_info)
        case 5:
            data.save_csv_file(students_info)
        case 6:
            data.import_csv_file(students_info)
        case 7:
            print("Thank you for using this student system!")