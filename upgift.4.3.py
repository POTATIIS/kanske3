mål = int(input('Ange ett heltal för antalet kronor som är ditt mål: ')) #tar input och gär mål variabeln ett värde
mål = mål*100 # omvandlar kronor till öre
öre = 1 #din bas lön på från första dagen
dagar = 0 # man börjar räkna dagarna från dag 0
while öre <= mål: #ser till så att programet loopar tills det når sitt mål
    dagar = dagar + 1 # ser till så att dagarna ökas
    öre = öre*2 # ser till så att lönen ökas med 2 för varje dag
print(f'Det kommer att ta {dagar} dagar tills du har tjänat ihop {mål/100:.0f} kronor! ') # sista delen i programmet som skriver ut antalet dagar det tog för att nå målet
