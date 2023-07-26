from lib.estimated_reading_time import *
import pytest

"""
Given a text with 600 words
It returns a time of 3 minutes
"""

def test_600_words():
    text = []
    for i in range(0, 600):
        text.append('word')
    result = estimated_reading_time(text)
    assert result == 'This text should take 3 minutes to read'

"""
Given a text with 1200 words
It returns a time of 6 minutes
"""

# def test_1200_words():
#     text = " ".join(['word' for i in range(0, 1200)])
#     result = estimated_reading_time(text)
#     assert result == 'This text should take 6 minutes to read'

# """
# Given a text of 12,000 words
# It returns a time of 60 minutes
# """

# def test_12000_words():
#     text = " ".join(['word' for i in range(0, 12000)])
#     result = estimated_reading_time(text)
#     assert result == 'This text should take 60 minutes to read'

# """
# Given a text of 2300 words
# It returns a time of 38 minutes
# """

# # def test_2300_words():
# #     text = " ".join(['word' for i in range(0, 2300)])
# #     result = estimated_reading_time(text)
# #     assert result == 'This text should take 38 minutes to read'

"""
Given None as input,
Raise exception
"""

def test_None_value():
    with pytest.raises(Exception) as error:
        estimated_reading_time(None)
    assert str(error.value) == 'Please enter a string'

"""
Given an input different from a string, e.g. number
Raise exception
"""

def test_no_string_given():
    with pytest.raises(Exception) as error:
        estimated_reading_time(123)
    assert str(error.value) == 'Please enter a string'

