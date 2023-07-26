from lib.to_do import *
import pytest

"""
Given a string that includes #TODO
Returns True
"""
def test_text_includes_string():
    assert to_do('Hello! #TODO') == True

"""
Given a string that doesn't includes #TODO
Returns False
"""
def test_text_without_string():
    assert to_do('Hello!') == False

"""
Given a string that includes TODO
Returns False
"""
def test_text_without_ash():
    assert to_do('Hello! TODO') == False

"""
Given an empty string.
Raise Exception
"""
def test_empty_string():
    with pytest.raises(Exception) as error:
        to_do('')
    assert str(error.value) == "No string was given"

"""
Given None type value.
Raises Exception
"""
def test_none_value():
    with pytest.raises(Exception) as error:
        to_do(None)
    assert str(error.value) == "Invalid value"