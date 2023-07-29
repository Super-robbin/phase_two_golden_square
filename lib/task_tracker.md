Problem:
The user needs help to keep track of the tasks
The user wants a program that can add todo tasks to and see a list of them.
The user also needs a program that marks tasks as completed in a list.
Finally, the user wants to remove the completed tasks from the list.

Function Signature:
The signature of a class includes:
3 different functions:

def add(self, string)
    Adds todo tasks to a list

Parameters:
    string: string with todo tasks

Returns:
    Nothing

Side effects:
    No side effects

def return_list(self)
    Return a list with all the added todo tasks

Parameters:
    No parameters

Returns:
    Return a list with all the added todo tasks

Side effects:
    Exception for empty list

def remove(self, string)
    Remove completed tasks from the list

Parameters:
    string: string with completed tasks

Returns:
    Return a list with just todo tasks

Side effects:
    No side effects


Examples:

"""
Given a string with todo tasks
Add them to a list
"""
def test_add_todo_tasks('laundry, shopping, cooking'):
    ==> list = ['laundry', 'shopping', 'cooking']

"""
Return a list with the added todo tasks
"""
def test_return_list():
    ==> list = ['laundry', 'shopping', 'cooking']

"""
Given a string with completed tasks
Remove them from the list that contains todo tasks
Return the list with only todo tasks
"""

def test_remove_completed_tasks('shopping', 'cooking')
    ==> list = ['laundry']