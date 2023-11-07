import datetime
import random
import time
import sys

# datum van computer op dat moment
datum = datetime.datetime.now()
print(datum)

# kijkt specifiek naar de uren van de computer
Tijd_Nu = datetime.datetime.now().hour

while True:
    # vraagt om een input
    bericht = input('Vul hier uw bericht in alstublieft (Max 140 karakters):')

    if len(bericht) > 140:
        print('Uw bericht is langer dan 140 karakters. Probeer opnieuw.')
        continue  # langer dan 140 karakters dus stel de vraag opnieuw

    if len(bericht) == 0:
        print('Uw bericht is leeg. Probeer opnieuw.')
        continue  # langer dan 140 karakters dus stel de vraag opnieuw


    print('Uw bericht is opgeslagen!')
    break  # loop stopt

# vraagt om bevestiging
confirmatie = input('Weet u zeker dat u wil doorgaan? (ja/nee)').lower()

if confirmatie == 'ja':
    print('Doorgaan...')
else:
    print('Doorgaan geannuleerd.')
    sys.exit()  # Stop  programma als de input 'nee' is

Naam = input('Vul hier uw naam in (Klik gelijk op ENTER als u anoniem wil blijven):')

if len(Naam) >= 1:
    print('Hallo', Naam)
else:
    Naam = 'Anoniem'
    print('U bent anoniem')

# lijst van stations word geopend en gelezen
with open('data.txt', 'r') as file:
    lijst = file.readlines()

# Kiest een random station uit
Station_Keuze = random.choice(lijst).strip(' \t\n')
print(f'Uw bericht is vanaf Station {Station_Keuze} gemaakt.')

Goedkeuring = input('Weet u zeker dat u dit bericht wil verzenden? (ja/nee)').lower()

if Goedkeuring == 'ja':
    print('Bericht is verzonden')
else:
    print('Bericht wordt verwijderd...')
    print('Bericht verwijderd!')

# Controleer het tijdstip van de dag en geef een passende groet (extra)
if 12.00 <= Tijd_Nu < 18.00:
    print('Heb nog een prettige middag dag!')
elif 6.00 <= Tijd_Nu < 11.59:
    print('Fijne dag!')
else:
    print('Heb nog een fijne avond!')

# Voeg de gegevens van het bericht toe aan een CSV-bestand
with open('Check_Bericht.csv', 'a') as file:
    file.write(f'{datum}, {Station_Keuze}, {Naam}, {bericht} \n')

