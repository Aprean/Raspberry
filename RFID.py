#import knihoven
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
#uložení do proměné
ctecka = SimpleMFRC522()

#výpis textu
print("přiložte kartu")

text = ctecka.read()
text = str(text[0])

print(text)

GPIO.cleanup()

#přidání podmínek)
text = ctecka.read()
text = str(text[0])
if text == "701117799140":
      print("přístup povolen")

if text != "701117799140" and text != "":
      print("přístup odepřen")
Zdroj: https://www.itnetwork.cz/hardware-pc/raspberry-pi/raspberry-pi-pripojeni-rfid-ctecky
