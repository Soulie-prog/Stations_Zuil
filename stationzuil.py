import datetime
import random
import time
import sys
datum = datetime.datetime.now()
print(datum)
Tijd_Nu = datetime.datetime.now().hour

while True:
    bericht = input('Vul hier uw bericht in alstublieft (Max 140 karakters):')

    if len(bericht) > 140:
        print('Uw bericht is langer dan 140 karakters. Probeer opnieuw.')
        continue  #  continue om opnieuw te vragen om een bericht

    if len(bericht) == 0:
        print('Uw bericht is leeg. Probeer opnieuw.')
        continue  # continue om opnieuw te vragen om een bericht

    print('Uw bericht is opgeslagen!')
    break # geeft een break aan wat de while loop stopt




confirmatie= input('weet u zeker dat u wil doorgaan? (ja/nee)').lower()

if confirmatie == 'ja':
    print('Doorgaan...')

else:
    print('Doorgaan geannuleerd.')
    sys.exit()



Naam  = input('Vul hier uw naam in (Klik gelijk op ENTER als u anoniem wil blijven):')

if len(Naam) >= 1:
    print('hallo', Naam)

else:
    Naam = 'Anoniem'
    print('U bent anoniem')

with open('data.txt', 'r') as file:
    lijst = file.readlines()

Station_Keuze = random.choice(lijst).strip(' \t\n')
print(f'Uw bericht is vanaf Station {Station_Keuze} gemaakt.')

Goedkeuring = input('weet u zeker dat u dit bericht wil verzenden?(ja/nee)').lower()

if Goedkeuring == 'ja':
    print('Bericht is verzonden')

else:
    print('Bericht wordt verwijderd...')
    print('Bericht verwijderd!')

if 12.00 <= Tijd_Nu < 18.00:
    print('Heb nog een prettige middag dag!')
elif 6.00 <= Tijd_Nu < 11.59:
    print('fijne dag!')
else:
    print('Heb nog een fijne avond!')

with open('Check_Bericht.csv','a') as file:
    file.write(f'{datum}, {Station_Keuze}, \" {Naam} \",\" {bericht} \" \n')


