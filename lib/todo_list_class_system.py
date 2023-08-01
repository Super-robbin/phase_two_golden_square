
class TodoList:
    def __init__(self):
        self.todos_list = []

    def add(self, todo):
        self.todos_list.append(todo)

    def incomplete(self):
        incomplete = []
        for task in self.todos_list:
            if task.complete == False:
                incomplete.append(task)
        return incomplete

    def complete(self):
        complete = []
        for task in self.todos_list:
            if task.complete == True:
                complete.append(task)
        return complete

    def give_up(self):
        for task in self.todos_list:
            if task.complete == False:
                task.complete = True
        
