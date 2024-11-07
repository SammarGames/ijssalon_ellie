from algemene_functies import mijn_functie_2

def aanbieding_1(smaak="aarbei", prijs=4, korting=0.1):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f"Vandaag in de aanbieding: Emmertje ijs(1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro"
    return uitvoer
    

print(aanbieding_1())

def inkomsten_totaal(btw=0.09):
    totaal = 100
    bedrag = totaal * btw
    uitvoer = f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden"
    return uitvoer

print(inkomsten_totaal())

def laag_en_hoog(mijn_lijst=[220, 430, 125, 160, 205, 90, 345]): 
    laagste = min(mijn_lijst) 
    hoogste = max(mijn_lijst) 
    return [laagste, hoogste] 

print(laag_en_hoog())

def gemiddelde(mijn_lijst=[220, 430, 125, 160, 205, 90, 345]):
    gemiddelde = (mijn_lijst)
    totaal = sum(mijn_lijst)       
    aantal = len(mijn_lijst) 
    bedrag = totaal / aantal       
    uitvoer = f"De gemiddelde inkomsten deze week zijn {bedrag} euro."
    return uitvoer

print(gemiddelde())

def meervoudig(invoer_lijst=[10,5,3,2,1,2,9]):
    hoogste_en_laagste = laag_en_hoog(invoer_lijst)
    return hoogste_en_laagste

print(meervoudig())

def combinatie(invoer_lijst_2=meervoudig()):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer
print(combinatie())
