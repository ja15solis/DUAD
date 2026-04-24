import src.database as database
import src.models as models


def test_import_csv_file_returns_an_empty_list_if_the_path_does_not_exist():\
    # import_csv_file(file_path,object_type)
    #Arrange
    file_path =  'Projects/finance_manager_app/data/categories.csv'
    object_type = "movements"
    #Act
    result = database.import_csv_file(file_path,"movements")
    #Assert
    assert result == []