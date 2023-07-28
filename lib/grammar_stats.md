Problem:
As a user
So that I want to check if a text starts with capital letter and ends with sentence-ending punctuation mark,
I also want to check what percentage of the 'check' have passed the tests.

Function Signature:
The signature of a class includes:

def check(self, text)
    Verify if text starts with capital letter and ends with sentence-ending punctuation mark

Parameters:
    text: a long string of text to check

Returns:
    a boolean value True if the text starts with capital letter and ends with sentence-ending punctuation mark

Side effects:
    No side effects

Examples:

"""
Given a string that begins with a capital letter
and ends with a sentence-ending punctuation mark
Return True
"""
def test_starts_with_capital_ends_with_punctuation('Hello, my name is Bob. Pleasure to meet you!'):
    ==> True

"""
Given a string
Returns the integer number of the percentage
of the tests passed
"""
def percentage_good():
    ==> 20