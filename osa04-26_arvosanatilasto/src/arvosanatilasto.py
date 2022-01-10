# Kirjoita ratkaisu tähän

#koepisteet 0-20
#harjoituspisteet 10% = 1p  20% = 2p 30 % = 3p jne.
koepisteet = []
harjoitukset = []
hylatyt = []
hyvaksytyt = []
kokonais = []

hp = 0 #harjoituspisteet

while True:

    syote = input("Koepisteet ja harjoitusten määrä:")

    if syote == "":
        break

    k,h = syote.split(" ")

    hp = int(h) // 10

    if int(k) < 10:
        hylatyt.append(int(k))
    else:
        koepisteet.append(int(k))
        harjoitukset.append(hp)
        hyvaksytyt.append(int(k) + hp)

    kokonais.append(int(k) + hp)
        

#print(koepisteet)
#print(harjoitukset)
#print(hylatyt)
#print(hyvaksytyt)
#print(kokonais)
#keskiarbo

ka = (sum(kokonais)/(len(kokonais)))
hyv = 0
hyl = 0

for alkio in koepisteet:
    if alkio < 10:
        hyl +=1
    else:
        hyv +=1 



vitoset = 0
neloset = 0
kolmoset = 0
kakkoset = 0
ykkoset = 0
nollat = 0

for alkio in hyvaksytyt:
    if alkio < 15:
        hylatyt.append(alkio)
    if alkio >= 15 and alkio <= 17:
        ykkoset += 1
    if alkio > 17 and alkio <= 20:
        kakkoset += 1
    if alkio > 20 and  alkio <=23:
        kolmoset +=1
    if alkio > 23 and alkio <=27:
        neloset +=1
    if alkio > 27 and alkio <=30:
        vitoset +=1    

hyvpros = (1- (len(hylatyt)/(len(kokonais))))*100

if hyvpros == 1.0:
    hyvpros = "100.0"

vit = vitoset*"*"
nel = neloset*"*"
kol = kolmoset*"*"
kaks = kakkoset*"*"
yks = ykkoset*"*"
nol = len(hylatyt)*"*"

print(f"Tilasto:")
print(f"Pisteiden keskiarvo: {ka}")
print(f"Hyväksymisprosentti: {hyvpros:.1f}")
print(f"Arvosanajakauma:")
print(f"5: {vit}")
print(f"4: {nel}")
print(f"3: {kol}")
print(f"2: {kaks}")
print(f"1: {yks}")
print(f"0: {nol}")

