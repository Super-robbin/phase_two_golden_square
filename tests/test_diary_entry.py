from lib.diary_entry import DiaryEntry

"""
Given two strings
Returns them within a formatted string
"""

def test_right_format():
    my_diary = DiaryEntry('Makers journey', 'docs collected throughout the course July')
    assert my_diary.format() == 'My Makers journey: these are the docs collected throughout the course July.'

"""
Given two strings
Returns the sum of the number of words within those strings
"""

def test_count_words():
    my_diary = DiaryEntry('makers journey', 'docs collected throughout the course July')
    assert my_diary.count_words() == 8

"""
Given an integer with number of words a user can read in a minute
Returns estimate of the reading time in minutes for the contents at
the given wpm.
"""

def test_reading_time():
    my_diary = DiaryEntry('makers journey', 'docs collected throughout the course July')
    assert my_diary.reading_time(200) == 0.03

"""
Given an integer with number of words a user can read in a minute
Returns a chunk of the contents that the user could read in the
given number of minutes.
"""

def test_reading_chunks():
    my_diary = DiaryEntry('makers journey', 'docs collected throughout the course July')
    assert my_diary.reading_chunk(200, 0.03) == "word word word word word word"