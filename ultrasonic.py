import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pin_in = 8
GPIO.setup(pin_in, GPIO.IN)           

pin_out = 7                            
frekvence = 20                        
strida = 1                            
GPIO.setup(pin_out, GPIO.OUT)            
signal1 = GPIO.PWM(pin_out , frekvence)    
signal1.start(strida) 


while True:
  suma = 0
  for i in range(10):                   
     while GPIO.input(pin_in) == False:  
       time.sleep(0.00000001)
     start= time.time()                 
     while GPIO.input(pin_in) == True:   
       time.sleep(0.00000001)
     cas= time.time() - start           
     suma = suma + cas                  

  prumer = suma / 10                    
  print "Cas = " + str(prumer) + " ... tomu odpovida vzdalenost : " + str(int((prumer * 340 / 2) * 100)) + " cm"
  time.sleep(0.3)
