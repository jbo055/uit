
def valider_postadresse(adresse):
    if adresse[:4].isnumeric() and adresse[4] == ' ' and adresse[5:].isupper():
        return True
    return False


postadresser = [
    '1234 OSLO',       # Gyldig
    '5678 BERGEN',     # Gyldig
    '123 OSLO',        # Ugyldig (postnummeret har ikke fire sifre)
    '12345 OSLO',      # Ugyldig (postnummeret har mer enn fire sifre)
    '1234 oslo',       # Ugyldig (poststedet er ikke i store bokstaver)
    'OSLO 1234',       # Ugyldig (poststedet kommer før postnummeret)
    '1234 OSLO S',     # Gyldig (poststed med mellomrom)
    '1234 OSLO SØR',   # Gyldig (poststed med mellomrom og spesialtegn)
]

for adresse in postadresser:
    if valider_postadresse(adresse):
        print(f"'{adresse}' er en gyldig postadresse.")
    else:
        print(f"'{adresse}' er en ugyldig postadresse.")