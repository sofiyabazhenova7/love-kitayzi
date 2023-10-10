def to_dict(lst):
    return {element: element for element in lst}
print(to_dict([1, 2, 3, 4]))




my_dict = {'first_one': 'we can do it'}
def biggest_dict(**kwargs):
    my_dict.update(**kwargs)
biggest_dict(c=2, g=21, l=11, d=91)
biggest_dict(name='Ваня', age=24, weight=61, eyes_color='blue')
print(my_dict)




def count_it(sequence):
    num_frequency = {int(q): sequence.count(q) for q in sequence}
    sorted_num_frequency = sorted(num_frequency.items(), key=lambda element: element[1])
    return dict(sorted_num_frequency[-3:])
print(count_it('1111111111222'))
print(count_it('123456789012133288776655353535353441111'))
print(count_it('007767757744331166554444'))




from collections import OrderedDict
dct = OrderedDict({1: 1, 2: 2, 3: 3, 4: 4, 5: 5})
first = list(dct.items())[0]
last = list(dct.items())[-1]
dct.move_to_end(key=first[0])
dct.move_to_end(key=last[0], last=False)
second = list(dct.items())[1]
del dct[second[0]]
dct['new_key'] = 'new_value'
my_dict
{5: 5, 3: 3, 4: 4, 1: 1, 'new_key': 'new_value'}
id(my_dict)
17128656
