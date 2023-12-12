#navod
print(" Vzor: [x] [znamenko] [y]")
print(" Můžete zadat operátor: +, -, *, /, moc a odm")

#vstup
x = input("Zadejte proměnou x: ")
y = input("Zadejte proměnou y: ")

#pretypovani
x = float(x)
y = float(y)

#vstup 2
znamenko = input("Zadejte operátor:")

#podminky
if znamenko == "+":
    vysledek = x+y
    print(vysledek)
elif znamenko == "-":
    vysledek = x-y
    print (vysledek)
elif znamenko == "*":
    vysledek = x*y
    print(vysledek)
elif znamenko == "/":
    if y == 0:
        print("Nelze dělit nulou")
    else:
        vysledek = x/y
        print(vysledek)
elif znamenko == "moc":
    vysledek = x**y
    print(vysledek)
elif znamenko == "odm":
    vysledek = x**(1/y)
    print(vysledek)
