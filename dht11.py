# Nacteni knihoven
import sys
import Adafruit_DHT

# Nastaveni typu senzoru a cisla propojovaciho pinu
sensor = Adafruit_DHT.DHT11
pin = 4

# Nacteni vlhkosti a teploty do promennych
while True:
        
    vlhkost, teplota = Adafruit_DHT.read_retry(sensor, pin)

    # Pokud jsou oba udaje nenulove, vytiskneme je,
    # pokud ne, vytiskneme informaci o chybe.
    if vlhkost is not None and teplota is not None:
        print('Teplota: {0:0.1f} stC, vlhkost: {1:0.1f} %RH.'.format(teplota, vlhkost))
    else:
        print('Chyba pri cteni udaju, zkuste znovu!')
        sys.exit(1)
