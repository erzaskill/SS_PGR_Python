def soucet(a, b) : #má dva parametry
    return round(a + b,1)
# return vrací hodnotu
#print (soucet(1,5))

def soucetcisel() : #nemá parametry a nevrací hodnotu
    a= float(input("zadej a: "))
    b= float(input("zadej b: "))

    tisk= "cislo1: " + str(a) + "\n"
    tisk= tisk + "cislo2: " + str(b) + "\n"
    tisk= tisk + "soucet: " + str(soucet(a,b)) + "\n" #volá funkci soucet
    print (tisk)


#soucetcisel() #tohle tam musí být přesně i na velké písmena.. jinak to nepujde spustit

def soucetText(t1,t2) :
    return len(t1 + t2) #vestavěnná funkce, která vrací počet znaků v řetězci
#print(soucetText("Ahoj", "co je"))


#Tohle dělá součet písmen v textu!!
def soucetZnaku() :
    a= input("zadej text1: ")
    b= input("zadej text2: ")

    tisk= "text1: " + a + "\n"
    tisk= tisk + "text2: " + b + "\n"
    tisk= tisk + "soucet: " + str(soucetText(a,b)) + "\n" #volá funkci soucet
    print (tisk)


def praceText() :
    text= input("zadej text: ")
    print ("počet znaků: ",len(text)) #Zobrazí počet znaků v textu
    print ("třetí znak je: ", text[2]) #Vrátí třetí znak 0=1 v programování
    print ("poslední znak je: ", text[len(text)-1]) #Vrátí poslední znak
##praceText()


def inicialy() :
    Jmeno= input("Zadej jméno: ")
    Prijmeni= input("Zadej příjmení: ")
    print ("Inicialy: " + Jmeno[0] + "." + Prijmeni[0] + ".")
inicialy()


