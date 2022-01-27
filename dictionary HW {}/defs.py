
countries_dict={'Albaaniar':'Tirana', 'Andorra':'Andorra-la-Vella', 'Armeenia':'Jerevan', 'Aserbaidjaan':'Bakuu', 'Austria':'Viin', 'Belgia':'Brussel', 'Bosnia-ja-Hertsegoviina':'Sarajevo', 'Bulgaaria':'Sofia', 'Eesti':'Tallinn', 'Gruusia':'Thbilisi', 'Hispaania':'Madrid', 'Horvaatia':'Zagreb', 'Iirimaa':'Dublin', 'Island':'Reykjavk', 'Itaalia':'Rooma', 'Kasahstan':'Astana', 'Kreeka':'Ateena', 'Kupros':'Nikosia', 'Leedu':'Vilnius', 'Liechtenstein':'Vaduz', 'Luksemburg':'Luxembourg', 'Lati':'Riia', 'Madalmaad':'Amsterdam', 'Makedoonia':'Skopje', 'Malta':'Valletta', 'Moldova':'Chisinau', 'Monaco':'Monaco', 'Montenegro':'Podgorica', 'Norra':'Oslo', 'Poola':'Varssavi', 'Portugal':'Lissabon', 'Prantsusmaa':'Pariis', 'Rootsi':'Stockholm', 'Rumeenia':'Bukarest', 'Saksamaa':'Berliin', 'San-Marino':'San-Marino', 'Serbia':'Belgrad', 'Slovakkia':'Bratislava', 'Sloveenia':'Ljubljana', 'Soome':'Helsingi', 'Suurbritannia':'London', 'Dveits':'Bern', 'Taani':'Kopenhaagen', 'Tbehhi':'Praha', 'Turgi':'Ankara', 'Ukraina':'Kiiev', 'Ungari':'Budapest', 'Valgevene':'Minsk', 'Vatikan':'Vatican', 'Venemaa':'Moskva'}
    
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
    countries_dict.update(new)
    print(countries_dict)
    return d,new