from lib.diary_class_system import Diary
from lib.diary_entry_class_system import DiaryEntry

"""
Initially there are no entries
"""
def test_initially_has_no_entries():
    all_diary = Diary()
    assert all_diary.all() == []


"""
Given I add two entries
I can see them represented in a list, with the right format
"""
def test_add_multiple_entries():
    all_diary = Diary()
    entry1 = DiaryEntry('31 July', 'Do some coding')
    entry2 = DiaryEntry('01 August', 'Go to the cinema')
    all_diary.add(entry1)
    all_diary.add(entry2)
    assert all_diary.all() == [entry1, entry2]

"""
Given I add two entries
And I call #count_words
I can get the sum of all words in the content of the diary entries
"""
def test_count_words_returns_count_of_all_words_in_all_entry_contents():
    all_diary = Diary()
    entry1 = DiaryEntry('31 July', 'Do some coding')
    entry2 = DiaryEntry('01 August', 'Go to the cinema')
    all_diary.add(entry1)
    all_diary.add(entry2)
    assert all_diary.count_words() == 7

"""
Given I add two entries with a total length of 5
And I call #reading_time with a wpm of 2
Then the total reading time shouyld be 3
"""
def test_reading_time_returns_time_to_read_all_entries():
    all_diary = Diary()
    entry1 = DiaryEntry('31 July', 'Do something')
    entry2 = DiaryEntry('01 August', 'Go get food')
    all_diary.add(entry1)
    all_diary.add(entry2)
    assert all_diary.reading_time(2) == 3

"""
Given I add two entries, one long and one short
And I call #find_the_best_entry_for_reading_time
With a wpm and minuts that means I can only read the short one
Then #find_the_best_entry_for_reading_time returns the shorter one
"""
def find_the_best_entry_for_reading_time_returns_entry_that_fits_in_time():
    all_diary = Diary()
    entry1 = DiaryEntry('31 July', 'One two three')
    entry2 = DiaryEntry('01 August', 'One two three four five six seven')
    all_diary.add(entry1)
    all_diary.add(entry2)
    assert all_diary.find_best_entry_for_reading_time(2, 3) == entry1

"""
Given I add two entries, one long and one short
And I call #find_the_best_entry_for_reading_time
With a wpm and minuts that means I cannot read that entry
Then #find_the_best_entry_for_reading_time returns None
"""
def find_the_best_entry_for_reading_time_returns_none_if_single_entry_doesnt_fit():
    all_diary = Diary()
    entry1 = DiaryEntry('31 July', 'One two three four five six seven')
    all_diary.add(entry1)
    assert all_diary.find_best_entry_for_reading_time(2, 3) == None

"""
Given I add two entries, one long and one short
And I call #find_the_best_entry_for_reading_time
With a wpm and minuts that means I could read both
Then #find_the_best_entry_for_reading_time returns the longer one
"""
def find_the_best_entry_for_reading_time_returns_entry_that_fits_in_time():
    all_diary = Diary()
    entry1 = DiaryEntry('31 July', 'One two three')
    entry2 = DiaryEntry('01 August', 'One two three four five six seven')
    all_diary.add(entry1)
    all_diary.add(entry2)
    assert all_diary.find_best_entry_for_reading_time(2, 4) == entry2