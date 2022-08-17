vek= float(input("Zadej číslo: "))
def Plnolety():
    if vek < 18:
        print("neplnoletý ")
    else:
        print("plnoletý")

Plnolety()


def kladneZapNula():
    cislo=float(input("cislo: "))
    if cislo > 0: #musí být jednou
        print("kladne")
    elif cislo == 0: #elif může být vícekrát
        print("nula")
    else:
        print("zaporne")
kladneZapNula()


    
