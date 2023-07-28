class GrammarStats:
    def __init__(self):
        self.special = ['!', '?', '.']
        self.list = []
        
    def check(self, text):
        if any([c in self.special for c in text[-1]]) and text[0].isupper():
            self.list.append('P')
            return True
        else:
            self.list.append('F')
            return False

    def percentage_good(self):
        passed = self.list.count('P')
        length = len(self.list)
        return (passed / length) * 100