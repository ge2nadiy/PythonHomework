import string as s
import collections


def task3_2(intg):
    return {intg: intg ** 2 for intg in range(1, intg + 1)}


def task3_3(s):
    d = collections.defaultdict(int)
    for c in s:
        d[c] += 1
    return d


dict1 = {'a': 100, 'b': 200, 'c': 100}
dict2 = {'a': 200, 'b': 300, 'd': 200}
dict3 = {'a': 300, 'b': 100, 'c': 100}


def task3_4(*dicts):
    new_dict = {}
    for d in dicts:
        for key, value in d.items():
            new_dict[key] = new_dict.get(key, 0) + value
    return new_dict
