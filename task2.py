def task2_1(string):
    return string.translate(string.maketrans({"'": "\"", "\"": "'"}))


def task2_2(string: str):
    return string == string[::-1]


def task2_4(s: str, index: list):
    new_list = list
    begin = 0
    for ind in index:
        if ind > len(s):
            print("Bad index")
        else:
            new_list.append(s[begin:ind])
            begin = ind
    new_list.append(s[begin:])
    return new_list


def task2_5(s):
    tuplep = ()
    for index in str(s):
        tuplep += (int(index), )
    return tuplep


def task2_6(s: str):
    big = s.split()
    return max(big, key=len)


def task2_7(s: list):
    new_list = []
    for index in s:
        mult = 1
        for ind in s:
            mult *= ind
        new_list.append(int(mult / index))
    return new_list


def task2_8(lst: list):
    if len(lst) == 1:
        return None
    return list(zip(lst, lst[1:]))
