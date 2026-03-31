import pytest
import random
from ejercicios_de_funciones_7 import prime_numbers_within_a_list

def test_prime_numbers_within_a_list_works_with_small_list():
    #Arrange
    value = [1,2,3,4,5,6,7,8,9]
    #Act
    result = prime_numbers_within_a_list(value)
    #Assert
    assert result == [1,2,3,5,7]


def test_prime_numbers_within_a_list_works_with_large_list():
    #Arrange
    value = [x for x in range(1,200)]
    #Act
    result = prime_numbers_within_a_list(value)
    #Assert
    assert result == [1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,
    89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199]


def test_prime_numbers_within_a_list_works_with_negative_numbers():
    #Arrange
    value = [-1,-2,-3,-4,-5,-6,-7,-8,-9]
    #Act
    result = prime_numbers_within_a_list(value)
    #Assert
    assert result == [-1,-2,-3,-5,-7]