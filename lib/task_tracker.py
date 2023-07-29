class TaskTracker:
    def __init__(self):
        self.list = []
        
    def add(self, task):
        self.list.append(task)
        

    def return_list(self):
        return self.list
    
    def remove(self, task):
        return self.list.remove(task)
