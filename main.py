# Вариант №1
def make_new_array(string):
    array_ = []
    for i in string:
        if len(i) <= 3:
            array_.append(i)

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
    pass
