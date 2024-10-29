tekst="header"
lengte = len(tekst) + 4
print()
print(lengte * "*")
print(f"* {tekst} *")
print(lengte * "*")
print()

prijzen = {"aardbei" : 3, "vanille" : 4, "chocolade" : 5}
aanbieding = prijzen["aardbei"] * 0.8
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € {aanbieding}"
