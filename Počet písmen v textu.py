def PocetPismenVTextu():
    text= input("Zadej text: ")
    print(len(text))
PocetPismenVTextu()

def PrvniAPosledniATretiPismeno():
    text1= input("Zadej další text: ")
    print("První písmeno je: ", text1[0])
    print("Poslední písmeno je: ",text1[len(text1)-1])
    print("Třetí písmeno je: ", text1[2])
PrvniAPosledniATretiPismeno()
