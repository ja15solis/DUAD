import pytest
import random
from ejercicios_de_funciones_3 import sum_of_list_values

def test_sum_list_of_values_works_with_small_list():
    #Arrange
    list_of_values = [3,2,1,5,3]
    #Act
    result = sum_of_list_values(list_of_values)
    #Assert
    assert result == 14

def test_sum_list_of_values_works_with_big_list():
    #Arrange
    list_of_values = [random.randint(0,1000) for x in range(150)]
    #Act
    result = sum_of_list_values(list_of_values)
    #Assert
    assert result == sum(list_of_values)

def test_sum_list_of_values_works_with_decimal_numbers():
    #Arrange
    list_of_values = [random.uniform(0.3,100.5) for x in range(150)]
    #Act
    result = round(sum_of_list_values(list_of_values),5)
    #Assert
    assert result == round(sum(list_of_values),5)