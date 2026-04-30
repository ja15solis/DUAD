#CSV creation and update
#logic of every data import or export
import csv
import os
from src import models
#import menu

def import_csv_file(file_path,object_type):
    # Verifying if the path exist 
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return []
    try:
        with open(file_path, mode= 'r', encoding='utf-8-sig',newline='') as file:
            csv_file = csv.DictReader(file)
            # convert the DictReader object into a list, makes it a list of dictionaries.
            if not csv_file.fieldnames:
                raise ValueError("The csv file has no headers")
            objects = [] # list of dictionaries.
            for row in csv_file:
                if "amount" in row:
                    row["amount"] = float(row["amount"])
                if object_type == "categories":
                    objects.append(models.Category(**row))
                if object_type == "movements":
                    objects.append(models.Movement(**row))
            # change the values to int in a specific list of keys
            return objects
    except (ValueError, csv.Error) as error:
        print(f"There's an error in {file_path}: {error}") #print if there is an error 
        return []
    
def save_csv_file(objects,file_path,object_type):
    if object_type not in ["movements","categories"]:
        raise ValueError("Invalid object_type.")
    if not objects:
        print("No Objects to save.")
        return False
    dict_of_objects = [o.__dict__ for o in objects]
    headers = dict_of_objects[0].keys()
    try:
        with open(file_path, 'w', encoding= 'utf-8',newline='') as file:
            writer = csv.DictWriter(file,fieldnames=headers)
            writer.writeheader()
            writer.writerows(dict_of_objects)
        print(f"You have successfully saved the file named {file_path} !")
        return True
    except TypeError as error:
        print(f'There was an error related to data type: {error}')
        return False 