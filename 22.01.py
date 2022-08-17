###program bude nacitat texty do seznamu, pokud zadate 1 znak
###nacitani se ukonci, znak se neuloží

#potom volba
#1.výpis pod sebe (první velké ostatní malé)
#2.výpis pod sebe, místo číslic bude otazník
#3.nejdelší text/y
#4.konec





def texty():
    text=""
    seznam=[]
    while True:
        text=input("Zadej text: ")
        if len(text)==1:
            break
        elif len(text)!=1:
            seznam.append(text)
    volba=""
    otaznik="?"
    cislice="1234568790"
    while True:

        volba=input("Zadej svou volbu: 1=výpis pod sebe (první velké ostatní malé, 2=výpis pod sebe, místo číslic bude otazník, 3=nejdelší text/y, 4=konec")
        if volba=="1":
            for text in seznam:
                print(text[0].upper() + text[1:].lower())
                
        elif volba=="2":
            for text in seznam:
                text2=""
                for i in text:
                    
                    if i in cislice:
                        text2= text2 + "?"
                    else:
                        text2= text2 + i
                print(text2)
                    
        elif volba=="3":
            maxT=-35453423143
            for text in seznam:
                if len(text)>maxT:
                    maxT=len(text)
            tisk=""        
            for text in seznam:
                if len(text)==maxT:
                    tisk= tisk + text + " "
            print("nejdelší text/y: ",tisk)       
                    
        elif volba!="4":
            print("Napsal si to špatně!")
        else:
            break

texty()
                            
            
            
