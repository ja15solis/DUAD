import pytest
import random
from ejercicios_de_funciones_4 import reverse_text

def test_reverse_text_works_with_strings():
    #Arrange
    value = "DLROW OLLEH"
    #Act
    result = reverse_text(value)
    #Assert
    assert result == "HELLO WORLD"

def test_reverse_text_works_with_values_within_a_list():
    #Arrange
    value = ["hello","world"]
    #Act
    result = reverse_text(value)
    #Assert
    assert result == "worldhello"

def test_reverse_text_fails_with_list_of_numbers():
    #Arrange
    value = [0,1,2,3,4,5]
    #Act #Assert
    with pytest.raises(TypeError):
        reverse_text(value)