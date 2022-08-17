##Zadejte text, program ho upraví tak ze se budou stridat
#velke a male pismena
#napr. vstup "ahoj", vystup "AhOj"

def opaktext():
    text = input("Zadej text: ")
    velke = True
    text2=""
    for i in text:
        if velke == True:
            i= i.upper()
            velke == False
        else:
            i= i.lower()
            velke == True

        text2= text2 + i
    print(text2)
#opaktext()



#Nactete n textu do listu
#pokud zacina cislem pak oznamte ze je chybny a neukladejte
#pred vlozenim do listu upravte text : prvni velke, ostatni male
##volba 1.výpis, 2.odebrani posledniho trojku, 3.konec
def opaktext2():
    n= 3
    textS=[]
    for i in range(3):
        text= input("Zadej text: ")
        if text[0] in "0123456789":
            print("chyba!")
        else:      
            textS.append(text[0].upper()+ text[1:].lower())#ten zbytek je [1:]
       
        volba=""
        while (volba!="3."):
            
            volba=input("Zadej svou volbu 1.výpis, 2.odebrani posledniho trojku, 3.konec: ")
            if volba=="1.":
                print(i)
            elif volba=="2.":
                del(textS[-1]) #poslední prvek [-1]
            elif volba!="3.":
                print("napsal si to špatně! ")
            else:
                break        
       
opaktext2()


