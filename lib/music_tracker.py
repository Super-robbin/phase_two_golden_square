class MusicTracker:
    def __init__(self):
        self.list = []

    def add(self, track):
        self.list.append(track)

    def return_list(self):
        return self.list