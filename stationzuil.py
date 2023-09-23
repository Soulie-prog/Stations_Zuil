import datetime
import random
import time
import sys

bericht = input('Vul hier uw bericht in alstublieft (Max 140 karakters):')

if 1 <= len(bericht) <= 140:
    print('Uw bericht is opgeslagen!')

elif len(bericht) > 140:
    print('Uw bericht is langer dan 140 karakters')
elif len(bericht) == 0:
    print('u heeft niks ingevuld')
    print('Progamma sluiten...')
    time.sleep(2)
    print( 'Programma gesloten.')
    sys.exit()

confirmatie= input('weet u zeker dat u wil doorgaan? (ja/nee)')

if confirmatie == 'ja':
    print('Doorgaan...')

else:
    print('Doorgaan geannuleerd.')
    sys.exit()



Naam  = input('Vul hier uw naam in (Klik gelijk op ENTER als u anoniem wil blijven):')

if len(Naam) >= 1:
    print('hallo', Naam)

else:
    print('U bent anoniem')

Stations_lijst= ['alkmaar', 'Utrecht', 'Zeist', 'Maarn']

Station_Keuze = random.choice(Stations_lijst)  # Kiest een random station uit lijst

print(f'Uw bericht is vanaf Station {Station_Keuze} gemaakt.')

Goedkeuring= input('weet u zeker dat u dit bericht wil verzenden?(ja/nee)')

if Goedkeuring == 'ja':
    print('Bericht is verzonden')

else:
    print('Bericht wordt verwijderd...')
    print('Bericht verwijderd!')

Tijd_Nu = datetime.datetime.now().hour

if 6 <= Tijd_Nu < 18:
    print(' Heb nog een prettige dag!')
elif 1 <= Tijd_Nu < 5:
    print('')
else:
    print('Heb nog een fijne avond!')

