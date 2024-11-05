import pytest  # pytest install ==> pip install pytest
from encoding_function import *
from remove_duplicates import *
from reverse_list import *

def test_encoding_function():
    # Test with a valid input
    assert encoding_function("2 0 5 4") == "CAFE", "Test Case 1 Failed"
    
    # Test with an input that includes numbers outside the range
    assert encoding_function("9 8 7") == "JIH", "Test Case 2 Failed"
    
    # Test with an input that contains a number not in the dictionary
    # Since your original function does not handle exceptions,
    # We won't include a test case that expects an exception here

def test_remove_duplicates():
    # Test with a list containing duplicates
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5], "Test Case 1 Failed"
    
    # Test with a list that has no duplicates
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5], "Test Case 2 Failed"
    
    # Test with an empty list
    assert remove_duplicates([]) == [], "Test Case 3 Failed"

def test_reverse_list():
    # Test with a valid input
    assert reverse_list([1, 2]) == [2, 1], "Test Case 1 Failed"
    
    # Test with a different valid input
    assert reverse_list([100, 200]) == [200, 100], "Test Case 2 Failed"
    
    # Test with identical numbers
    assert reverse_list([5, 5]) == [5, 5], "Test Case 3 Failed"

# Uncomment the below line if you want to run pytest from the script directly
pytest.main()

