from defs import *

while True:
    print("Привет! Пройдёмся по странам и их столицам!")
    print("1 - Узнать столицу страны или наоборот,\n2 - Добавить новую страну и столицу,\n3 - Исправить ошибку,\n4 - Проверь свои знания,\n5 - nоказать все страны и столицы,\n6 - остановить программу")
    menu=input()
    if menu=="1":
        v=input("Будем искать страну по стoлице(1) или стoлицу по названию(2)? ")
        countries(stranb,v)
    elif menu=="2":
        new_key_value(stranb)

    elif menu=="3":
        mistake(stranb)

    elif menu=="4":
        test(stranb)

    elif menu=="5":
        print(stranb)

    elif menu=="6":
        print("Спасибо что воспользовались нашими услугами")
        break