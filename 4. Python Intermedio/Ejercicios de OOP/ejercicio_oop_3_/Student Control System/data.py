#logic of every data import or export
import csv
import os
import menu
from actions import Student
from actions import clear_screen

#5
def save_csv_file(students_info,file_path = '4. Python Intermedio/Ejercicios de OOP/ejercicio_oop_3_/Student Control System/students_info.csv'):
    clear_screen()
    # Show the option the user selected 
    print("5. Export data in CSV")
    print("-" * 50)
    student_info_dict = [student.__dict__ for student in students_info]
    headers = student_info_dict[0].keys()
    try:
        with open(file_path, 'w', encoding= 'utf-8',newline='') as file:
            writer = csv.DictWriter(file,fieldnames=headers)
            writer.writeheader()
            writer.writerows(student_info_dict)
        print(f"You have successfully saved the file named {file_path} !")
    except TypeError as error:
        print(f'There was an error related to data type: {error}')

    #This is for printing the result of the file exported and then return the menu function
    while True:
        print("-" * 50)
        return_to_menu = input('Press M and ENTER to return to the menu (M): ').strip().lower()
        if return_to_menu =='m':
            return menu.menu(students_info)           
        else:
            print("That wasn't the right key.")


#6
def import_csv_file(students_info,file_path = '4. Python Intermedio/Ejercicios de OOP/ejercicio_oop_3_/Student Control System/students_info.csv'):
    clear_screen()
    # Show the option the user selected 
    print("6. Import data via CSV")
    print("-" * 50)
    if os.path.exists(file_path):
        with open(file_path, mode= 'r', encoding='utf-8-sig',newline='') as file:
            students_reader = csv.DictReader(file)
            # convert the DictReader object into a list, makes it a list of dictionaries.
            student_info_dict = list(students_reader) # convert the DictReader object into a list, makes it a list of dictionaries.
            # change the values to int in a specific list of keys
            keys_to_change = ['spanish','english','social_studies','science']
            for entry in student_info_dict:
                for key in keys_to_change: #iterate over the list of keys to change
                    if key in entry: 
                        entry[key] = float(entry[key])

            #dropping average because is calculated when the Student is created
            for student in student_info_dict:
                student.pop("average", None)
            # creating the list of students
            students_info = [Student(**s) for s in student_info_dict]

            print(f"You have successfully imported the information from {file_path}")
            #This is for printing the result of the file import and then return the menu function
            while True:
                print("-" * 50)
                return_to_menu = input('Press M and ENTER to return to the menu (M): ').strip().lower()
                if return_to_menu =='m':
                    return menu.menu(students_info)           
                else:
                    print("That wasn't the right key.")
                
                return menu.menu(students_info)
    else: 
        print("You haven't exported students_info yet, please enter the information manually (1) and export it (5) to make an import later.")
        while True:
                print("-" * 50)
                return_to_menu = input('Press M and ENTER to return to the menu (M): ').strip().lower()
                if return_to_menu =='m':
                    return menu.menu(students_info)           
                else:
                    print("That wasn't the right key.")
                
                return menu.menu(students_info)
