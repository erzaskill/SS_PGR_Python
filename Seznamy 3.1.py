##Program načte jméno a potom příjmení
##Spoji je to retezce nasledujicim zpusobem: Petr Novak
##Takto upraveny retezec vlozi do seznamu Lide
##Pote se zepta zda pokracovat, pokud ano opet nacte, jinak obsah seznamu zobrazi


def seznam():
        Lide=[]
        while (True):
                jmeno = input("Zadej jméno: ")
                prijmeni = input("Zadej prijmeni: ")
                clovek = jmeno[0].upper() + jmeno[1:].lower() + " "
                clovek = clovek + prijmeni[0].upper() + prijmeni[1:].lower()
                Lide.append(clovek)
                if input ("a = pokracovat"). lower()!="a":break
        print(Lide)

#seznam()

##Program načte jméno a potom příjmení
##Spoji je to retezce nasledujicim zpusobem: Petr Novak
##Takto upraveny retezec vlozi do seznamu Lide
##Pote se zepta zda pokracovat, pokud ano opet nacte, jinak obsah seznamu zobrazi
##volby: 1. vypis pod sebe, 2. hledani (tadare hnebi a program zjisti zda je v seznamu
##3. konec

def seznam1():
        Lide=[]
        while (True):
                jmeno = input("Zadej jméno: ")
                prijmeni = input("Zadej prijmeni: ")
                clovek = jmeno[0].upper() + jmeno[1:].lower() + " "
                clovek = clovek + prijmeni[0].upper() + prijmeni[1:].lower()
                Lide.append(clovek)
                if input ("a pokracovat"). lower()!="a":break
        while (True):
                volba = input("1. vypis, 2. vyhledani, 3. konec")
                if volba == "1":
                        for clovek in Lide:
                                print(clovek)
                elif volba == "2":
                        jmeno = input("Zadej jmeno hledane osoby: ")
                        if jmeno in Lide:print("je v seznamu")
                        else: print("neni v seznamu")
                elif volba == "3":break
                else:print("neexistující volba")



seznam1()


##Program do seznamu cisel vygeneruje 10 cislic v intervalu 1 az 100
##Dale se zepta uzivatele na cislo 1 do 100
##Pote oznami zda se cislo v seznamu nachazi nebo ne


def seznam2():
        import random
        cisla=[]
        for i in range(10):
                cisla.append(random.randint(1,100))
        cislo = input ("Zadej číslo 1-100")
        
        if cislo in cisla:
                print("je v seznamu")
        else:print ("neni v seznamu")
        print(cisla)
        


#seznam2()



##Program do seznamu cisel vygeneruje 10 cislic v intervalu 1 az 100
##Dale se zepta uzivatele na cislo 1 do 100
##Pote oznami zda se cislo v seznamu nachazi nebo ne
##Rozsirte, hada se tak dlouho dokud cislo nenajde, po uhadnuti se zobrazi pocet pokusu


def seznam3():
        import random
        cisla=[]
        for i in range(10):
                cisla.append(random.randint(1,100))
        print(cisla)

        pocet = 0 
        while(True):
                cislo = int(input("Zadej číslo 1-100"))
                pocet = pocet + 1
                if cislo in cisla:
                        print("je v seznamu")
                        print("pocet pokusu ", pocet)
                        break
                else:print ("neni v seznamu")

seznam3()

#Zadejte text, program ho upraví tak ze se budou stridat velke a male pismena
#napr. ahoj, aHoJ


def seznam4():
        text= input("Zadej text")
