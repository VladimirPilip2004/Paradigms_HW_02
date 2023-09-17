# Домашнее задание к семинару №2
# Условие:
# На вход подается число n.
# Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.
# Пример вывода:
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# 1 * 6 = 6
# ..
# 1 * 9 = 9

def multiplicationTable():
	for i in range(1, n+1):
		print(1, "*", i, "=", i)
	
n = int(input("Введите число N: "))
result = multiplicationTable()		
print(result)

# В этой программе присутствует процедурная и структурная парадигма
# Структурная парадигма потому что, используется  цикл for и отсутствует goto.
# Процедурная парадигма потому что, используется процедура multiplicationTable().