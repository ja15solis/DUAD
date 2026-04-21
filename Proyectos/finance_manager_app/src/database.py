#CSV creation and update
#logic of every data import or export
import csv
import os
import src.models as models

#import menu

def import_csv_file(file_path,object_type):
    # Verifying if the path exist 
    if os.path.exists(file_path):
        with open(file_path, mode= 'r', encoding='utf-8-sig',newline='') as file:
            csv_file = csv.DictReader(file)
            # convert the DictReader object into a list, makes it a list of dictionaries.
            dict_of_objects = list(csv_file) # convert the DictReader object into a list, makes it a list of dictionaries.
            # change the values to int in a specific list of keys
            keys_to_change = ['amount']
            for entry in dict_of_objects:
                for key in keys_to_change: #iterate over the list of keys to change
                    if key in entry: 
                        entry[key] = float(entry[key])
            # creating the list of objects (works for categories and movements)
            if object_type == "categories":
                objects = [models.Category(**o) for o in dict_of_objects]
            elif object_type == "movements":
                objects = [models.Movement(**o) for o in dict_of_objects]
            return objects
    else:
        return []
    
def save_csv_file(objects,file_path,object_type):
    if object_type == "movements":
        dict_of_objects = [o.__dict__ for o in objects]
    elif object_type == "categories":
        dict_of_objects = [o.__dict__ for o in objects]
    else:
        raise ValueError("Invalid object_type")
    
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
