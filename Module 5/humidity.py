
########################################################################
# Filename    : humidity.py
# Description : Display air temp, water temp, and humidity on lcd
# Author      : brhn
# modification: 7/13/2023
########################################################################

from PCF8574 import PCF8574_GPIO
import Adafruit_DHT
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import sleep, strftime
from datetime import datetime
import os

############################# INSTRUCTIONS #############################
# For this project you will need to output the data from multiple ds18b20s
# to an lcd like last project but with humidity added. Your read and sensor
# methods will be the same as in airtemp.py but you will need to read in
# humidity in the loop() method
#

# 3. loop()
#       - this method will take in the temp values and output
#         them to the lcd after. then will sleep for 3 seconds
#         before clearing and outputting humidity
#
# Note: you may need to change the pin numbers for the lcd object and
#       DHT_PIN
#
# SAMPLE OUTPUT:
#  A_Temp: 75.2 F
#  W_Temp: 45.7 F
#
#  sleep(3)
#
#  Humidity: 52%
#
#  sleep(3)





DHT_SENSOR = Adafruit_DHT.DHT11
#DHT_PIN = 21


#Hint: use os.listdir()     
def sensor():

    return ds18b20
    
  
def read(ds18b20): 
        
    return data
    
def loop(ds18b20):  

    mcp.output(3,1)     # LCD backlight
    lcd.begin(16,2)     # set number of lines and columns

    while(True):    #Output water temperature    
        #lcd.clear()
        lcd.setCursor(0,0)  # set cursor position
                           
        
def destroy(): #kill command, must clear lcd
    lcd.clear()
    quit()
    
    
PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
# Create PCF8574 GPIO adapter.
try:
    mcp = PCF8574_GPIO(PCF8574_address)
except:
    try:
        mcp = PCF8574_GPIO(PCF8574A_address)
    except:
        print ('I2C Address Error !')
        exit(1)

# Create lcd object and pass in MCP GPIO adapter. 
# lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp) 


if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        serialNums = sensor() #get serial number
        loop(serialNums)
    except KeyboardInterrupt: #kill
        destroy()

