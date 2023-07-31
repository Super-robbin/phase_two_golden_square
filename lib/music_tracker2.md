Problem:
The user needs help to keep track of the music listening
The user needs to check if a track has already been listened
or not. If listened, then the track has to be added to a list.
The user also needs a program that returns a list containing the added listened tracks.

Function Signature:
The signature of a class includes:
3 different functions:

def dictionary2list(self, dictionary)
    Tranforms a dictionary into a list of tuples.

Parameters:
    dictionary: a dictionary with both listened and not listened tracks

Returns:
    Nothing

Side effects:
    No side effects

def create_listened_list(self)
    Iterates over the list of tuples, checks whether a track has been listened or not, if listened, adds the track to a new list.

Parameters:
    No parameters

Returns:
    Nothing

Side effects:
    No side effects

def return_listened_list(self)
    Returns a list of listened tracks

Parameters:
    No parameters

Returns:
    Nothing

Side effects:
    No side effects


Examples:

"""
Given a dictionary with both listened and not listened tracks
Tranforms the dictionary into a list of tuples
"""
def test_check_listened({'beyonce': 'listened', 'oasis': 'listened', 'queen': 'not listened'}):
    ==> list = [('beyonce', 'listened'), ('oasis', 'listened'), ('queen', 'not listened')]

"""
Given a list of tuples, check whether a track is listened or not listened
Create a new list with only listened tracks
Return the list
"""
def test_create_listened_list():
    ==> list = ['beyonce', 'oasis']

"""
Returns a list containing only listened tracks
"""
def return_listened_list()
    ==> list = ['beyonce', 'oasis']
