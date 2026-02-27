#logic of every data import or export
import csv
import os
import menu
from actions import clear_screen

#5
def save_csv_file(students_info,file_path = 'students_info.csv'):
    clear_screen()
    # Show the option the user selected 
    print("5. Export data in CSV")
    print("-" * 50)
    headers = students_info[0].keys()
    try:
        with open(file_path, 'w', encoding= 'utf-8',newline='') as file:
            writer = csv.DictWriter(file,fieldnames=headers)
            writer.writeheader()
            writer.writerows(students_info)
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
def import_csv_file(students_info,file_path = 'students_info.csv'):
    clear_screen()
    # Show the option the user selected 
    print("6. Import data via CSV")
    print("-" * 50)
    if os.path.exists(file_path):
        with open(file_path, mode= 'r', encoding= 'utf-8',newline='') as file:
            students_reader = csv.DictReader(file)
            students_info = list(students_reader) # convert the DictReader object into a list, makes it a list of dictionaries.
            print("You have successfully imported the information from {file_path}")
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
