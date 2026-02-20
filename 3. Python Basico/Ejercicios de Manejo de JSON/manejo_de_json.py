import json
from pathlib import Path


def read_json(file_path):
    with open (file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def add_data(data):

    print("Adding a new pokemon")
    new_entry = {}
    new_entry['name'] = {"english": input("Pokemon name: ")}
    new_entry['level'] = int(input("Enter the level of the pokemon (from 1 to 100): "))
    new_entry['type'] = input("Type of the pokemon (separated by ','): ").split(',')
    new_entry['base']={}
    new_entry['base']['HP'] = int(input("Enter the base HP (from 1 to 100): "))
    new_entry['base']['Attack'] = int(input("Enter the base Attack (from 1 to 100): "))
    new_entry['base']['Defense'] = int(input("Enter the base Defense (from 1 to 100): "))
    new_entry['base']['Sp. Attack'] = int(input("Enter the base Sp. Attack (from 1 to 100): "))
    new_entry['base']['Sp. Defense'] = int(input("Enter the base Sp. Defense (from 1 to 100): "))
    new_entry['base']['Speed'] = int(input("Enter the base Speed (from 1 to 100): "))
    data.append(new_entry)
    print("¡New pokemon added!")
    
    return data


def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False) #making it more readable and ascii is for special characters
    print(f"Changes saved in: {file_path}")


def main ():
    name = input('Please enter name of the json that contains the pokemon info: ').strip()
    file_path = Path(name).stem #removes the extension
    if not file_path.lower().endswith('.json'):
        file_path += '.json'
    try: 
        data = read_json(file_path)
        # keys = extract_keys(data)
        data_modified = add_data(data)
        save_json(data_modified,file_path)

    except FileNotFoundError:
        print("Error: The file was not found.")
    return 



if __name__ == '__main__':
    main()

