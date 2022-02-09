import random
stranb={}
file=open("rig-pea.txt","r")
for line in file:
    k,v=line.strip().split(":")
    stranb[k.strip()]=v.strip()
   

    
def countries(d:dict, v:int):
    keys_list=(list(d.keys()))
    values_list=(list(d.values()))
    if v=="1":
        mas=[]
        capital=(input("Введи столицу: ")).capitalize()
        capital.title()
        for i in values_list:
            if i==capital:
                for i in range(len(values_list)):
                    if values_list[i]==capital:
                        mas.append(int(i))
                        print("Страна -", keys_list[i],"<-->", "Cтолица -", values_list[i])
    else:
        country=(input("Введите страну: ")).capitalize()
        a=d.get(country)
        print("Страна -", country ,"<-->", "Cтолица -", a)
        return dict 

def new_key_value(d:dict):
    new={}
    a=""
    country=(input("Введите страну: ")).capitalize()
    capital=(input("Введите столицу: ")).capitalize()
    a += str(country) + ":" + str(capital)
    new={country:capital}
    stranb.update(new)
    file=open("rig-pea.txt","a")
    file.write("\n"+a)
    print(stranb)
    return d,new


def mistake(d:dict):
    print("В какой стране ошибка?, напишите название страны и новую столицу")
    s=input()
    del stranb[s]
    print(stranb)
    str(new_key_value(stranb))
    return d,a

def test(d:dict):
    score = 0
    list=[]
    for element in stranb.keys():
        list.append(element)
    for vopros in range(11):
        rnd_element = random.sample(list,1)[0]
        print(rnd_element)
        vast = input("Ответ= ")
        vopros += 1
        if vast == stranb[rnd_element]:
            print("Правильный ответ")
            score = score+1
        else:
            print("Не правильный ответ")
    print("Смотрим результаты?")
    print("1-da,2-net")
    vastvast=int(input("Введите ваш ответ= "))
    if vastvast not in [1,2]:
        print("Пожалуйста выбирайте среди данных вариантов!")
    else:
        if vastvast==1:
            results=((score/11)*100)
            print("Ваше знание столиц и стран ровняется",results,"%")
        else:
            print("Спасибо что воспользовались")