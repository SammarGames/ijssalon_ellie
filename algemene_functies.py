def mijn_functie_1(a=2,b=4,c=10,d=12):
    return a * a, b * b, c * c, d * d
    

print(mijn_functie_1())

def mijn_functie_2(a,b):
    uitvoer_lijst = []
    uitvoer_lijst.append(a+b)
    uitvoer_lijst.append(a-b)
    uitvoer_lijst.append(a*b)
    uitvoer_lijst.append(a/b)
    return uitvoer_lijst
totaal1 = mijn_functie_2(12,3)
totaal2 = mijn_functie_2(12,2)
totaal3 = mijn_functie_2(10,5)
totaal4 = mijn_functie_2(100,20)

print(totaal1)
print(totaal2)
print(totaal3)
print(totaal4)