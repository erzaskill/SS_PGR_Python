#A
#Vytvořte program ktery bude načítat čísla. Načítání bude ukončeno po zadání záporného čísla
#Se zapornou hodnoutou se nebude pracovat
#Program následně zobrazí možnost: 1. Výpis čísel, 2. Průměrná hodnota, 3.Minimální hodnota
#Po provedení volby se program ukončí


def Test():
    a=1
    soucet=0
    pocet=0
    volba=""
    hodnota=""
    min=6546546
    a=float(input("Zadej číslo: "))
    while a>-1:
        hodnota= hodnota + str(a) + "; "
        soucet= soucet + a
        pocet= pocet + 1
        if a<min:
            min = a
        a=float(input("Zadej číslo: "))
    volba=input("Vyber si mezi: 1.=Výpis čísel, 2.=Prům. hodnota, 3.=Min. hodnota: ")
    if volba == "1.":
        print("Výpis hodnot:",hodnota)
    elif volba == "2.":
        print("Průměrná hodnota: ",soucet/pocet)
    elif volba == "3.":
        print("Minimální hodnota: ", min)

#Test()

#vytvořte program
#bude nacitat cisla, dokud se nezada 0
#potom vypise nejvyssi hodnotu a průměr

def WhileOpk():
    a=1
    soucet=0
    pocet=0
    max=-6546546
    a=float(input("Zadej číslo: "))
    while a!=0:
        if a>max:
            max=a
        soucet= soucet + a
        pocet= pocet + 1
        a=float(input("Zadej číslo: "))
    print("Max. hodnota" + str(max) + "\nPrůměr: " + str(soucet/pocet))
#WhileOpk()


#program načte 2 hodnoty typu string
#následně zobrazí 1.nejdelší text, 2.celkový počet znaků, 3.konec
#dokud se nezadá 3, pořád se vrací na volbu

def WhileLenOpk():
    a=input("Zadej text: ")
    b=input("Zadej druhý text: ")
    volba= ""
    while volba!="3.":
        volba=input("Vyber si mezi: 1. Zobrazí nejdelší text; 2.Celkový počet znaků; 3.konec____: ")
        if volba == "1.":
            if len(a)>len(b):
                print("Nejdelší text je: ",a)
            elif len(a)==len(b):
                print("Texty mají stejný počet znaků: " + "\n" + str(a) + "\n" + str(b))
            else:
                print("Nejdelší text je: ",b)
        elif volba== "2.":
            print("Celkový počet znaků je: ",len(a)+len(b))
        elif volba !="3.":
            print("Špatně si zadal volbu")
        else:
            print("Konec")

#WhileLenOpk()

#NAUČ SE WHILE TRUE
        
            
            


