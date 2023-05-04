from datetime import datetime #pro praci s datumem a casem
import time
import RPi.GPIO as GPIO #import knihovnu gpio
import matplotlib.pyplot as plt #import kniovny na grafy

GPIO.setmode(GPIO.BCM) #nastavit druh gpio asi
GPIO.setwarnings(False) #vypnout varování

global i #počáteční počet zápisů/měření
i=1

#nastavení pinů
teplota_a_vlhkost_pin = 5#
co2_pin = 2
jas_pin = 3
volba_pin =4 
red_pin = 17#
green_pin = 27#
blue_pin = 22#
button_read_pin = 15
button_start_stop_pin = 18
button_vykreslit_graf = 14

#definování pinů IN/OUT
GPIO.setup(teplota_a_vlhkost_pin, GPIO.IN)
GPIO.setup(co2_pin, GPIO.IN)
GPIO.setup(jas_pin, GPIO.IN)
GPIO.setup(volba_pin, GPIO.IN)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)
GPIO.setup(button_read_pin, GPIO.IN)
GPIO.setup(button_start_stop_pin, GPIO.IN)
GPIO.setup(button_vykreslit_graf, GPIO.IN)

#vypnutí všech OUT pinů
GPIO.output(red_pin, GPIO.LOW)
GPIO.output(green_pin, GPIO.LOW)
GPIO.output(blue_pin, GPIO.LOW)


def mereni_zapis_hodnot():
  global i
  with open("mereni.txt", "a") as soubor: #při otevření připíše hodnoty do souboru proto "a" append
    cislo_mereni = str(i)
    
    i=i+1
    aktualni_cas = str(datetime.now()) #str aby to bylo v textu, jebat to všude
    teplota = str() #do závorek zapsat čtení senzoru, popřípadně to hodit do funkce
    vlhkost = str()
    co2 = str()
    jas = str()
    volba = str()

    #druhá možnost zápisu: trošku lepší, podporuje i další řádek s {/n}
    radek_pro_zapis = f"{cislo_mereni}#{aktualni_cas}#{teplota}#{vlhkost}#{co2}#{jas}#{volba}"
    radek_pro_vypis = f"Číslo měření: {cislo_mereni} v čase: {aktualni_cas};;; teplota: {teplota}C; vlhkost:{vlhkost}%; CO2:{co2}PPM; jas:{jas}lx; volba topení:{volba}%"

    #zapsat řádek do souboru
    soubor.write(radek_pro_zapis)
    soubor.write("/n")

    print(radek_pro_vypis)

    time.sleep(0.5) #zpoždění v s aby to nebylo v piči

def vykresleni_grafu():
  pocet_namerenych_hodnot = 0 #definujem
  
  with open("mereni.txt", "r") as soubor:
    obsah_souboru = soubor.readlines() #přečíst úplně vše v souboru po řádcích, každý řádek je prvek pole
    pocet_namerenych_hodnot = len(obsah_souboru) #sebrat počet řádků. použití len = lenght
  
    #vezmem hodnoty ze souboru
    cisla_mereni = [] #vypíšu hodnoty do polí, množný název protože hodně hodnot
    aktualni_casy = []
    teploty = []
    vlhkosti = []
    co2ky = []
    jasy = []
    volby = []
  
    #zpracování řádek po řádku
  for radek in obsah_souboru:
    if radek == "":#prázdný řádek přeskočím
      continue

    radek_rozdeleny = radek.split("#") #čím budeme dělit řádky, znak rozdělení

    #naplním si připravená pole hodnotami
    cisla_mereni.append(float(radek_rozdeleny[0])) #vložíme do pole hodnoty z první pozice
    aktualni_casy.append(radek_rozdeleny[1])
    teploty.append(float(radek_rozdeleny[2]))
    vlhkosti.append(float(radek_rozdeleny[3]))
    co2ky.append(float(radek_rozdeleny[4]))
    jasy.append(float(radek_rozdeleny[5]))
    volby.append(radek_rozdeleny[6])
    
    print("graf vykreslen")

  pocet_namerenych_hodnot = len(cisla_mereni) #zapíšeme kolik jsme opravdu načetli hodnot

  #vykreslíme grafy
  x = list(range(0, pocet_namerenych_hodnot)) #příprava osy x

  plt.plot(x, cisla_mereni, "r") #zadáme hodnoty do osy Y a využijeme předešlou x
  #plt.plot(x, vlhkosti, "b") #písmenka za tím jsou barvy

  plt.grid() #ukázat mřížku
  plt.xlabel("pořadí měření [-]") #popisek osy x
  
  plt.savefig("mereni.png", dpi=600) #uložit jako PNG
  plt.show() #ukázat graf

while True: #hlavní loop
  GPIO.output(red_pin, GPIO.HIGH) #svítí jen červená
  GPIO.output(green_pin, GPIO.LOW)
  GPIO.output(blue_pin, GPIO.LOW)
  
  if GPIO.input(button_start_stop_pin): #zapnutí loopu zapnutí
    print("start")
    time.sleep(1.5) #prevence aby rychle se zas loop nevypnul, stejné jako všechny 1.5s
    
    while True: #loop kontoroly výpisu a zápisu
      GPIO.output(red_pin, GPIO.LOW) #svítí jen zelená
      GPIO.output(green_pin, GPIO.HIGH)
      GPIO.output(blue_pin, GPIO.LOW)
      
      if GPIO.input(button_start_stop_pin) == True: #vypnutí loopu zapnutí
        print("stop")
        time.sleep(1.5)
        break
        
      elif GPIO.input(button_vykreslit_graf) == True:
        vykresleni_grafu()
        time.sleep(1.5)
        
      while GPIO.input(button_read_pin) == True:
        GPIO.output(blue_pin, GPIO.HIGH) #zapnutí modré ledky, jakože čte
        mereni_zapis_hodnot()
        time.sleep(1) #delay aby se to necetlo furt
        GPIO.output(blue_pin, GPIO.LOW) #vypnutí modré ledky, jakože dočetla
        
      
