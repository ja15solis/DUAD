#Entry point of the program
from pathlib import Path
import src.controller

base_directory = Path(__file__).resolve().parent # absolute path

def main ():
    data_directory = base_directory / "data" 
    data_directory.mkdir(exist_ok=True) #auto create data directory and if exist_ok=True it doesn't raise FileExistsError

    categories_path = data_directory / 'categories.csv'
    movements_path  = data_directory / 'account_balance.csv'

    src.controller.menu(categories_path,movements_path)


if __name__ == '__main__':
    main()