#https://www.blog.berrybase.de/

import os
import subprocess
from time import *
import lcddriver 
import RPi.GPIO as GPIO 

#Function to get local IP
def get_ip():
    res = str(subprocess.check_output(['hostname', '-I'])).split(' ')[0].replace("b'","")
    if (len(res) != 13):
        return(" Finding IP...")
    else:
        return(res)

#Get CPU temperature 
def measure_temp():
    temp = os.popen("vcgencmd measure_temp").readline()
    t= temp[5:9]
    return(t)
    

L = 21                                          #Fan Pin 

#GPIO Setup:
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)                          #GPIO Mode BCM
GPIO.setup(L,GPIO.OUT)                          #Fan Pin as Output 

#LCD Init:
lcd = lcddriver.lcd()                           #Init LCD Display

lcd.lcd_display_string("****************",1)    #1.line
lcd.lcd_display_string("****************",2)    #2.line
sleep(4)                                        #Delay
lcd.lcd_clear()                                 #Clear Display

#main
def main():


    while True:
        
        T= measure_temp()                        #Get CPU Temperature
        
        IP= str(get_ip())                        #Convert IP to String
        tmp = float(T)                           #Get Temperature as float
        
        
        
        lcd.lcd_display_string("CPU-Temp = "+T,1)  #Display CPU Temperature on 1.line
        lcd.lcd_display_string("IP="+IP,2)         #Display Pi-IP on 2.line
        
        sleep(0.5)                               #Update Screen every 0.5 Second
        
        if (tmp>65):                   
            GPIO.output(L,GPIO.HIGH)             #Turn the fan ON
            
        if (tmp<55): 
            GPIO.output(L,GPIO.LOW)              #Turn the fan OFF
             
#Execute main code
if __name__ == "__main__":
    main()
