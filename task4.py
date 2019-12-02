import re
import csv
from collections import Counter


def task4_1():
    with open("unsorted_names.txt", 'r') as rf:
        mass = rf.readlines()
    new_mass = sorted(mass)
    with open("sorted_names.txt", 'w') as wf:
        for mas in new_mass:
            wf.write(mas)


def task4_2(number_of_words=3):
    with open("lorem_ipsum.txt", 'r') as rf:
        s = rf.read()
        words = re.findall(r'\w+', s)

    cap_words = [word.lower() for word in words]
    word_counts = Counter(cap_words)
    print(type(word_counts))
    print(word_counts.most_common(number_of_words))


#task4_3
def get_top_performers(file_path, number_of_top_students = 5):
    with open(file_path) as rf:
        reader = csv.reader(rf)
        next(reader, None)
        sorted_list = sorted(list(reader), key = lambda student: student[2], reverse = True)
        return list(map(lambda student: student[0], sorted_list[:number_of_top_students]))
    
def sort_by_age(file_path):
    with open(file_path) as rf:
        with open('data/sorted_students.csv', 'w') as wf:
            reader = csv.reader(rf)
            header = next(reader, None)
            sorted_list = sorted(list(reader), key = lambda student: student[1], reverse = True)
            
            writer = csv.writer(wf)
            writer.writerow(header)
            writer.writerows(sorted_list)

file_path = 'data/students.csv'
print(get_top_performers(file_path))

file_path = 'data/students.csv'
sort_by_age(file_path)

#task4_4
a = "I am global variable!"

def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():

        a = "I am local variable!"
        print(a)

    return inner_function

enclosing_funcion()()