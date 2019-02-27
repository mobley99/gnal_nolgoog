from googlon import Googlon

class Solution:

    def __init__(self):
        self.text = None
        self.prepositions = 0
        self.verbs = 0
        self.subjuntives = 0
        self.ordered = []
        self.pretty_numbers = 0
    
    def set_text_io(self):
        """
        Read from standard input
        """
        self.text = input().split(' ')

    def set_text_str(self, txt):
        """
        Read from standard input
        """
        self.text = txt.split(' ')
    
    def set_text_file(self, filename):
        """
        Read from file
        """
        self.text = []
        with open(filename,'r') as f:
            for line in f:
                for word in line.split():
                    self.text.append(word)
    
    def clear_chars(self):
        """
        Clear \n 
        """    
        for i in range(len(self.text)):
            self.text[i] = self.text[i].replace('\n','')
        self.text = [word for word in self.text if word]
    
    def run(self):
        self.clear_chars()
        if self.text:
            for word in self.text:
                if Googlon.is_prep(word):
                    self.prepositions += 1
                if Googlon.is_verb(word):
                    self.verbs += 1
                    if Googlon.is_subjunctive(word):
                        self.subjuntives += 1
                if Googlon.is_pretty_number(Googlon.number(word)):
                    self.pretty_numbers += 1

            self.ordered = Googlon.sort_text(self.text)
        
        print('Prepositions: {}'.format(self.prepositions))
        print('Verbs: {}'.format(self.verbs))
        print('Subjunctive verbs: {}'.format(self.subjuntives))
        print('Ordered Text: {}'.format(self.ordered))
        print('Pretty numbers: {}'.format(self.pretty_numbers))
        

        


