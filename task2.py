def task2_2(string: str):
    return string == string[::-1]


def task2_3(string: str):
    b = []
    a = 0
    for index in string:
        if index == ' ':
            a = len(index) - a
            b.append(string[a:len(index)])


def main():
    print(task2_2(input()))


if __name__ == '__main__':
    main()