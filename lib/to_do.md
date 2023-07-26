Problem:
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO

Function Signature:
def text_checker(text)
    Verify if a text contains the string #TODO

Parameters:
    text: a long string of text to read

Returns:
    a boolean value True if the text contains the string #TODO

Side effects:
    Exception for inputs that are not strings
    Exception for inputs that is equal to None

Examples:

"""
Given a string that includes #TODO
Returns True
"""
def test_text_includes_string('Hello! #TODO'):
        ==> True

"""
Given a string that doesn't includes #TODO
Returns False
"""
def test_text_without_string('Hello!'):
        ==> False

"""
Given a string that includes TODO
Returns False
"""
def test_text_without_#('Hello! TODO'):
        ==> False

"""
Given an empty string.
Raise Exception
"""
def test_empty_string(''):
    ==> 'No string was given"

"""
Given None type value.
Raises Exception
"""
def test_none_value(None):
     ==> 'No string was given"