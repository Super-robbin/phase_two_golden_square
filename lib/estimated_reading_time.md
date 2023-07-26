Problem:
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.


Function Signature:
def estimated_reading_time(text)
    prints a string that is the estimated reading time based on input text

Parameters:
    text: a long string of text to read

Returns:
    a new string stating the estimated reading time in minute
    E.g. 'This text should take .. minutes to read'

Side effects:
    Exception for inputs that are not strings
    Exception for inputs that is equal to None


Examples:

"""
Given a text with 600 words
It returns a time of 3 minutes
"""
def test_600_words(''..600..'):
==> '3 minutes'


"""
Given a text with 1200 words
It returns a time of 6 minutes
"""
def test_1200_words(''..1200..'):
==> '6 minutes'

"""
Given a text of 12,000 words
It returns a time of 60 minutes
"""
def test_1200_words(''..1200..'):
==> '6 minutes'

"""
Given a text of 2300 words
It returns a time of 38 minutes
"""
def test_2300_words(''..2300..'):
==> '38 minutes'

"""
Given None as input,
Raise exception
"""
def test_None_value(None):
==> 'Please enter a string'

"""
Given an input different from a string, e.g. number
Raise exception
"""
def test_no_string_given(123):
==> 'Please enter a string'