#Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
#m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = (int(input("Введите N - количество элементов первого множества: ")))
NumList1 = []
for i in range(n):
    num = int(input("Введите num: "))
    NumList1.append(num)
print(NumList1)


m = (int(input("Введите M - количество элементов первого множества: ")))
NumList2 = []
for i in range(m):
    num = int(input("Введите num: "))
    NumList2.append(num)
print(NumList2)


NumList3 = NumList1+NumList2

print(NumList3)
for i in set(NumList3):
    if NumList3.count(i) > 1:
        print(i)