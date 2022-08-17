##Nactete text, pokud obsahuje mezeru, ktera neni na prvnim nebo
##poslednim miste. Pak na konec textu pridejte "." + prvni znak velkym.


def program():
    text=input("Zadej text: ")
    if " " in text and text[0]!=" " and text[-1]!=" ":
        text=text[0].upper() + text[1:].lower() + "."
        print(text)
    
    
    
#program()

#Nactete text. A zjisti zda text zacina velkym pismenem.

        

def program1():
    text=input("Zadej text: ")
    
    if text==text[0].lower() + text[1:] and text!=text[0].upper() + text[1:]:
        print("Text začíná malým písmenem")
    else:
        print("Text začíná velkým písmenem")

    
#program1()


#Kolik písmen je velkých.. #nemíš psát mezery
        
def program2():
    
    text=input("Zadej text: ")
    p=0
    
    for i in text:
        if i==i.upper():
            p= p+1
    print("Počet velkých písmen: ",p)
    


#program2()

#Nactete text.
#Zobrazte vsechny cislice, ktere se vyskytuji v textu

def program3():
    text=input("Zadej text: ")
    cislice="1234567890"
    cisliceS=[]
    for i in text:
        if i in cislice:
            cisliceS.append(i)
    print(cisliceS)
       

#program3()

#Nactete text.
#Nahradte vsechny cislice "?" a mezery "_".

def program4():
    text=input("Zadej text: ")
    cislice="1234567890"
    text2=""
    mezera=" "
    for i in text:
        if i in cislice:
            text2=text2 + "?"
        elif i==mezera:
            text2=text2 + "_"
        else: text2= text2 + i  
    print(text2)
program4()
            
            
   
