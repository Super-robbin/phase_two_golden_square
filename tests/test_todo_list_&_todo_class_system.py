from lib.todo_class_system import Todo
from lib.todo_list_class_system import TodoList

"""
Given I add two tasks to do to a list,
I can return a new list of incompleted tasks
"""
def test_add_multiple_todo_tasks():
    tasks = TodoList()
    task1 = Todo('Cook the dinner')
    task2 = Todo('Clean the house')
    tasks.add(task1) == 'Cook the dinner'
    tasks.add(task2) == 'Clean the house'
    assert tasks.incomplete() == [task1, task2]

"""
Given I add three tasks to do to a list, I mark two as completed
I add them to a new list that just contains completed tasks
I return the new list
"""
def test_add_multiple_completed_tasks():
    tasks = TodoList()
    task1 = Todo('Cook the dinner')
    task2 = Todo('Clean the house')
    task3 = Todo('Buy the grocery')
    tasks.add(task1) == 'Cook the dinner'
    tasks.add(task2) == 'Clean the house'
    tasks.add(task3) == 'Cook the dinner'
    task1.mark_complete()
    task2.mark_complete()
    assert tasks.complete() == [task1, task2]

"""
Given I add three tasks to do to a list
I mark them all as completed
"""
def test_mark_all_tasks_completed():
    tasks = TodoList()
    task1 = Todo('Cook the dinner')
    task2 = Todo('Clean the house')
    task3 = Todo('Buy the grocery')
    tasks.add(task1) == 'Cook the dinner'
    tasks.add(task2) == 'Clean the house'
    tasks.add(task3) == 'Cook the dinner'
    tasks.give_up()
    assert tasks.complete() == [task1, task2, task3]