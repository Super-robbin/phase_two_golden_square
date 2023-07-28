from lib.grammar_stats import *

"""
Given a string that begins with a capital letter
and ends with a sentence-ending punctuation mark
Return True
"""

def test_starts_with_capital_ends_with_punctuation():
    my_str = GrammarStats()
    assert my_str.check('Hello, my name is Bob. Pleasure to meet you!') == True

"""
Given a string
Returns the integer number of the percentage
of the tests passed
"""

def test_percentage_good():
    my_str = GrammarStats()
    my_str.check('Hey!')
    my_str.check('Hey')
    my_str.check('nope.')
    my_str.check('hi')
    my_str.check('bOb.')
    assert my_str.percentage_good() == 20