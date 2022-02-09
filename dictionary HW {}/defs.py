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
    country=(input("Введите страну: ")).capitalize()
    capital=(input("Введите столицу: ")).capitalize()
    new={country:capital}
    stranb.update(new)
    print(stranb)
    return d,new


def mistake(d:dict):
    print("В каком слове ошибка?, напишите название страны и новую столицу")
    s=input()
    del stranb[s]
    print(stranb)
    new_key_value(stranb)
    return d

def hui(d:dict):
    print()
    s=random.choice(list(d.keys()))
    print(s)