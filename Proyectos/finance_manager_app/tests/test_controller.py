import src.controller as controller
import src.models as models


def test_headers_data_returns_headers_without_spaces_and_capitalize_words_from_a_list_of_objects():
    #Arrange
    object_expense =  models.Movement("expense","test_object_expense",100,"food")
    object_income =  models.Movement("income","test_object_income",200,"salary")
    
    value = [object_expense,object_income]
    #Act
    result = controller.headers_data(value)
    #Assert
    assert result == ["Movement type","Title","Amount","Category"]


def test_update_data_returns_a_list_of_values_of_the_attributes_using_a_list_of_objects():
    #Arrange
    object_expense =  models.Movement("expense","test_object_expense",100,"food")
    object_income =  models.Movement("income","test_object_income",200,"salary")
    
    value = [object_expense,object_income]
    #Act
    result = controller.update_data(value)
    #Assert
    assert result == [["expense","test_object_expense",100,"food"],["income","test_object_income",200,"salary"]]