import FreeSimpleGUI as sg
import src.models as models


def show_menu_window():
    btn_size = (20,1)
    layout_menu = [
        [sg.Text(f"The current balance is: ")], #value_balance
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
            show_expense_window()
        elif event == "Income":
            show_income_window()
        elif event == "New Category":
            show_category_window()
    window_menu.close()

def show_expense_window(categories):
    btn_size = (20,1)
    layout_expense = [
        [sg.Text("Title: ",size=(10,1)), sg.Input(key="-EX_TITLE_INPUT-",size=(30,1))],
        [sg.Text("Amount: ",size=(10,1)), sg.Input(key="-EX_AMOUNT_INPUT-",size=(30,1))],
        [sg.Text("Category: ",size=(10,1)), sg.Combo([c.name for c in categories], key='-EX_CATEGORY_INPUT-',size=(30,1))],
        [sg.Text(size=(40,1),key="-EX_OUTPUT_MESSAGE-")],
        [sg.Button("Accept",size=btn_size),sg.Button("Cancel",size=btn_size)],
    ]
    window_expense = sg.Window("Expense entry",layout_expense, modal=True)

    while True:
        event, values = window_expense.read()

        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break
        elif event == "Accept":
            try:
                if values["-EX_CATEGORY_INPUT-"] == []:
                    window_expense["-EX_OUTPUT_MESSAGE-"].update("Please in enter a category")
                else:
                    expense = {
                    "movement_type": "expense",
                    "title": values["-EX_TITLE_INPUT-"],
                    "amount": float(values["-EX_AMOUNT_INPUT-"]),
                    "category": values["-EX_CATEGORY_INPUT-"]
                    }
                    window_expense.close()
                    return models.Movement(*expense.values()) #unpacking the list*
            except ValueError as error:
                window_expense["-EX_OUTPUT_MESSAGE-"].update("Please in enter a valid number in amount")
    window_expense.close()
    return None


def show_income_window(categories):
    btn_size = (20,1)
    layout_income = [
        [sg.Text("Title: ",size=(10,1)), sg.Input(key="-IN_TITLE_INPUT-",size=(30,1))],
        [sg.Text("Amount: ",size=(10,1)), sg.Input(key="-IN_AMOUNT_INPUT-",size=(30,1))],
        [sg.Text("Category: ",size=(10,1)), sg.Combo([c.name for c in categories], key='-IN_CATEGORY_INPUT-',size=(30,1))],
        [sg.Text(size=(40,1),key="-IN_OUTPUT_MESSAGE-")],
        [sg.Button("Accept",size=btn_size),sg.Button("Cancel",size=btn_size)],
    ]
    window_income = sg.Window("Income entry",layout_income, modal=True)

    while True:
        event, values = window_income.read()

        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break
        elif event == "Accept":
            try:
                if values["-IN_CATEGORY_INPUT-"] == []:
                    window_income["-IN_OUTPUT_MESSAGE-"].update("Please in enter a category")
                else:
                    income = {
                    "movement_type": "income",
                    "title": values["-IN_TITLE_INPUT-"],
                    "amount": float(values["-IN_AMOUNT_INPUT-"]),
                    "category": values["-IN_CATEGORY_INPUT-"],
                    }
                    window_income.close()
                    return models.Movement(*income.values()) #unpacking the list*
            except ValueError as error:
                window_income["-IN_OUTPUT_MESSAGE-"].update("Please in enter a valid number in amount")
    window_income.close()
    return None


def show_category_window(categories):
    btn_size = (20,1)
    layout_category = [
        [sg.Text("Please create a category that is not in the options already: ")],
        [sg.Text("Categories: ",size=(10,1)), sg.Combo([c.name for c in categories], key='-CATEGORY-',size=(30,1))],
        [sg.Text("New Category: ",size=(10,1)),sg.Input(key="-INPUT-",size=(30,1))],
        [sg.Text(size=(40,1),key="-OUTPUT-")],
        [sg.Button("Accept",size=btn_size),sg.Button("Cancel",size=btn_size)],
        
    ]
    window_category = sg.Window("Creation of Category",layout_category, modal=True)

    while True:
        event, values = window_category.read()

        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break
        elif event == "Accept":
            if values["-INPUT-"] != "":
                if values["-INPUT-"].lower() in [c.name.lower() for c in categories]:
                    window_category["-OUTPUT-"].update("The category is already created")
                else:
                    try:
                        name =  values["-INPUT-"]
                        window_category.close()
                        return name
                    except ValueError as error:
                        window_category["-OUTPUT-"].update("Please in enter a category")

    window_category.close()
    return None