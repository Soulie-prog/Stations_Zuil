kluisbestand = 'fa_kluizen.txt'

def lees_kluizen():
    try:
        with open(kluisbestand, 'r') as file:
            kluizen = file.readlines()
            return kluizen
    except FileNotFoundError:
        return []

def schrijf_kluizen(kluizen):
    with open(kluisbestand, 'w') as file:
        for kluis in kluizen:
            file.write(kluis)

def aantal_kluizen_vrij():
    kluizen = lees_kluizen()
    return 12 - len(kluizen)

def nieuwe_kluis():
    if aantal_kluizen_vrij() == 0:
        return -2  # Geen kluizen beschikbaar

    kluis_nummer = int(input("Voer een kluisnummer in (1 t/m 12): "))
    if kluis_nummer < 1 or kluis_nummer > 12:
        return -1  # Ongeldig kluisnummer

    kluizen = lees_kluizen()
    for kluis in kluizen:
        if int(kluis.split(';')[0]) == kluis_nummer:
            return -1  # Kluisnummer al in gebruik

    kluis_code = input("Voer een kluiscode in (minimaal 4 tekens, geen ';'): ")
    if len(kluis_code) < 4 or ';' in kluis_code:
        return -1  # Ongeldige code

    kluizen.append(f"{kluis_nummer};{kluis_code}\n")
    schrijf_kluizen(kluizen)
    return kluis_nummer

def kluis_openen():
    kluis_nummer = int(input("Voer uw kluisnummer in: "))
    kluis_code = input("Voer uw kluiscode in: ")

    kluizen = lees_kluizen()
    for kluis in kluizen:
        nummer, code = kluis.strip().split(';')
        if int(nummer) == kluis_nummer and code == kluis_code:
            return True

    return False

def kluis_teruggeven():
    kluis_nummer = int(input("Voer uw kluisnummer in: "))
    kluis_code = input("Voer uw kluiscode in: ")

    kluizen = lees_kluizen()
    nieuwe_kluizen = []
    kluis_gevonden = False

    for kluis in kluizen:
        nummer, code = kluis.strip().split(';')
        if int(nummer) == kluis_nummer and code == kluis_code:
            kluis_gevonden = True
        else:
            nieuwe_kluizen.append(f"{nummer};{code}\n")

    if kluis_gevonden:
        schrijf_kluizen(nieuwe_kluizen)
        return True
    else:
        return False

# Hoofdmenu
while True:
    print("Kluisverhuur Menu:")
    print("1: Ik wil weten hoeveel kluizen nog vrij zijn")
    print("2: Ik wil een nieuwe kluis")
    print("3: Ik wil even iets uit mijn kluis halen")
    print("4: Ik geef mijn kluis terug")

    keuze = int(input("Voer uw keuze in: "))

    if keuze == 1:
        print(f"Aantal kluizen vrij: {aantal_kluizen_vrij()}")
    elif keuze == 2:
        resultaat = nieuwe_kluis()
        if resultaat == -2:
            print("Er zijn geen kluizen beschikbaar.")
        elif resultaat == -1:
            print("Ongeldige invoer. Probeer opnieuw.")
        else:
            print(f"Uw kluis is gekoppeld aan kluisnummer {resultaat}.")
    elif keuze == 3:
        if kluis_openen():
            print("Kluis geopend!")
        else:
            print("Ongeldige combinatie van kluisnummer en code.")
    elif keuze == 4:
        if kluis_teruggeven():
            print("Kluis is succesvol teruggegeven.")
        else:
            print("Ongeldige combinatie van kluisnummer en code.")
    else:
        print("Ongeldige keuze. Probeer opnieuw.")
