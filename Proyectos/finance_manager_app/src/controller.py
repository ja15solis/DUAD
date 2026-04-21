#event loop and logic
import FreeSimpleGUI as sg
import src.views as views
import src.models as models
import src.database as database

#movements
def headers_data(list_objects):
    dict_movements = [o.__dict__ for o in list_objects]
    headers_list = list(dict_movements[0].keys())
    headers = [h.replace("_"," ").capitalize() for h in headers_list]
    return headers


def update_data(list_objects):
    dict_movements = [o.__dict__ for o in list_objects]
    headers = list(dict_movements[0].keys())
    return [[d.get(h) for h in headers] for d in dict_movements]

def menu(categories_path,movements_path):

    categories = database.import_csv_file(categories_path,"categories") #list of objects
    movements = database.import_csv_file(movements_path, "movements") #list of objects

    # Acount
    account = models.Account(movements)

    #layout
    btn_size = (20,1)

    layout_menu = [
        [sg.Text(f"The current balance is: {account.balance} ",key="-BALANCE-")], #value_balance
        [sg.Table(key= "-TABLE-",values=update_data(movements), headings = headers_data(movements), auto_size_columns=True, justification='left')],
        [sg.Button("Expense",size=btn_size),sg.Button("Income",size=btn_size)],
        [sg.Button("New Category",size=btn_size),sg.Button("Quit",size=btn_size)],
        [sg.Text(size=(40,1),key="-OUTPUT-")],
    ]
    window_menu = sg.Window("Personal Finance Manager",layout_menu)

    while True:
        event, values = window_menu.read()
        if event == sg.WINDOW_CLOSED or event == "Quit":
            break
        elif event == "Expense":
            expense = views.show_expense_window(categories)
            if expense is None:
                continue
            account.apply_movement(expense)#this already append the movement
            #movements.append(income)
            window_menu["-BALANCE-"].update(f"The current balance is: {account.balance} ")
            window_menu["-TABLE-"].update(values = update_data(movements))
            #objects,file_path,object_type
            database.save_csv_file(movements,movements_path,"movements")
        elif event == "Income":
            income = views.show_income_window(categories)
            if income is None:
                continue
            account.apply_movement(income) #this already append the movement
            #movements.append(income)
            window_menu["-BALANCE-"].update(f"The current balance is: {account.balance} ")
            window_menu["-TABLE-"].update(values = update_data(movements))
            database.save_csv_file(movements,movements_path,"movements")
        elif event == "New Category":
            name = views.show_category_window(categories)
            if name is None:
                continue
            category = models.Category(name)
            categories.append(category)
            database.save_csv_file(categories,categories_path,"categories")



    window_menu.close()