from math import ceil

class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        self.entries.append(entry)

    def all(self):
        return self.entries

    def count_words(self):
        #count_words belonging to Diary class
        #self.count_words()

        #count_words belonging to an instance of DiaryEntry
        #is self.entries[0].count_words()

        total = 0
        for entry in self.entries:
            total += entry.count_words()
        return total

    def reading_time(self, wpm):
        if self.entries == []:
            raise Exception("No entries added yet")

        word_count = self.count_words()
        return ceil(word_count / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        words_the_user_could_read = wpm * minutes
        most_readable = None
        longest_found_so_far = 0
        # readable_entries = []
        for entry in self.entries:
            if entry.count_words() <= words_the_user_could_read:
                if entry.count_words() > longest_found_so_far:
                    most_readable = entry
                    longest_found_so_far = entry.count_words()
        return most_readable
        #         readable_entries.append(entry)
        # if readable_entries == []:
        #     return None
        # return readable_entries[0]
