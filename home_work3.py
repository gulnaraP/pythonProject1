#3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
#Option 1
my_list = ['a', 'b', [1, 2, 3], 'd']
print(my_list[2][0])
print(my_list[2][1])
print(my_list[2][2])

# Option 2. Using deconstruction
my_list = ['a', 'b', [1, 2, 3], 'd']
list1 = my_list[2]
print(*list1, sep='\n')

#3.2. Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#   - получите сумму всех чисел,
#   - распечатайте все строки, где есть буква 'a'

list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
print('original list:',list_1)
print('Sum of all numbers:',sum([x for x in list_1 if type(x) == int]))
print('All words with a:',[y for y in list_1 if type(y) == str and "a" in y])

#3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж

#print(tuple(['cat', 'dog', 'horse', 'cow']))


#3.4.Напишите программу, которая определяет, какая семья больше.
#      1) Программа имеет два input() - например, family_1, family_2.
#      2) Членов семьи нужно перечислить через запятую.
#     Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
family_1 = tuple(input('Введите текст через запятую: ').split(','))
family_2 = tuple(input('Введите текст через запятую: ').split(','))
if len(family_1) == len(family_2):
    print('Equal')
elif len(family_1) > len(family_2):
    print('family_1')
else:
    print('family_2')

#3.6.Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# Option 1
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
result = 0
for x in my_dictionary:
    result += my_dictionary[x]
print(result)


# Option 2
my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print(sum(my_dictionary.values()))


#3.7.Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
new_list = set([1, 2, 3, 4, 5, 3, 2, 1])
print(new_list)

#3.8.Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#     - найдите значения, которые встречаются в обоих множествах
#     - найдите значения, которые не встречаются в обоих множествах
#     - проверьте являются ли эти множества подмножествами друг друга
set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
print(set1.intersection(set2))
print(set1.symmetric_difference(set2))
print(set1.issubset(set2))
print(set2.issubset(set1))