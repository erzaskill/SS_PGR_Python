def TEST():
    otazka=""
    a=1
    min=654564654
    soucet=0
    pocet=0
    opacnaHod=""
    hodnota=""
    while otazka!="Ne": 
        a=float(input("Zadej číslo: "))
        otazka=input("Chceš pokračovat? ")
        soucet= soucet + a
        pocet= pocet + 1
        hodnota= hodnota + str(a) + " ;"
        opacnaHod= str(a) + " ;" + opacnaHod
        if min>a:
            min=a
    volba=input("Vyber si mezi: 1. Výpis čísel 2.Opačný výpis 3. Průměrná a min hodnota")
    if volba== "1.":
        print("Hodnoty: ", hodnota)
    elif volba== "2.":
        print("Opačný výpis: ",opacnaHod)
    elif volba== "3.":
        print("Průměrná hodnota: " + str(soucet/pocet) + "\nMinimální hodnota: " + str(min))
TEST()
