# Copyright (c) 2025 Heidi Hekkala
# License: MIT

from datetime import datetime, date

def muunna_tietotyyppi(rivi: list) -> list:
    """Ottaa parametrina CSV-rivin merkkijonoja (listana), muuntaa merkkijonot oikeisiin tietotyyppeihin 
    (aikaleiman datetime-olioksi ja muut arvot liukuluvuiksi), korvaa desimaalipilkut pisteillä ennen muunnosta.
    Palauttaa muunnetun rivin listana."""

    muutettu_rivi = []
    muutettu_rivi.append(datetime.fromisoformat(rivi[0]))
    muutettu_rivi.append(float(rivi[1].replace(",", ".")))
    muutettu_rivi.append(float(rivi[2].replace(",", ".")))
    muutettu_rivi.append(float(rivi[3].replace(",", ".")))
    return muutettu_rivi

def lue_data(tiedoston_nimi: str) -> list:
    """Lukee CSV-tiedoston, kutsuu funktiota muunna_tietotyyppi ja palauttaa listan oikeissa tietotyypeissä.."""
    rivit = []
    with open(tiedoston_nimi, "r", encoding="utf-8") as f:
        next(f)
        for rivi in f:
            rivi = rivi.strip()
            rivin_tiedot = rivi.split(";")
            rivit.append(muunna_tietotyyppi(rivin_tiedot))
    return rivit

def suomalainen_pvm(aika: datetime) -> str:
    """Muuttaa datetime suomalaiseen muotoon pv.kk.vuosi"""
    pvm_str = f"{aika.day}.{aika.month}.{aika.year}"
    return pvm_str

def nayta_paavalikko() -> str:
    """Tulostaa päävalikon, kysyy käyttäjän syötteen,
    tarkistaa onko syöte kelvollinen ja palauttaa käyttäjän valinnan merkkijonona. 
    Jos syöte ei ole 1, 2, 3 tai 4, tulostaa virheilmoituksen ja pyytää syötettä uudelleen."""
    
    while True:
        valinta = input(
            "-----------------------------------------------------\n"
            "Valitse raporttityyppi:\n"
            "1) Päiväkohtainen yhteenveto aikaväliltä\n"
            "2) Kuukausikohtainen yhteenveto yhdelle kuukaudelle\n"
            "3) Vuoden 2025 kokonaisyhteenveto\n"
            "4) Lopeta ohjelma\n"
            "-----------------------------------------------------\n"
            "Syötä valintasi (1-4): ").strip()

        if valinta in ["1", "2", "3", "4"]:
            return valinta

        print("Virheellinen valinta. Valinnan oltava 1, 2, 3 tai 4.")
        input("Paina Enter jatkaaksesi")

def alavalikko() -> str:
    """Tulostaa alavalikon, kysyy käyttäjän syötteen,
    tarkistaa onko syöte kelvollinen ja palauttaa käyttäjän valinnan merkkijonona. 
    Jos syöte ei ole 1, 2 tai 3, tulostaa virheilmoituksen ja pyytää syötettä uudelleen."""
    
    while True:
        valinta = input(
            "-----------------------------------------------------\n"
            "Mitä haluat tehdä seuraavaksi?\n"
            "1) Kirjoita raportti tiedostoon raportti.txt\n"
            "2) Luo uusi raportti\n"
            "3) Lopeta\n"
            "-----------------------------------------------------\n"
            "Syötä valintasi (1-3): ").strip()

        if valinta in ["1", "2", "3"]:
            return valinta

        print("Virheellinen valinta. Valinnan oltava 1, 2 tai 3.")
        input("Paina Enter jatkaaksesi")

def aikavalin_kokonaisarvot(data: list, alkuaika: date, loppuaika: date) -> list:
    """Ottaa parametrinä tiedoston datan (list) ja alkamis- ja päättymisajat (datetime).
    Laskee ja palauttaa listana annetun aikavälin kokonaiskulutuksen kWh, kokonaistuotannon kWh ja keskilämpötilan."""
    kokonaiskulutus = 0.0
    kokonaistuotanto = 0.0
    lampotilojen_summa = 0.0
    laskuri = 0

    for rivi in data:
        if alkuaika <= rivi[0].date() <= loppuaika:
            kokonaiskulutus += rivi[1]
            kokonaistuotanto += rivi[2]
            lampotilojen_summa += rivi[3]
            laskuri += 1
    
    keskilampotila = lampotilojen_summa / laskuri

    return [kokonaiskulutus, kokonaistuotanto, keskilampotila]

def kuukauden_kokonaisarvot(data: list, kuukausi: int) -> list:
    """Ottaa parametrinä tiedoston datan (list) ja kuukauden numeron (int).
    Laskee ja palauttaa listana annetun kuukauden kokonaiskulutuksen kWh, kokonaistuotannon kWh ja keskilämpötilan."""
    kokonaiskulutus = 0.0
    kokonaistuotanto = 0.0
    lampotilojen_summa = 0.0
    laskuri = 0

    for rivi in data:
        if rivi[0].month == kuukausi:
            kokonaiskulutus += rivi[1]
            kokonaistuotanto += rivi[2]
            lampotilojen_summa += rivi[3]
            laskuri += 1
    
    keskilampotila = lampotilojen_summa / laskuri

    return [kokonaiskulutus, kokonaistuotanto, keskilampotila]

def vuoden_kokonaisarvot(data: list) -> list:
    """Ottaa parametrinä tiedoston datan (list).
    Laskee ja palauttaa listana koko vuoden kokonaiskulutuksen kWh, kokonaistuotannon kWh ja keskilämpötilan."""
    kokonaiskulutus = 0.0
    kokonaistuotanto = 0.0
    lampotilojen_summa = 0.0
    laskuri = 0

    for rivi in data:
        kokonaiskulutus += rivi[1]
        kokonaistuotanto += rivi[2]
        lampotilojen_summa += rivi[3]
        laskuri += 1
    
    keskilampotila = lampotilojen_summa / laskuri

    return [kokonaiskulutus, kokonaistuotanto, keskilampotila]

def luo_paivaraportti(data: list) -> str:
    """Ottaa parametrina tiedoston datan (list) ja kysyy käyttäjältä alku- ja loppupäivän.
    Tarkistaa päivämäärien oikeellisuuden ja jos syöte virheellinen, pyytää syötettä uudelleen.
    Kutsuu funktiota aikavalin_kokonaisarvot ja muodostaa raoportin valitulle aikavälille.
    Palauttaa raportin merkkijonona."""

    while True:
        alkupvm = input("Anna alkupäivä (pv.kk.vvvv): ").strip()
        loppupvm = input("Anna loppupäivä (pv.kk.vvvv): ").strip()
        
        # Tarkistetaan päivämäärien oikeellisuus (alkuaika ennen loppuaikaa, vuosi on 2025 ja pvm annettu oikeassa muodossa)
        try:
            alkuaika = datetime.strptime(alkupvm, "%d.%m.%Y").date()
            loppuaika = datetime.strptime(loppupvm, "%d.%m.%Y").date()

            if alkuaika > loppuaika:
                print("Alkupäivän on oltava ennen loppupäivää.")
                print("-----------------------------------------------------")
                continue
            
            if alkuaika.year != 2025 or loppuaika.year != 2025:
                print("Päivämäärien on oltava vuodelta 2025.")
                print("-----------------------------------------------------")
                continue

            break
        
        except ValueError:
            print("Virhe päivämäärän syötössä. Anna päivät muodossa pv.kk.vvvv. ")
            print("-----------------------------------------------------")
            continue

    aikavalin_kokonaiskulutus = aikavalin_kokonaisarvot(data, alkuaika, loppuaika)[0]
    aikavalin_kokonaistuotanto = aikavalin_kokonaisarvot(data, alkuaika, loppuaika)[1]
    aikavalin_keskilampotila = aikavalin_kokonaisarvot(data, alkuaika, loppuaika)[2]

    return (f"\nPäiväraportti {alkupvm} - {loppupvm}:\n" +
            f"Kokonaiskulutus {aikavalin_kokonaiskulutus:.2f} kWh\n".replace(".", ",") +
            f"Kokonaistuotanto {aikavalin_kokonaistuotanto:.2f} kWh\n".replace(".", ",") +
            f"Keskilämpötila {aikavalin_keskilampotila:.2f} °C\n".replace(".", ","))

def luo_kuukausiraportti(data: list) -> str:
    """Ottaa parametrina tiedoston datan (list) ja kysyy käyttäjältä kuukauden numeron.
    Tarkistaa kuukauden numeron oikeellisuuden ja jos syöte virheellinen, pyytää syötettä uudelleen.
    Kutsuu funktiota kuukauden_kokonaisarvot ja muodostaa raportin valitulle kuukaudelle.
    Palauttaa raportin merkkijonona."""
    
    while True:
        try:
            kuukausi = int(input("Anna kuukauden numero (1-12): "))
            if 1 <= kuukausi <= 12:
                break
            else:
                print("Virheellinen syöte. Anna kuukauden numero väliltä 1-12.")
        except ValueError:
            print("Virheellinen syöte. Anna kuukauden numero väliltä 1-12.")
    
    kuukaudet = ["tammikuulta", "helmikuulta", "maaliskuulta", "huhtikuulta", "toukokuulta", "kesäkuulta",
                 "heinäkuulta", "elokuulta", "syyskuulta", "lokakuulta", "marraskuulta", "joulukuulta"]

    kuukauden_kokonaiskulutus = kuukauden_kokonaisarvot(data, kuukausi)[0]
    kuukauden_kokonaistuotanto = kuukauden_kokonaisarvot(data, kuukausi)[1]
    kuukauden_keskilampotila = kuukauden_kokonaisarvot(data, kuukausi)[2]
    
    return (f"\nKuukausiraportti {kuukaudet[kuukausi - 1]}:\n" +
              f"Kokonaiskulutus {kuukauden_kokonaiskulutus:.2f} kWh\n".replace(".", ",") +
              f"Kokonaistuotanto {kuukauden_kokonaistuotanto:.2f} kWh\n".replace(".", ",") +
              f"Keskilämpötila {kuukauden_keskilampotila:.2f} °C\n".replace(".", ","))

def luo_vuosiraportti(data: list) -> str:
    """Ottaa parametrina tiedoston datan (list), kutsuu funktiota vuoden_kokonaisarvot 
    ja muodostaa koko vuoden raportin. Palauttaa raportin merkkijonona."""

    vuoden_kokonaiskulutus = vuoden_kokonaisarvot(data)[0]
    vuoden_kokonaistuotanto = vuoden_kokonaisarvot(data)[1]
    vuoden_keskilampotila = vuoden_kokonaisarvot(data)[2]
    
    return ("\nVuoden 2025 raportti:\n" +
              f"Kokonaiskulutus {vuoden_kokonaiskulutus:.2f} kWh\n".replace(".", ",") +
              f"Kokonaistuotanto {vuoden_kokonaistuotanto:.2f} kWh\n".replace(".", ",") +
              f"Keskilämpötila {vuoden_keskilampotila:.2f} °C\n".replace(".", ","))



def kirjoita_raportti_tiedostoon(raportti: str) -> None:
    """Kirjoittaa raportin tiedostoon raportti.txt."""

    with open("raportti.txt", "w", encoding="utf-8") as f:
        f.write(raportti)


def main() -> None:
    """Ohjelman pääfunktio: lukee datan, näyttää valikot ja ohjaa raporttien luomista."""
    
    data = lue_data("2025.csv")

    while True:
        valinta1 = nayta_paavalikko()
        if valinta1 == "1":
            aikavaliraportti = luo_paivaraportti(data)
            print(aikavaliraportti) 
            valinta2 = alavalikko()
            if valinta2 == "1":
                kirjoita_raportti_tiedostoon(aikavaliraportti)
                print("Raportti kirjoitettu tiedostoon raportti.txt")
            elif valinta2 == "2":
                continue
            elif valinta2 == "3":
                print("Ohjelma lopetettu.\n")
                break

        elif valinta1 == "2":
            kuukausiraportti = luo_kuukausiraportti(data)
            print(kuukausiraportti)
            valinta2 = alavalikko()
            if valinta2 == "1":
                kirjoita_raportti_tiedostoon(kuukausiraportti)
                print("Raportti kirjoitettu tiedostoon raportti.txt")
            elif valinta2 == "2":
                continue
            elif valinta2 == "3":
                print("Ohjelma lopetettu.\n")
                break

        elif valinta1 == "3":
            vuosiraportti = luo_vuosiraportti(data)
            print(vuosiraportti)
            valinta2 = alavalikko()
            if valinta2 == "1":
                kirjoita_raportti_tiedostoon(vuosiraportti)
                print("Raportti kirjoitettu tiedostoon raportti.txt")
            elif valinta2 == "2":
                continue
            elif valinta2 == "3":
                print("Ohjelma lopetettu.\n")
                break

        elif valinta1 == "4":
            print("Ohjelma lopetettu.\n")
            break
    
if __name__ == "__main__":
    main()