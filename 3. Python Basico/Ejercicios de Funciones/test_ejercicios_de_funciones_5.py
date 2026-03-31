import pytest
import random
from ejercicios_de_funciones_5 import count_upper_low_cases

def test_count_low_cases():
    #Arrange
    value = "HellO WoRLd"
    #Act
    result = count_upper_low_cases(value)
    #Assert
    assert result["lower_cases"] == 5

def test_count_upper_cases():
    #Arrange
    value = "HellO WoRLd"
    #Act
    result = count_upper_low_cases(value)
    #Assert
    assert result["upper_cases"] == 5

def test_count_upper_lower_cases_fails_with_no_str_type():
    #Arrange
    value = [0,1,2,3,4,5]
    #Act #Assert
    with pytest.raises(TypeError):
        count_upper_low_cases(value)