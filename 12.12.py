#zadám text, který bude mít minimálně 5 znaků
#když ne napíše chybu, když bude mít 5 znaků program se ukončí

def opakovani1():

        while(True):
                text=input("Zadej text, minimálně 5 znaků!!")
                if len(text)>=5:break
                else: print("Text je krátký")

#opakovani1()


def seznam():
        den=["pondělí","úterý","středa","čtvrtek","pátek"]
        trzby = []
        soucet = 0
        for i in range(5):
                pocet=float(input("tržba " + (den[i]) + ": "))
                trzby.append (soucet)
                soucet = soucet + pocet
        print(trzby)
        print("součet tržeb: ",soucet)

seznam()                
        
