# Copyright (c) 2025 Heidi Hekkala
# License: MIT

# Käytän sanakirjoja varaustietojen tallentamiseen.
# Sanakirjojen käyttö tekee koodin lukemisesta huomattavasti selkeämpää,
# koska avaimen nimi kertoo suoraan, mihin kyseisessä kohdassa viitataan. 
# Varaus["varaus_vahvistettu"] on paljon nopeammin tulkittavissa kuin varaus[8],
# ja tämä helpottaa mm. virheiden löytämistä ja koodin ylläpitoa/jatkokehittämistä.


from datetime import datetime

def muunna_varaustiedot(varaus_lista: list[str]) -> dict:
    return {
        "id": int(varaus_lista[0]),
        "nimi": varaus_lista[1],
        "email": varaus_lista[2],
        "puhelin": varaus_lista[3],
        "varauksen_pvm": datetime.strptime(varaus_lista[4], "%Y-%m-%d").date(),
        "varauksen_klo": datetime.strptime(varaus_lista[5], "%H:%M").time(),
        "varauksen_kesto": int(varaus_lista[6]),
        "hinta": float(varaus_lista[7]),
        "varaus_vahvistettu": varaus_lista[8].lower() == "true",
        "varattu_tila": varaus_lista[9],
        "varaus_luotu": datetime.strptime(varaus_lista[10], "%Y-%m-%d %H:%M:%S")
    }

def hae_varaukset(varaustiedosto: str) -> list[dict]:
    varaukset = []
    with open(varaustiedosto, "r", encoding="utf-8") as f:
        for varaus in f:
            varaus = varaus.strip()
            varaustiedot = varaus.split('|')
            varaukset.append(muunna_varaustiedot(varaustiedot))
    return varaukset

def vahvistetut_varaukset(varaukset: list):
    for varaus in varaukset:
        if(varaus["varaus_vahvistettu"]):
            # f-lauseen sisällä avain '-merkeillä, koska f-lauseen alussa "
            print(f"- {varaus['nimi']}, {varaus['varattu_tila']}, {varaus['varauksen_pvm'].strftime('%d.%m.%Y')} klo {varaus['varauksen_klo'].strftime('%H.%M')}")

    print()

def pitkat_varaukset(varaukset: list):
    for varaus in varaukset:
        if(varaus["varauksen_kesto"] >= 3):
            print(f"- {varaus['nimi']}, {varaus['varauksen_pvm'].strftime('%d.%m.%Y')} klo {varaus['varauksen_klo'].strftime('%H.%M')}, kesto {varaus['varauksen_kesto']} h, {varaus['varattu_tila']}")

    print()

def varausten_vahvistusstatus(varaukset: list):
    for varaus in varaukset:
        if(varaus["varaus_vahvistettu"]):
            print(f"{varaus['nimi']} → Vahvistettu")
        else:
            print(f"{varaus['nimi']} → EI vahvistettu")

    print()

def varausten_lkm(varaukset: list):
    vahvistetutVaraukset = 0
    eiVahvistetutVaraukset = 0
    for varaus in varaukset[1:]:
        if(varaus["varaus_vahvistettu"]):
            vahvistetutVaraukset += 1
        else:
            eiVahvistetutVaraukset += 1

    print(f"- Vahvistettuja varauksia: {vahvistetutVaraukset} kpl")
    print(f"- Ei-vahvistettuja varauksia: {eiVahvistetutVaraukset} kpl")
    print()

def varausten_kokonaistulot(varaukset: list):
    varaustenTulot = 0
    for varaus in varaukset:
        if(varaus["varaus_vahvistettu"]):
            varaustenTulot += varaus["varauksen_kesto"]*varaus["hinta"]

    print("Vahvistettujen varausten kokonaistulot:", f"{varaustenTulot:.2f}".replace('.', ','), "€")
    print()

def main():
    varaukset = hae_varaukset("varaukset.txt")

    print("1) Vahvistetut varaukset")
    vahvistetut_varaukset(varaukset)
    print("2) Pitkät varaukset (≥ 3 h)")
    pitkat_varaukset(varaukset)
    print("3) Varausten vahvistusstatus")
    varausten_vahvistusstatus(varaukset)
    print("4) Yhteenveto vahvistuksista")
    varausten_lkm(varaukset)
    print("5) Vahvistettujen varausten kokonaistulot")
    varausten_kokonaistulot(varaukset)

if __name__ == "__main__":
    main()