# Copyright (c) 2025 Heidi Hekkala
# License: MIT

from datetime import datetime, timedelta

def muunna_tietotyyppi(rivi: list) -> list:
    """Muuttaa tietorivien tietotyypit oikeiksi"""
    muutettu_rivi = []
    muutettu_rivi.append(datetime.fromisoformat(rivi[0]))
    muutettu_rivi.append(int(rivi[1]))
    muutettu_rivi.append(int(rivi[2]))
    muutettu_rivi.append(int(rivi[3]))
    muutettu_rivi.append(int(rivi[4]))
    muutettu_rivi.append(int(rivi[5]))
    muutettu_rivi.append(int(rivi[6]))
    return muutettu_rivi


def lue_data(tiedoston_nimi: str) -> list:
    """Lukee CSV-tiedoston ja palauttaa rivit sopivassa rakenteessa ja tietotyypeissä."""
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
    
def paivan_kulutus_ja_tuotanto(aika: datetime, data: list) -> str:
    """ Ottaa parametrinä ajan (datetime) ja tiedoston datan (list).
        Laskee annetun päivän yhteiskulutuksen ja -tuotannon jokaista kulutus/tuotantopistettä kohden, 
        ja muuttaa Wh -> kWh.
        Palauttaa merkkijonon, jossa kulutus- ja tuotantosummat joka pisteelle valmiiksi pyöristettynä ja muotoiltuna
    """
    kulutus1 = 0
    kulutus2 = 0
    kulutus3 = 0
    tuotanto1 = 0
    tuotanto2 = 0
    tuotanto3 = 0
    paiva = aika.date()
    for rivi in data:
        if rivi[0].date() == paiva:
            kulutus1 += rivi[1] / 1000
            kulutus2 += rivi[2] / 1000
            kulutus3 += rivi[3] / 1000
            tuotanto1 += rivi[4] / 1000
            tuotanto2 += rivi[5] / 1000
            tuotanto3 += rivi[6] / 1000
    kulutus1 = f"{kulutus1:.2f}".replace(".", ",")
    kulutus2 = f"{kulutus2:.2f}".replace(".", ",")
    kulutus3 = f"{kulutus3:.2f}".replace(".", ",")
    tuotanto1 = f"{tuotanto1:.2f}".replace(".", ",")
    tuotanto2 = f"{tuotanto2:.2f}".replace(".", ",")
    tuotanto3 = f"{tuotanto3:.2f}".replace(".", ",")
    return f"\t{kulutus1}\t{kulutus2}\t{kulutus3}\t{tuotanto1}\t{tuotanto2}\t{tuotanto3}"

def tulostuksen_muotoilu(data: list, aloitus_pvm: datetime, viikkonumero: int) -> str:
    """ Muotoilee viikon datan taulukoksi.
        Ottaa parametrina viikon datan (list), aloituspäivämäärän (datetime) ja viikkonumeron (int).
        Laskee päivämäärät aloituspäivästä eteenpäin 7 päivän ajan.
        Muotoilee päivämäärän suomalaiseen muotoon ja hakee datan funktiolla paivan_kulutus_ja_tuotanto().
        Palauttaa str-muotoisen merkkijonon, jossa viikon data taulukkomuodossa.
    """

    paivat = ["maanantai", "tiistai  ", "keskiviikko", "torstai  ", "perjantai", "lauantai", "sunnuntai"]
    
    viikko_x = f"\nViikon {viikkonumero} sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n\n"
    viikko_x += "Päivä\t\tPvm\t\t\t\tKulutus [kWh]\t\t\tTuotanto [kWh]\n"
    viikko_x += "\t\t\t(pv.kk.vvvv)\tv1\t\tv2\t\tv3\t\tv1\t\tv2\t\tv3\n"
    viikko_x += "---------------------------------------------------------------------------\n"

    for i in range(7):
        paiva = aloitus_pvm + timedelta(days=i) # timedelta lisää tiedoston ensimmäiseen päivämäärään += 1, kunnes käyty läpi koko viikko 7pv
        viikko_x += f"{paivat[i]}\t{suomalainen_pvm(paiva)}\t{paivan_kulutus_ja_tuotanto(paiva, data)}\n"
   
    viikko_x += "---------------------------------------------------------------------------\n"
    return viikko_x

def raportti_tiedostoon(viikko: str) -> None:
    """ Kirjoittaa yhden viikon raportin tiedostoon.
        Jos tiedostossa on sisältöä ennestään, lisää raportin tiedoston loppuun.
    """

    with open("yhteenveto.txt", "a", encoding="utf-8") as f:
         f.write(viikko)


def main() -> None:
    """

    """

    data_vk41 = lue_data("viikko41.csv")
    data_vk42 = lue_data("viikko42.csv")
    data_vk43 = lue_data("viikko43.csv")

    
    raportti_tiedostoon(tulostuksen_muotoilu(data_vk41, datetime(2025, 10, 6), 41))
    raportti_tiedostoon(tulostuksen_muotoilu(data_vk42, datetime(2025, 10, 13), 42))
    raportti_tiedostoon(tulostuksen_muotoilu(data_vk43, datetime(2025, 10, 20), 43))

if __name__ == "__main__":
    main()
