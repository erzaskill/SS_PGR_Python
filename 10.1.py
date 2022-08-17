#program zistí pošet mezer v zadaném textu

def pocetMezer():
        p=0
        text= input("Zadej text")
        for i in text:
                if i ==" " : p = p + 1
        print("počet mezer", p)

#pocetMezer()

##program nahradí mezery v textu "_"

def mezery():
        p=0
        text2 = ""
        text = input("Zadej text")
        for i in text:
                if i ==" " : text2 = text2 +"_"
                else: text2 = text2 + i
        print("počet mezer", text2)

mezery()

#Načtěte do seznamu n jmen. Zjistěte aby každé jméno
#začínal velkým písmenem, ostatní byly malým.
##seznam setřiťe a následně vypište a to za sebou, oddělené mezerou.

def seznam():
        jmena=[]
        pocet=int(input("Zadej počet jmen: "))
        vypis=""
        for i in range(pocet):
                jmeno=input("Zadej jméno: ")
                jmeno= jmeno + " "
                jmena.append(jmeno[0].upper() + jmeno[1:].lower())
                jmena.sort()
                
        print(jmena)
#seznam()
                
                
