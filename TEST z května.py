## (A)
def prumer():
    a=float(input("a: "))
    b=float(input("b: "))
    c=float(input("c: "))
    tisk = "a: " + str(a) + ", b: " + str(b) + ", c: " + str(c) + "\n"
    tisk = tisk + "prumer: " + str((a+b+c)/3)
    print (tisk)

#prumer()



def soucetTextu():
    t1 = input("text1: ")
    t2 = input("text2: ")
    print(len(t1+t2))

#soucetTextu()

### (B)
def soucetCtverce():
    a=float(input("a: "))
    o=4*a
    s=a*a
    tisk= ("Strana a: ") + str(a) + "cm\n"
    tisk = tisk + "obvod: " + str(o) + "cm\n"
    tisk = tisk + "obsah: " + str(a**2) + "cm"
    print(tisk)
#soucetCtverce()

def Text():
    t1 = input("text1: ")
    print("počet znaků: ", len(t1))
    print("první znak: ", t1[0])
    print("poslední znak: ", t1[len(t1)-1])
    
Text()
          
