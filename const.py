"""

Definition of sort keys, foo and bar letters sets

"""


sort_dict_alpha = dict()
sort_dict_numeric = dict()
sort_keys = 'sxocqnmwpfyheljrdgui'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for kv in range(len(sort_keys)):
    sort_dict_alpha[sort_keys[kv]] = alphabet[kv]

for kv in range(len(sort_keys)):
    sort_dict_numeric[sort_keys[kv]] = kv

foo_letters = ['u', 'd', 'x', 's', 'm', 'p', 'f']
bar_letters = [letter for letter in sort_keys if letter not in foo_letters]


