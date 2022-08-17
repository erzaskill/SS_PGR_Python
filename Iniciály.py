a = input("Váše jméno je?: ")
b = input("Vaše příjmení je?: ")
c = input("Váš věk je?: ")

tisk = "Vaše jméno je?: " + a + "\n" +"Váše příjmení je: " + b + "\n" +"Váš věk je:? " + c
print(tisk)

plnolety = 18 <= float(c) #do plnolety se uloží true nebo false
                # plnolety je datoveho typu boolean

print ("plnoletý: ", plnolety)


