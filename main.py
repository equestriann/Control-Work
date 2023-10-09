# Вариант №1
def make_new_array(string):
    array_ = []
    for a in string:
        if len(a) <= 3:
            array_.append(a)

    return array_

strings = [
    ['hello', '2', 'world', ':-)'],
    ['1234', '1567', '-2', 'computer science'],
    ['Russia', 'Denmark', 'Kazan']
]

for i in strings:
    print(make_new_array(i))


# Вариант №2
def make_new_array_from_input():
    list_of_strings = input('Напишите что-нибудь: ')
    array_ = []
    for b in list_of_strings.split():
        if len(b) <= 3:
            array_.append(b)

    return array_
