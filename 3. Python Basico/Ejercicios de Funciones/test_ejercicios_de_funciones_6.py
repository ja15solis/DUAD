import pytest
import random
from ejercicios_de_funciones_6 import order_string

def test_order_string_works_with_dashes():
    #Arrange
    value = "a-t-g-d-s-g-d"
    #Act
    result = order_string(value)
    #Assert
    assert result == "a-d-d-g-g-s-t"


def test_order_string_works_with_dashes_and_numbers():
    #Arrange
    value = "a-2-4-t5-g2-d3-s7-g6-d6"
    #Act
    result = order_string(value)
    #Assert
    assert result == "2-4-a-d3-d6-g2-g6-s7-t5"


def test_order_string_works_with_only_numbers():
    #Arrange
    value = "3-2-5-7-8-99-6-45-67-23-54-68"
    #Act
    result = order_string(value)
    #Assert
    assert result == "2-23-3-45-5-54-6-67-68-7-8-99"