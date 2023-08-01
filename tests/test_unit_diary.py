from lib.diary_class_system import Diary
import pytest

"""
Initially there are no entries
"""
def test_initially_has_no_entries():
    all_diary = Diary()
    assert all_diary.all() == []

"""
Initially, word count is zero
"""
def test_initially_has_no_entries():
    all_diary = Diary()
    assert all_diary.count_words() == 0

"""
Initially, #reading_time should raise an error
"""
def test_initially_reading_time_raises_error():
    diary = Diary()
    with pytest.raises(Exception) as err:
        diary.reading_time(2)
    assert str(err.value) == 'No entries added yet'
