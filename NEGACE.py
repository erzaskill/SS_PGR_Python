def absHodnota():
    a= float(input("Zadej cislo: "))
    if a<0:
        print(a*-1)
    else:
        print("absolutni hodnota: ",a)

#absHodnota()

def Zaokrouhleni():
    a=float(input("Zadej cislo: "))
    mist= int(input("Desetin. míst: "))
    print(round(a,mist))

Zaokrouhleni()

def ZaokrouhleniSVracenim():
    a=float(input("Zadej cislo: "))
    mist=int(input("Desetin. míst: "))
    return(round(a,mist))
print(ZaokrouhleniSVracenim())


def IfaLenDohromady():
    text= input("Zadej Text: ")
    print(text[0])
    if len(text)>20:
        print("Více než 20 znaků")
    elif len(text)==1:
        print("Jeden znak!")
    elif text[0]== " ":
        print("Text začíná mezerou!!")
    else:
        print("Text je v pořádku")

#IfaLenDohromady()

def ZaokrouhleniAnoNe():
    a= float(input("Zadej číslo: "))
    mist= input("Chceš zaokrouhlit na celé číslo? ")
    if (mist.upper())== "ANO": #.upper() ošetří to aby jsme to nemuseli psát
                                #velkými písmeny
        print(round(a,0))
    elif (mist.upper())== "NE": #tohle je zbytečné, protože elif znamená tady
                                #to samé co else
        print(a)
    else:
        print(a)
#ZaokrouhleniAnoNe()

def PrevodVelkeMale():
    text= input("Zadej text: ")
    Vyber= input(" VELKÉ nebo MALÉ, STEJNÉ: ")
    if Vyber == "VELKÉ":
        print(text.upper())
    elif Vyber == "MALÉ":
        print(text.lower())
    else:
        print(text)
#PrevodVelkeMale()

def prevodMaleVelke():
    text= input("Zadej text: ")
    print(text[0].upper() + text[1:].lower())
prevodMaleVelke()
