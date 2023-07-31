class MusicTracker2:
    def __init__(self):
        pass

    def dictionary2list(self, dictionary):
        list = [(k, v) for k, v in dictionary.items()]
        return list

    def created_listened_list(self, list):
        lst = []
        for track in list:
            if track[-1] == 'listened':
                lst.append(track[0])
        return lst

    def dictionary2listenedlist(self, dictionary):
        # lst = self.dictionary2list(dictionary)
        return self.created_listened_list(self.dictionary2list(dictionary))