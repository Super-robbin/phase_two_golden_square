from lib.music_tracker import *
"""
Given a string with listened tracks
Add them to a list
"""
def test_add_listened_tracks():
    my_str = MusicTracker()
    my_str.add('beyonce')
    my_str.add('oasis')
    my_str.add('queen')
    assert my_str.return_list() == ['beyonce', 'oasis', 'queen']

"""
Return a list with the added listened tracks
"""
def test_return_list():
    my_str = MusicTracker()
    my_str.add('beyonce')
    my_str.add('oasis')
    my_str.add('queen')
    assert my_str.return_list() == ['beyonce', 'oasis', 'queen']