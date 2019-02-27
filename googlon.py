from const import sort_dict_numeric
from const import sort_dict_alpha
from const import foo_letters
from const import bar_letters
from verbs import Verb

"""

foo letters: u, d, x, s, m, p, f
bar letters: foo_letters complement
prep:  6 letters which end in a foo letter and do not contain the letter u.
verbs: words of 6 letters or more that end in a bar letter
subjunctive verb: if is verb and starts in a bar letter
order keys: sxocqnmwpfyheljrdgui
numbers: base 20, where each letter is a digit .
pretty number:  it is greater than or equal to 81827 and it is divisible by 3

"""

class Googlon:

    def valid(func):
        def f(*args):
            if args[0]:
                return func(*args)
            else:
                return False
        return f

    @staticmethod
    @valid
    def is_prep(word):
        prop1 = len(word) == 6
        prop2 = word[-1] in foo_letters
        prop3 = 'u' not in word
        return prop1 and prop2 and prop3

    @staticmethod
    @valid         
    def is_verb(word):
        prop1 = len(word) >= 6
        prop2 = word[-1] in bar_letters
        return prop1 and prop2
    
    @staticmethod
    @valid
    def is_subjunctive(word):
        return word[0] in bar_letters

    @staticmethod
    def sort_text(words):
        word_ = []
        words = list(set(words))
        for w in words:
            n = ''
            for l in w:
                n += sort_dict_alpha[l]
            word_.append(n)
        words = list(zip(words,word_))
        words = sorted(words,key=lambda x: x[1])
        return list(list(zip(*words))[0])

    @staticmethod
    def number(word):
        number = 0
        for i in range(len(word)):
            number += 20 ** i * sort_dict_numeric[word[i]]
        return number
    
    @staticmethod
    def is_pretty_number(number):
        return number >= 81827 and number % 3 == 0

