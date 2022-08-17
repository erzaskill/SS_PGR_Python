import random
#vypíše to seznam 10 náhodných čísel, součet čísel, průměr, max, min, seřadit
#seřadit opačně, prvni a poslední číslo
def opakSez1():
    cisla=[]
    for i in range(10):
        cisla.append(random.randint(-10,10))
        cislaK=cisla[:]
    print(cisla)
    print("součet: ", sum(cisla))
    print("průměr: ", sum(cisla)/len(cisla))
    print("maximum: ", max(cisla))
    print("minimum: ", min(cisla))
    cisla.sort()
    print("seřadit: ",cisla)
    cisla.sort(reverse=True)
    print("seřadit opačně: ",cisla)
    print("první číslo: ",cislaK[0])
    print("poslední číslo: ",cislaK[-1])

#opakSez1()



##Vygeneruj n cisel do seznamu, dále nabídne volbu:
##1. výpis seřazený vzestupně, 2. výpis seřazený sestupně
##3. konec
##výpis bude na řádku, (8; 5)
##dokud nezadáme 3 stále se bude zobrazovat volba


def opakSez2():
    cisla=[]
    pocet=int(input("Zadej počet čísel: "))
    for i in range(pocet):
        cisla.append(random.randint(-100,100))
        cislaK=cisla[:]

    volba=""
    while (volba!=3):
        volba=input("1.=výpis seřazený vzestupně, 2. výpis seřazený sestupně, 3. konec - vyber si: ")
        if volba=="1.":
            v=""
            cisla.sort()
            for i in range(pocet):
                v= v + str(cisla[i]) + "; "
            print(v)
        elif volba=="2.":
            cisla.sort(reverse=True)
            v=""
            for i in range(pocet):
                v= v + str(cisla[i]) + "; "
            print(v)
        elif volba!="3.":
            print("Zadal si špatně svou volbu.. pozor na tečku!")
        else:
            break
        

#opakSez2()



## vygeneruj n cisel (na n se zeptá) do seznamu
##dále se program zeptá, který prvek chcete vypsat,
##pokud zadáte neexistující prvek, pak to oznámí
##poté se zeptá zda chcete pokračovat


def opakSez3():
    cisla=[]
    pocet=int(input("Zadej počet čísel: "))
    for i in range(pocet):
        cisla.append(random.randint(-100,100))
        cislaK=cisla[:]

    volba=""
    while True:
        prvek=int(input("Který prvek chceš vypsat: "))
        if prvek <0 or prvek > (len(cisla)-1):
            print("Neexistující prvek")
        else:
            print(cisla[prvek])
        if input("Pokud chceš pokračovat napiš: ano: ")!="ano":
            break

        
#opakSez3()


        
##Vytvořte program, který pod sebe vypíše dny v týdnu
def opakSez4():
    dny= ["po", "út", "stř", "čt", "pá", "so", "ne"]
    
    for i in range (7):
        a=random.randint(0,6)
        s=dny[a]
        print(s)
        
        
opakSez4()


#příští týden - píšem test ze seznamu

        




























        
























        



