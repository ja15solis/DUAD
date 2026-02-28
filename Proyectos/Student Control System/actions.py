#logic of every menu action
import os
import menu
import json

def clear_screen():
    #Clears the screen and the terminal
    os.system('clear' if os.name != 'nt' else 'cls')

#1
def add_student_info(students_info):
    clear_screen()
    # Show the option the user selected 
    print("1. Manual Entry of Student Grades")
    #Loop for n students
    while True: 
        clear_screen()
        # general information of the student
        print("-" * 50)
        # Dictionary containing the info of the student
        new_entry = {}
        name = input("Please enter the Student Full Name: ")
        new_entry["name"] = name 
        print("-" * 50)
        new_entry["section"] = input(f"Please enter the class/section of {name}: ")
        print("-" * 50)
        print("Now, please enter the grades of each subject with a value from 1-100: ")
        print("-" * 50)
        # Grades of the student
        ##Spanish
        while True:
            try:
                spanish = int(input("Enter the \"Spanish\" grade: "))
                if 0 <= spanish <= 100:
                    new_entry["spanish"] = spanish
                    break
                else:
                    raise ValueError()
            except ValueError as error:
                print("Please enter a valid number from 1 to 100")
        ##English
        while True:
            try:
                english = int(input("Enter the \"English\" grade: "))
                if 0 <= english <= 100:
                    new_entry["english"] = english
                    break
                else:
                    raise ValueError()
            except ValueError as error:
                print("Please enter a valid number from 1 to 100")
        ##Social Studies
        while True:
            try:
                social_studies = int(input("Enter the \"Social Studies\" grade: "))
                if 0 <= social_studies <= 100:
                    new_entry["social_studies"] = social_studies
                    break
                else:
                    raise ValueError()
            except ValueError as error:
                print("Please enter a valid number from 1 to 100")
        ##Science
        while True:
            try:
                science = int(input("Enter the \"Science\" grade: "))
                if 0 <= science <= 100:
                    new_entry["science"] = science
                    break
                else:
                    raise ValueError()
            except ValueError as error:
                print("Please enter a valid number from 1 to 100")
        # Calculating the Average for each student
        new_entry["average"] = (spanish + english + social_studies + science)/4
        print("-" * 50)
        students_info.append(new_entry)
        print(f"You have successfully added the \" {name}\" info!")

        #Asking fot another record
        while True:
            other_game = input('Do you want to enter another student? (Y/N): ').strip().lower()
            if other_game =='y':
                break
            elif other_game == "n":
                return menu.menu(students_info)    ##end           
            else:
                print("Please enter a valid answer to the question, 'Y' or 'N'.")

#2
def print_students_info(students_info):
    clear_screen()
    # Show the option the user selected 
    print("2. Check Students Info")
    print("-" * 50)
    if not students_info: 
        print("The list is empty please enter information manually (1) or via CSV (6)")
    else:
        # printing in a nice format
        print(json.dumps(students_info, indent=4, sort_keys=False))
    #This is for printing the information and then return the menu function once the user have seen the information
    while True:
        print("-" * 50)
        return_to_menu = input('Press M and ENTER to return to the menu (M): ').strip().lower()
        if return_to_menu =='m':
            return menu.menu(students_info)           
        else:
            print("That wasn't the right key.")
        ##end 

#3
def top_3_students (students_info):
    clear_screen()
    # Show the option the user selected 
    print("3. Top 3 Students")
    print("-" * 50)
    # this is not a copy, any pop would affect the students info:
    top_3 = sorted(students_info, key=lambda x: x['average'], reverse=True)[:3]
    #new list of dictionaries containing the top 3 students
    top_3_general_info = []
    for student in top_3:
        #creating a new dict containing only the info we want
        clean_student = {
        "name": student["name"],
        "average": student["average"]
        }
        top_3_general_info.append(clean_student)
    # printing the result in a nice format
    print(json.dumps(top_3_general_info, indent=4, sort_keys=False))
    #This is for printing the information and then return the menu function once the user have seen the information
    while True:
        print("-" * 50)
        return_to_menu = input('Press M and ENTER to return to the menu (M): ').strip().lower()
        if return_to_menu =='m':
            return menu.menu(students_info)           
        else:
            print("That wasn't the right key.")
    

#4
def average_grade_all_students (students_info):
    clear_screen()
    # Show the option the user selected 
    print("4. Average grade per student-subject")
    print("-" * 50)
    #list of all average records of the students
    list_of_averages = []
    for student in students_info:
        average = student["average"]
        list_of_averages.append(average)
    #calculating the average for the list values
    general_average = sum(list_of_averages)/len(list_of_averages)

    print(f"The average grade of all students is {general_average}")
    #This is for printing the information and then return the menu function once the user have seen the information
    while True:
        print("-" * 50)
        return_to_menu = input('Press M and ENTER to return to the menu (M): ').strip().lower()
        if return_to_menu =='m':
            return menu.menu(students_info)           
        else:
            print("That wasn't the right key.")
