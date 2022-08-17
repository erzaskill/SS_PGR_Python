def pocitadlo(): 
    x=float(input("zadej hodnotu x: "))
    y=float(input("Zadej hodnotu y: "))
    priklad= (x*y)
    if priklad == 0:
        print("chyba")
    else:
        print(1/priklad)

#pocitadlo()

def rozmezi():
    x= float(input("Zadej hodnotu: "))
    if x<1:
        print("číslo není v zadaném intervalu")
    elif x>100:
        print("číslo není v zadaném intervalu")
    else:
        print("číslo je v zádaném intervalu")

#rozmezi()

def vstupne():
    vek=float(input("Zadej svůj věk: "))
    if vek <=0 or vek >130:
        print("chyba ve věku")
    elif vek <= 10:
        print("Dej mi 300Kč! ")
    elif vek <= 18:
        print("Dej mi 500Kč! ")
    elif vek <=60:
        print("Dej mi 1000Kč! ")
    else:
        print("Dej mi 400Kč! ")

#vstupne()

def kalkulacka():
    a= float(input("a: "))
    b= float(input("b: "))
    volba= input("vyber( +, -, *, /) : ")
    if volba =="+":
        print(a+b)
    elif volba=="-":
        print(a-b)
    elif volba=="*":
        print(a*b)
    elif volba=="/":
        if b!=0:
            print(a/b)
        else:
            print("nulou nelze dělit!")
    else:
        print("špatná volba")

#kalkulacka()

def inicialy():
    
    jmeno= input("Zadej své jméno: ")
    prijmeni= input("Zadej své příjmení: ")
    inicialy= jmeno[0] + "." + prijmeni[0] + "."
    if len(jmeno)<3 and len(prijmeni)<3:
        print("chyba")
    else:
        print(inicialy)

inicialy()

        

              
