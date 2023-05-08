# instalace knihovny pro sériovou komunikaci
pip install pyserial

import serial   #import knihovny
ser = serial.Serial('COM5', 9600)  #uložení specifikace séeriové komunikace, nastavení COM dle Arduino IDE
while 1:                           #smyčka, aby se program nevypl po každém zapuntí
    val = int(input("Vlož  1"))
    ser.write(val)                 #použití komunikace zapasné do proměné a write vypíše co uživatel zadal

#program na čtení dat z Arduina
import serial       #import knihovny

ser = serial.Serial('COM5', 9600, timeout=1)    #nastavení proměnné, timeout na chvíli zastaví program 

while 1:
    pre = ser.readline().decode('utf-8').rstrip()       #čtení z proměnné, dekódování, rstrip odstraní přebytečtné 
    print(pre)
