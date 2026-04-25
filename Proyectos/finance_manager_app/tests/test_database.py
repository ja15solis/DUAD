import src.database as database
import src.models as models
import pytest



def test_import_csv_file_returns_an_empty_list_if_the_path_does_not_exist():
    # import_csv_file(file_path,object_type)
    #Arrange
    file_path =  'Projects/finance_manager_app/data/categories.csv'
    object_type = "movements"
    #Act
    result = database.import_csv_file(file_path,"categories")
    #Assert
    assert result == []


def test_import_csv_file_does_not_returns_an_empty_list_if_the_path_exist():
    # import_csv_file(file_path,object_type)
    #Arrange
    file_path =  'Proyectos/finance_manager_app/data/categories.csv'
    object_type = "categories"
    #Act
    result = database.import_csv_file(file_path,object_type)
    #Assert
    assert result != []

def test_import_csv_file_returns_an_list_of_objects_categories_if_the_object_type_is_categories():
    # import_csv_file(file_path,object_type)
    #Arrange
    file_path =  'Proyectos/finance_manager_app/data/categories.csv'
    object_type = "categories"
    #Act
    result = database.import_csv_file(file_path,object_type)
    #Assert
    assert isinstance(result[0],models.Category)


def test_import_csv_file_returns_an_list_of_objects_movement_if_the_object_type_is_movements():
    # import_csv_file(file_path,object_type)
    #Arrange
    file_path =  'Proyectos/finance_manager_app/data/account_balance.csv'
    object_type = "movements"
    #Act
    result = database.import_csv_file(file_path,object_type)
    #Assert
    assert isinstance(result[0],models.Movement)


def test_save_csv_file_fails_and_returns_value_error_if_the_object_type_is_not_movements_or_categories():
    # save_csv_file(objects,file_path,object_type)
    #objects is a list of objects
    #Arrange
    file_path =  'Proyectos/finance_manager_app/data/test_account_balance.csv'
    object_type = "income"
    objects = []
    objects.append(models.Movement("expense","test_1",1000,"Food"))
    objects.append(models.Movement("expense","test_2",2000,"Food"))
    #Act
    #Assert

    with pytest.raises(ValueError):
        database.save_csv_file(objects,file_path,object_type)


def test_save_csv_file_works_if_the_object_type_is_movements_or_categories():
    # save_csv_file(objects,file_path,object_type)
    #objects is a list of objects
    #Arrange
    file_path =  'Proyectos/finance_manager_app/data/test_account_balance.csv'
    object_type = "movements"
    objects = []
    objects.append(models.Movement("expense","test_1",1000,"Food"))
    objects.append(models.Movement("expense","test_2",2000,"Food"))
    #Act
    result = database.save_csv_file(objects,file_path,object_type)
    #Assert
    assert result == True