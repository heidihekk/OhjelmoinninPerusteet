from datetime import datetime

"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin. Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19.95 €
Kokonaishinta: 39.9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""

def main():
    # Määritellään tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"

    # Avataan tiedosto ja luetaan sisältö
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()

    # Tuloste
    varausnumero = int(varaus.split('|')[0]) # split('|')- metodi pilkkoo rivin ja tuottaa listatyyppisen muuttujan
    print("Varausnumero:", varausnumero)

    varaaja = varaus.split('|')[1]
    print("Varaaja:", varaaja)

    paivamaara = datetime.strptime(varaus.split('|')[2], "%Y-%m-%d").date()
    print("Päivämäärä:", paivamaara.strftime("%d.%m.%Y")) # metodi .strftime("%d.%m.%Y") muotoilee ajan muotoon pp.kk.vvvv
    
    aloitusaika = datetime.strptime(varaus.split('|')[3], "%H:%M").time()
    print("Aloitusaika:", aloitusaika.strftime("%H.%M")) # metodi .strftime("%H.%M") muotoilee ajan muotoon hh.mm

    tuntimaara = int(varaus.split('|')[4])
    print("Tuntimäärä:", tuntimaara)

    tuntihinta = float(varaus.split('|')[5])
    print(f"Tuntihinta: {tuntihinta:.2f}".replace(".", ","), "€") #.replace-metodilla voi korvata pisteen pilkulla, huom ei toimi int/float, siksi f-lausemuotoilu.

    kokonaishinta = tuntimaara * tuntihinta
    print(f"Kokonaishinta: {kokonaishinta:.2f}".replace(".", ","), "€")
    
    maksettu = varaus.split('|')[6].strip() == "True" #.strip() poistaa merkkijonon alusta ja lopusta välilyönnit ja rivinvaihdot.
    print(f"Maksettu: {'Kyllä' if maksettu else 'Ei'}") 
    
    # Edellisen tulostuslauseen voi kirjoittaa myös:
    # if maksettu:
    #     onko_maksettu = "Kyllä"
    # else:
    #     onko_maksettu = "Ei" 
    # print("Maksettu:", onko_maksettu)
    
    kohde = varaus.split('|')[7]
    print("Kohde:", kohde)
    
    puhelin = varaus.split('|')[8]
    print("Puhelin:", puhelin)

    sahkoposti = varaus.split('|')[9]
    print("Sähköposti:", sahkoposti)

if __name__ == "__main__":
    main()