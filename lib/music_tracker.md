Problem:
The user needs help to keep track of the music listening
The user wants a program that can add listened tracks to a list.
The user also needs a program that returns a list containing the
added listened tracks.

Function Signature:
The signature of a class includes:
2 different functions:

def add(self, string)
    Adds listened tracks to a list

Parameters:
    string: string with listened tracks

Returns:
    Nothing

Side effects:
    No side effects

def return_list(self)
    Return a list with all the added listened tracks

Parameters:
    No parameters

Returns:
    Return a list with all the added listened tracks

Side effects:
    No side effects


Examples:

"""
Given a string with listened tracks
Add them to a list
"""
def test_add_listened_tracks('beyonce, oasis, queen'):
    ==> list = ['beyonce', 'oasis', 'queen']

"""
Return a list with the added listened tracks
"""
def test_return_list():
    ==> list = ['beyonce', 'oasis', 'queen']
