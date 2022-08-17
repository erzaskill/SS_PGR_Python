#Zadejte text, program ho upravi tak ze se budou stridat

#velke a male pismena
#napr. vstup ahoj, vystup AhOj

def text1():
        text = input("Zadej text: ")
        text2 = ""
        velke = True
        for y in text:
                if velke == True:
                        y = y.upper()
                        velke = False

                else:
                        y = y.lower
                        velke == True
                        text2 = text2 + y
        print(text2)
                        
                
#text1()


##Nactete n textu do listu
## Pokud zacina cislem pak oznamte ze je spatne a neukladejte
##/red vlozenim do listu upravte text : prvni velke, ostatni male
##volba 1. výpis, 2. odebrání posledního prvku, 3. konec
def text():
        n = 4
        textS =[]
        for i in range(n):
                text = input("Zadej text: ")
                if text[0] in "0123456789":print ("chyba")
                else: textS.append (text[0].upper() + text[1:].lower())
        while(True):
                volba= input("1. výpis, 2. odstranění posledního prvku, 3. konec")
                if volba == "1":
                        print(i)
                elif volba =="2":
                        del(textS[-1])
                elif volba == "3":
                        break
                else:
                        print("chyba")
        print(textS)


text()
                
