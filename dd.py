def mesice():
        mesice=["led","únor","břez","dub","květ","červ","čvrnc","srp","září","říj","list"]
        while True: 
                cislo= int(input("Zadej číslo měsíce 1-12: "))
                if cislo >=10 and cislo <=12:
                        print(mesice[cislo - 1])
                        volba =  input("a pokračovat")
                        if volba != "a": break

mesice()
