import csv
import os
from pathlib import Path #for removing the extension of the file

def clear_screen():
    #Clears the screen and the terminal
    os.system('clear' if os.name != 'nt' else 'cls')

def user_input_games():
    list_of_games = []
    while True:
        clear_screen()
        print("=" * 50)
        print("           NEW GAME ENTRY         ")
        print("=" * 50)
        name = input('Please enter the name of the game: ')
        game_type = input('Please enter the type of game: ')
        developer = input('Please enter the Developer of game: ')
        esrb_classification = input('Please enter the ESRB classification of game: ')
        
        entry = {
            'Name': name,
            'Type': game_type,
            'Developer':developer,
            'ESRB classification': esrb_classification
        }

        list_of_games.append(entry)

        while True:
            other_game = input('Do you want to enter another game? (Y/N): ').strip().lower()
            if other_game =='y':
                break
            elif other_game == "n":
                return list_of_games               
            else:
                print("Please enter a valid answer to the question, 'Y' or 'N'.")
    

def save_csv_file(file_path):
    list_of_games = user_input_games()
    headers = list_of_games[0].keys()
    with open(file_path, 'w', encoding= 'utf-8',newline='') as file:
        writer = csv.DictWriter(file,fieldnames=headers,delimiter='\t')
        writer.writeheader()
        writer.writerows(list_of_games)

def main ():
    name = input('Please enter the name of the csv where you want to save the info of the games: ').strip()
    file_path = Path(name).stem
    if not file_path.lower().endswith('.csv'):
        file_path += '.csv'
    save_csv_file(file_path)
    clear_screen()
    print(f'You have successfully created the {file_path} with the games information')

if __name__ == '__main__':
    main()