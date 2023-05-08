#import knihovny
import RPi.GPIO as GPIO
#nastavení módu na používání čísla portu dle desky
GPIO.setmode(GPIO.BOARD)
#nastavení portu na input a nastavení výstupů 0 a 1
GPIO.setup(18, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#proměnná
a = 0
#cyklus 
while True:
        if GPIO.input(18) and a != 1:
            print("open")
            a = 1


        elif GPIO.input(18) == False and a != 2:
              print("close")
              a = 2
