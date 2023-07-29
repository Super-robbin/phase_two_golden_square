import math

class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def format(self):
        return f'My {self.title}: these are the {self.contents}.'

    def count_words(self):
        return len(self.title.split()) + len(self.contents.split())
        
    def reading_time(self, wpm):
        words = self.contents.split()
        word_count = len(words)
        return word_count / wpm

    def reading_chunk(self, wpm, minutes):
        chunk_of_words = int(wpm * minutes)
        text = ' '.join(['word' for i in range(1, chunk_of_words + 1)])
        return text