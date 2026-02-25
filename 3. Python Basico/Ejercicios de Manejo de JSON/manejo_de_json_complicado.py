import json
import os
from pathlib import Path

def clear_screen():
    #Clears the screen and the terminal
    os.system('clear' if os.name != 'nt' else 'cls')


#1. I need to read the file
#2. I need to know if the data is a list or dictionary
#3. I need to explore if there is a nested dictionary or nested key:value

# def identify_data_type(data):
#     data_type = ""
#     if isinstance(data, dict):
#         data_type = "dict"
#     elif isinstance(data, list):
#         data_type = "list"
#     return data_type


def read_json(file_path):
    with open (file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def extract_keys(data, main_key = ""):
    list_of_keys = []
    if isinstance(data, dict):
        for key,value in data.items():
            #keeping track of the main key
            if main_key == "":
                new_route = key
            else:
                new_route = f"{main_key}.{key}"

            list_of_keys.append(new_route) # saving the value to the list of keys


            #evaluating if the value is another dict
            if isinstance(value,dict):
                list_of_keys.extend(extract_keys(value,new_route)) #calls the same function to explore in the nested key before passing to the next key and save the new value
            else:
                list_of_keys.append(main_key)
    elif isinstance(data, list) and len(data) > 0:
        list_of_keys.extend(extract_keys(data[0], f"{main_key}[]")) #first element of the list

    return list(set(list_of_keys))


def main ():
    name = input('Please enter name of the json that contains the pokemon info: ').strip()
    file_path = Path(name).stem #removes the extension
    if not file_path.lower().endswith('.json'):
        file_path += '.json'
    try: 
        data = read_json(file_path)
        keys = extract_keys(data)
        print(keys)
    except FileNotFoundError:
        print("Error: The file was not found.")
    return print(extract_keys(data))



if __name__ == '__main__':
    main()

# read_json("pokemon.json")
