#Задание 2.1
#Напишите программу, которая проверяет здоровье персонажа в игре.
#Если оно равно или меньше нуля, выведите на экран False, в противном случае True.
health = int(input('Введите уровень здоровья вашего персонажа: '))
if health > 0:
    print('True')
else:
    print('False')

#Задание 2.2
#Напишите программу, которая проверяет является ли введенное число четным. Если да, выведите на экран текст “Четное”, а иначе - “Нечетное”
#number = int(input("Введите любое число:"))
if number%2:
         print('Нечетное')
else:
         print('Четное')

#Задание 2.3
#Напишите программу, которая проверяет является ли год високосным. Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008) и не являются столетиями (500, 600). Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)
# С вложенными условиями
 year = int(input('Enter year:'))
 if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
     print('This is leap year!')
 else:
     print('This is not leap year!')
#Задание 2.4
#Напишите программу, которая печатает введенный текст заданное количество раз, построчно. Текст и количество повторений нужно ввести с помощью inpit()

# С циклом while/while loop

text = input("Enter your text: ")
num = int(input('Enter the number of repetitions: '))
i = 1
while i <= num:
    print(text)
    i += 1

# С циклом for/for loop

num = int(input('Enter the number of repetitions: '))
for i in range(1, num+1):
    print(i, text)
