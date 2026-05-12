import FreeSimpleGUI as sg
from src import models as models
from src import validation

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
            movement, error = validation.validate_movement(
                values,
                key_map={
                    "title": "-EX_TITLE_INPUT-",
                    "amount": "-EX_AMOUNT_INPUT-",
                    "category": "-EX_CATEGORY_INPUT-"
                },
                movement_type="expense"
            )
            if error:
                match str(error):
                    case "Title":
                        window_expense["-EX_OUTPUT_MESSAGE-"].update("Please enter a Title")
                    case "Amount":
                        window_expense["-EX_OUTPUT_MESSAGE-"].update("Please in enter a valid number in Amount")
                    case "Category":
                        window_expense["-EX_OUTPUT_MESSAGE-"].update("Please in enter a Category")
                    case "Invalid Number":
                        window_expense["-EX_OUTPUT_MESSAGE-"].update("Please enter a positive value for Amount")
            else:
                window_expense.close()
                return movement


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
            movement, error = validation.validate_movement(
                values,
                key_map={
                    "title": "-IN_TITLE_INPUT-",
                    "amount": "-IN_AMOUNT_INPUT-",
                    "category": "-IN_CATEGORY_INPUT-"
                },
                movement_type="income"
            )
            if error:
                match str(error):
                    case "Title":
                        window_income["-IN_OUTPUT_MESSAGE-"].update("Please enter a Title")
                    case "Amount":
                        window_income["-IN_OUTPUT_MESSAGE-"].update("Please in enter a valid number in Amount")
                    case "Category":
                        window_income["-IN_OUTPUT_MESSAGE-"].update("Please in enter a Category")
                    case "Invalid Number":
                        window_income["-IN_OUTPUT_MESSAGE-"].update("Please enter a positive value for Amount")
            else:
                window_income.close()
                return movement


def show_category_window(categories):
    btn_size = (20,1)
    layout_category = [
        [sg.Text("Please create a new category: ")],
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