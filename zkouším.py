def kalkulacka():
    a= float(input("a= "))
    b= float(input("b= "))
    volba= input("vyber: +, -, *, /.. ")
    if volba=="+":
        print(a+b)
    elif volba=="-":
        print(a-b)
    elif volba=="*":
        print(a*b)
    elif volba=="/":
        if b!=0:
            print(a/b)
        else:
            print("Nulou nelze dělit")
    else:
        print("Vyber si z uvedených možností!!")

#kalkulacka()

def inicialy():
    jmeno=input("Zadej jméno: ")
    prijmeni=input("Zadej příjmení: ")
    inicialy= jmeno[0] + "." + prijmeni[0] + "."
    if len(jmeno)<=2 or len(prijmeni)<=2:
        print("jméno nebo příjmení na dvě a méně písmena neexistuje")
    else:
        print(inicialy)
        
#inicialy()

def zkousim():        
    text= input("Zadej text: ")
    print(text[len(text)-1])
#zkousim()

def PrevodMaleaVelke():
    text=input("Zadej text: ")
    print(text[0].upper() + text[1:].lower())
PrevodMaleaVelke()

