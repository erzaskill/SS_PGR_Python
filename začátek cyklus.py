def druhamocninacyklus():
    volba="1"
    while volba=="1":
        a=float(input("Zadej číslo: "))
        print(a**2)
        volba= input("1= pokračovat: ")
    
#druhamocninacyklus()

def vypisnezapornehocislacyklus2():
    a=0
    tisk=""
    while a>=0:
        a=float(input("Zadej číslo: "))
        if a >= 0:tisk = tisk + str(a) + "\n"
    print(tisk)

        

#vypisnezapornehocislacyklus2()

def vypisNezapCisel():#od 1 do 100
    a=1
    while a<101:
        print(a)
        a=a+1
#vypisNezapCisel()
   
def vypisNezapSudehoCisla():
    a=2
    while a<101:
        print(a)
        a=a+2

#vypisNezapSudehoCisla()

def VypisCisel():#od 2 do n
    a=2
    n= int(input("do kolika: "))
    while a<=n:
        print(a)
        a= a + 2
VypisCisel()

    



