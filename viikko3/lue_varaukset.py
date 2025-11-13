"""
Ohjelma joka lukee tiedostossa olevat varaustiedot
ja tulostaa ne konsoliin käyttäen funkitoita.
Alla esimerkkitulostus:

Varausnumero: 123
Varaaja: Anna Virtanen
Päivämäärä: 31.10.2025
Aloitusaika: 10.00
Tuntimäärä: 2
Tuntihinta: 19,95 €
Kokonaishinta: 39,9 €
Maksettu: Kyllä
Kohde: Kokoustila A
Puhelin: 0401234567
Sähköposti: anna.virtanen@example.com

"""
from datetime import datetime, date, time

def hae_varausnumero(varaus: list[str]) -> int:
    varausnumero = int(varaus[0])
    print(f"Varausnumero: {varausnumero}")
    return varausnumero
    
def hae_varaaja(varaus: list[str]) -> str:
    nimi = varaus[1]
    print(f"Varaaja: {nimi}")
    return nimi

def hae_paiva(varaus: list[str]) -> date:
    pvm = datetime.strptime(varaus[2], '%Y-%m-%d').date()
    print(f"Päivämäärä: {pvm.strftime('%d.%m.%Y')}")
    return pvm

def hae_aloitusaika(varaus: list[str]) -> time:
    aika = datetime.strptime(varaus[3], '%H:%M').time()
    print(f"Aloitusaika: {aika.strftime('%H.%M')}")
    return aika

def hae_tuntimaara(varaus: list[str]) -> int:
    tuntimaara = int(varaus[4])
    print(f"Tuntimäärä: {tuntimaara}")
    return tuntimaara

def hae_tuntihinta(varaus: list[str]) -> float:
    tuntihinta = float(varaus[5])
    print(f"Tuntihinta: {tuntihinta:.2f}".replace(".", ","), "€")
    return tuntihinta

def laske_kokonaishinta(varaus: list[str]) -> float:
    kokonaishinta = int(varaus[4]) * float(varaus[5])
    print(f"Kokonaishinta: {kokonaishinta:.2f}".replace(".", ","), "€")
    return kokonaishinta
    
def hae_maksettu(varaus: list[str]) -> bool:
    maksettu = varaus[6].strip() == "True"
    print(f"Maksettu: {'Kyllä' if maksettu else 'Ei'}")
    return maksettu

def hae_kohde(varaus: list[str]) -> str:
    kohde = varaus[7]
    print(f"Kohde: {kohde}")
    return kohde

def hae_puhelin(varaus: list[str]) -> str:
    puhelin = varaus[8]
    print(f"Puhelin: {puhelin}")
    return puhelin

def hae_sahkoposti(varaus: list[str]) -> str:
    email = varaus[9]
    print(f"Sähköposti: {email}")
    return email

def tulosta_varaus(varaus: list[str]) -> None:
    hae_varaaja(varaus)
    hae_paiva(varaus)
    hae_aloitusaika(varaus)
    hae_tuntimaara(varaus)
    hae_tuntihinta(varaus)
    laske_kokonaishinta(varaus)
    hae_maksettu(varaus)
    hae_kohde(varaus)
    hae_puhelin(varaus)
    hae_sahkoposti(varaus)
    


def main():
    # Maaritellaan tiedoston nimi suoraan koodissa
    varaukset = "varaukset.txt"

    # Avataan tiedosto, luetaan ja splitataan sisalto
    with open(varaukset, "r", encoding="utf-8") as f:
        varaus = f.read().strip()
        varaus = varaus.split('|')

    # hae_varausnumero(varaus)
    # hae_varaaja(varaus)
    # hae_paiva(varaus)
    # hae_aloitusaika(varaus)
    # hae_tuntimaara(varaus)
    # hae_tuntihinta(varaus)
    # laske_kokonaishinta(varaus)
    # hae_maksettu(varaus)
    # hae_kohde(varaus)
    # hae_puhelin(varaus)
    # hae_sahkoposti(varaus)
    tulosta_varaus(varaus)

if __name__ == "__main__":
    main()