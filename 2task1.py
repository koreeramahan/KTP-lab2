import random

my_number=random.randint(0,50);
a=float(input('Попробуйте ввести число a, которое больше загаданного числа:\n'))
while (a<=my_number):
	a=float(input('Введите число a еще раз:\n'))
print('Введённое число а больше загаданного. Загаданное число = ',my_number)
