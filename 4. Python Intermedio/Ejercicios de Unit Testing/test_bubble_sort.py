import pytest
import random
from bubble_sort import bubble_sort

def test_works_with_small_list ():
    # Arrange
    list_of_numbers = [9,5,2,11]
    # Act
    result = bubble_sort(list_of_numbers)
    # Assert
    assert result == [2,5,9,11]


def test_works_with_long_list():
    # Arrange
    list_of_numbers = [random.randint(0,1000) for x in range(150)]
    # Act
    result_sorted = sorted(list_of_numbers)
    result = bubble_sort(list_of_numbers)
    # Assert
    assert result_sorted == result


def test_works_with_empty_list():
    # Arrange
    list_of_numbers = []
    # Act
    result = bubble_sort(list_of_numbers)
    # Assert
    assert result == None


def test_fails_with_other_parameters_that_are_not_a_list():
    # Arrange
    list_of_numbers = {"test":4}
    # Act # Assert
    with pytest.raises(TypeError):
        bubble_sort(list_of_numbers)

