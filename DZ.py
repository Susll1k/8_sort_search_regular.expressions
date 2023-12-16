#1 Задание

lst=[1,2,3,6,5,4]
def InsertionSort(alist):
    for i in range(1, len(alist)):
        j = i - 1
        temp = alist[i]
        while (j >= 0 and alist[j] > temp):
            alist[j+1] = alist[j]
            j = j - 1 
        alist[j + 1] = temp
    return alist
print(lst)
print(InsertionSort(lst))

#----------------------------------------------------------------------------------------------------------------
#2 Задание

lst=[1,2,3,6,5,4]
def InsertionSort(alist):
    for i in range(1, len(alist)):
        j = i - 1
        temp = alist[i]
        while (j >= 0 and alist[j] < temp):
            alist[j+1] = alist[j]
            j = j - 1 
        alist[j + 1] = temp
    return alist
print(lst)
print(InsertionSort(lst))


#----------------------------------------------------------------------------------------------------------------
#3 Задание


a = int(input("Сколько товаров?: "))
cost=[]
for i in range(a):
    b=int(input("Стоимость: "))
    cost.append(b)
def prom(cst):
    ret=0
    for i in range(1, len(cst)):
        j = i - 1
        temp = cst[i]
        while (j >= 0 and cst[j] > temp):
            cst[j+1] = cst[j]
            j = j - 1 
        cst[j + 1] = temp

    list_len = len(cst) - len(cst) % 3

    for i in range(0, list_len, 3):
        j = cst[i:i+3]
        print()
        ret= ret + j[1] + j[2]

    if list_len != len(cst):
        g = cst[list_len:]
        ret+= g[0]

    return ret

print(prom(cost))


#----------------------------------------------------------------------------------------------------------------
#4 Задание


spisok=[9,4,1,6]
cost=[]
def min_difference(num):
    new_num = sorted(num)
    m=max(num)
    for i in range(len(num)-1):
        a= new_num[i+1] - new_num[i]
        if a < m:
            m=a
    return m
print(min_difference(spisok))


#----------------------------------------------------------------------------------------------------------------
#5 Задание


str = int(input("Сколько строк?: "))
list_str=[]
for i in range(str):
    b=input("Введите слово: ")
    list_str.append(b)

def get_longest_len(lst):
    max_len = len(lst[0])
    for word in lst:
        if len(word) > max_len:
            max_len = len(word)
    
    return max_len

def update_word(word, max_len):
    num_of_stars = max_len - len(word)
    return "*"*num_of_stars + word

max_len = get_longest_len(list_str)
for word in list_str:
    print(update_word(word, max_len))





#----------------------------------------------------------------------------------------------------------------
#6 Задание


lst = [-3,-2,1,2,3,4]

num_need=-sum(lst)
lst.append(num_need)
print(f"Число, которое нам нужно чтобы сумма элементов с положительными значениями стала бы равна модулю суммы элементов с отрицательными значениями, равна: {num_need}")
print(lst)




#----------------------------------------------------------------------------------------------------------------
#Регулярные выражения

import re

text = "Апельсин; john.doe@example.com | Банан: jsmith@mail.net ; Вишня, jane_doe123@gmail.com | Дыня; contact@website.org"

# Задание 1 
res1 = re.findall(r"@\w+\.\w+", text)
print(res1)

# Задание 2
res2 = re.findall(r"[АУЕОЫЭЯИЮЁ][А-Яа-я]+", text)
print(res2)

# Задание 3
res3 = re.split(r"[,:;|]", text)
print(res3)
