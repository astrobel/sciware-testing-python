import pytest
from sciware_testing_python import sum_numbers, add_vectors

def test_sum_numbers_123():
    # basic test to see if we get the expected answer for a simple case.
    sum_test = sum_numbers([1,2,3])
    assert sum_test == 6

def test_sum_numbers_yours():
    # write another test of the sum_numbers function
    sum_test = sum_numbers([5,6,7,8])
    assert sum_test == 26 # boot scootin'!

def test_sum_numbers_empty():
    # what's the sum of an empty list?
    pass

#@pytest.mark.xfail(strict=True, raises=TypeError)
def test_sum_strings():
    #assert sciware_testing_python.sum_numbers(["1","2","3"]) == "123"
    pass

# Write a test for the add_vectors function

# Write a test for sum_numbers on a list of booleans
