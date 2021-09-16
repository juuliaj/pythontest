import http_pyynto

def ryhmittele_toimipaikoittain(numero_sanakirja):
    paikat = {}
    for numero, nimi in numero_sanakirja.items():
        if nimi not in paikat:
            paikat[nimi] = []

        paikat[nimi].append(numero)

    return paikat

def etsi_postinumerot(paikka):

    postinumerot = http_pyynto.hae_postinumerot()

    postitmp = ryhmittele_toimipaikoittain(postinumerot)

    if paikka in postitmp:
        postitmp[paikka].sort()

        loydetyt_str = ', '.join(postitmp[paikka])
        return loydetyt_str

    else:
        return "Toimipaikkaa ei löytynyt"

def main():
    postitoimipaikka = input('Kirko9ita postitoimipaikka: ').upper()

    print(etsi_postinumerot(postitoimipaikka))

if __name__ == '_main_':
    main()
   

