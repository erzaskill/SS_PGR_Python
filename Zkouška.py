def ObsahObvodCtverce():
    a=float(input("a= "))
    o= 4*a
    s= a**2
    tisk= "a= " + str(a) + "\n" + "o= " + str(o) + "\n" + "s= " + str(s)
    print(tisk)

ObsahObvodCtverce()

def PocetPismen():
    text=input("Zadej text: ")
    print("počet znaků v textu: ", len(text))
    print("Sedmý znak v textu: ", text[6])
    print("Poslední znak v textu: ", text[len(text)-1])

PocetPismen()
    
