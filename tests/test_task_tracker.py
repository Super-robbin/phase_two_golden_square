from lib.task_tracker import *

"""
Given a string with todo tasks
Add them to a list
"""
def test_add_todo_tasks():
    my_str = TaskTracker()
    my_str.add('laundry')
    my_str.add('shopping')
    my_str.add('cooking')
    assert my_str.return_list() == ['laundry', 'shopping', 'cooking']

"""
Given a string with todo tasks
Add them to a list
"""
def test_empty_list():
    my_str = TaskTracker()
    assert my_str.return_list() == []

"""
Given a string with completed tasks
Remove them from the list that contains todo tasks
Return the list with only todo tasks
"""

def test_remove_completed_tasks():
    my_str = TaskTracker()
    my_str.add('laundry')
    my_str.add('shopping')
    my_str.add('cooking')
    my_str.remove('shopping')
    my_str.remove('cooking')
    assert my_str.return_list() == ['laundry']