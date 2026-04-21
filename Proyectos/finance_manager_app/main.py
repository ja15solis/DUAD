#Entry point of the program
import src.controller


def main ():
    categories_path ='Proyectos/finance_manager_app/data/categories.csv'
    movements_path ='Proyectos/finance_manager_app/data/account_balance.csv'
    src.controller.menu(categories_path,movements_path)


if __name__ == '__main__':
    main()