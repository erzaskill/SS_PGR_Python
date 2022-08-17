def zkousimfor():
    pocet=int(input("Kolik čísel se má vypsat??"))
    a=0
    hodnota=""
    zaphodnota=""
    zapsoucet=0
    zappocet=0
    soucet=0
    hodnotaodzadu=""
    zaphodnotaodzadu=""
    max=-5456465
    min=6464654564
    for i in range(pocet):
        a=float(input("Zadej číslo: "))
        soucet= soucet + a
        hodnota= hodnota + str(a) + "; "
        hodnotaodzadu= str(a) + "; " + hodnotaodzadu
        if a < 0:
            zaphodnota= zaphodnota + str(a) + "; "
            zapsoucet= zapsoucet + a
            zappocet= zappocet + 1
            zaphodnotaodzadu= str(a) + "; " + zaphodnotaodzadu
        if a < min:
            min= a
        if a > max:
            max= a
    print("Zap. Hodnoty od zadu: " + str(zaphodnotaodzadu[0:len(zaphodnotaodzadu)-2]) + "\nHodnoty od zadu: " + str(hodnotaodzadu[0:len(hodnotaodzadu)-2]) + "\nPrůměr Záp. Hodnot: " + str(zapsoucet/zappocet))
    print("Zap.Hodnoty: " + str(zaphodnota[0:len(zaphodnota)-2]) + "\nHodnoty: " + str(hodnota[0:len(hodnota)-2]) + "\nPrůměr: " + str(soucet/pocet) + "\nMax. hodnota: " + str(max) + "\nMin. Hodnota: " + str(min))

#zkousimfor()

import random
def nahodnacisla():
    a=0
    pocet=int(input("Kolik čísel se má vypsat??"))
    hodnota=""
    hodnotaodzadu=""
    max=-255465456
    min=4564564
    soucet=0
    for i in range(pocet):
        a=random.randint(-100,100)
        hodnota= hodnota + str(a) + "; "
        hodnotaodzadu= str(a) + "; " + hodnotaodzadu
        soucet= soucet + a
        if a < min:
            min= a
        if a > max:
            max= a
    print("Hodnoty od zadu: " + str(hodnotaodzadu[0:len(hodnotaodzadu)-2])+"\nHodnoty: " + str(hodnota[0:len(hodnota)-2]) + "\nPrůměr: " + str(soucet/pocet) + "\nMax. hodnota: " + str(max) + "\nMin. Hodnota: " + str(min))
        
#nahodnacisla()

def znaky():
    tisk=""
    
    pocet=int(input("Kolik znaků chceš vypsat?: "))
    for y in range(1, pocet+1):
        for i in range(pocet+1-y):
            tisk= tisk + "*" 

        print(tisk)
        tisk=""
        
    for y in range(1, pocet+1):
        for i in range(y):
            tisk= tisk + "*" 

        print(tisk)
        tisk=""
znaky()
        
    




















    
