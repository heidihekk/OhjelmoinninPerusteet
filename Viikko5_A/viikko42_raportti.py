# Copyright (c) 2025 Heidi Hekkala
# License: MIT

from datetime import datetime

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
    return f"{kulutus1}\t{kulutus2}\t{kulutus3}\t{tuotanto1}\t{tuotanto2}\t{tuotanto3}"

def main() -> None:
    """
    Ohjelman pääfunktio: lukee datan tiedostosta "viikko42.csv", 
    laskee yhteenvedot joka päivälle ja tulostaa raportin.
    """

    data = lue_data("viikko42.csv")

    print("\nViikon 42 sähkönkulutus ja -tuotanto (kWh, vaiheittain)\n")
    print("Päivä\t\tPvm\t\tKulutus [kWh]\t\tTuotanto [kWh]")
    print("\t\t(pv.kk.vvvv)\tv1\tv2\tv3\tv1\tv2\tv3")
    print("---------------------------------------------------------------------------")
    print(f"maanantai\t{suomalainen_pvm(datetime(2025, 10, 13))}\t{paivan_kulutus_ja_tuotanto(datetime(2025, 10, 13), data)}")
    print(f"tiistai\t\t{suomalainen_pvm(datetime(2025, 10, 14))}\t{paivan_kulutus_ja_tuotanto(datetime(2025, 10, 14), data)}")
    print(f"keskiviikko\t{suomalainen_pvm(datetime(2025, 10, 15))}\t{paivan_kulutus_ja_tuotanto(datetime(2025, 10, 15), data)}")
    print(f"torstai\t\t{suomalainen_pvm(datetime(2025, 10, 16))}\t{paivan_kulutus_ja_tuotanto(datetime(2025, 10, 16), data)}")
    print(f"perjantai\t{suomalainen_pvm(datetime(2025, 10, 17))}\t{paivan_kulutus_ja_tuotanto(datetime(2025, 10, 17), data)}")
    print(f"lauantai\t{suomalainen_pvm(datetime(2025, 10, 18))}\t{paivan_kulutus_ja_tuotanto(datetime(2025, 10, 18), data)}")
    print(f"sunnuntai\t{suomalainen_pvm(datetime(2025, 10, 19))}\t{paivan_kulutus_ja_tuotanto(datetime(2025, 10, 19), data)}")

if __name__ == "__main__":
    main()
