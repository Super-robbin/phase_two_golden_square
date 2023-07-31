from lib.music_tracker2 import *

"""
Given a dictionary with both listened and not listened tracks
Tranforms the dictionary into a list of tuples
"""
def test_dictionary2list():
    mk2 = MusicTracker2()
    dictionary = {'beyonce': 'listened', 'oasis': 'listened', 'queen': 'not listened'}
    assert mk2.dictionary2list(dictionary) == [('beyonce', 'listened'), ('oasis', 'listened'), ('queen', 'not listened')]

"""
Given a list of tuples, check whether a track is listened or not listened
Create a new list with only listened tracks
"""
def test_create_listened_list():
    mk2 = MusicTracker2()
    list = [('beyonce', 'listened'), ('oasis', 'listened'), ('queen', 'not listened')]
    assert mk2.created_listened_list(list) == ['beyonce', 'oasis']

"""
Returns a list containing only listened tracks
"""
def test_dictionary2listenedlist():
    mk2 = MusicTracker2()
    dictionary = {'beyonce': 'listened', 'oasis': 'listened', 'queen': 'not listened'}
    assert mk2.dictionary2listenedlist(dictionary) == ['beyonce', 'oasis']