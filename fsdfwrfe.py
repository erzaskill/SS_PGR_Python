def seznam():
        seznam = [1,6,2,4,3]

        print("číslo 2 se vyskytuje v seznamu: ", seznam.count(2)) #count vraci pocet vyskytu
        print("první výskyt 3: ", seznam.index(3)) #první číslo výskytu seznamu

#seznam()

#program vygeneruje do seznamu n čísel
#Program čísla vypíše
#Dále se zeptá na hodnotu, poté oznámí zda se v seznamu hodnota nachází,
#pokud ano, tak kolikrát, a na které pozici je první výskyt

import random

def seznam1():
        seznam=[]
        for i in range (10):
                seznam.append(random.randint(1,10))
                              
        print(seznam)
                              
        hodnota=int(input("jaká hodnota? "))
        
        if seznam.count(hodnota) > 0:
                print("Počet výskytů:  ", seznam.count(hodnota))
                print("první výskyt ", seznam.index(hodnota))
        else: print("hodnota není v seznamu")

        volba = input("odstranit hodnotu" + str(hodnota) + "ze seznamu ? ano - ne")
        if volba == "ano":
                for i in range(seznam.count(hodnota)): #odstranění všech výskytů dané hodnoty
                        seznam.remove(hodnota)
        print(seznam)


#seznam1()

 #Program vygeneruje do seznamu n čísel (-100,100))
 #dále nabídne možnosti : 1. výpis, 2. odstranění prvního prvku 3. konec

def seznam2():
        seznam = []
        for i in range (10):
                seznam.append(random.randint(-100,100))
        while(True):
                volba=input("1. vápis, 2. odstranění prvního prvku, 3. odstranění zadaného prvku, 4. konec")
                if volba=="1": print(seznam)
                elif volba =="2": del(seznam[0])
                elif volba == "3":
                        index = int(input("index prvku"))
                        if index >=0 and index<len(seznam):del(seznam[index])
                        else:print("index je mimo rozsah seznamu")
                elif volba =="4": break
                else:Print("Špatná volba")
#seznam2()

##program, vygeneruje do seznamu n čísel (-100,100)
##seznam se vypíše
##zobrazí průměrnou hodnotu
##Dále zjistí nadprůměrné hodnoty ve vygenerovaném seznamu
##ty vloží do nového seznamu
##Obsah nového seznamu vypíše

def seznam3():
        seznam=[]
        for i in range(10):
                seznam. append(random.randint(-100,100))
        print(seznam)
        prum= sum(seznam)/len(seznam)
        print("prumer",prum)

        seznamNadpr = []
        for prvek in seznam:
                if prvek > prum: seznamNadpr.append(prvek)
        print(seznamNadpr)

#seznam3()

#Program, vygeneruje do seznamu n čísel (-10,10)
#Program čísla vypíše
#Dále se zeptá zda chcete odstranit kladní, nebo záporné hodnoty
#Hodnoty odstraní a seznam vypíše
        
def seznam4():
        cisla=[]
        for c in range(10):
                cisla.append(random.randint(-10,10))
        print(cisla)
        
        volba = input("odstranit kladne, zaporne, neodstranit k/z/")
        c=0
        if volba =="k":
                while c<len(cisla):
                        if cisla[c]>0:
                                del(cisla[c])
                                c=-1
                        c = c +1
        elif volba =="z":
                while c< len(cisla):
                        if cisla[c]<0:
                                del(cisla[c])
                                c=-1
                        c = c +1
        print(cisla)
        print(len(cisla))
seznam4()


