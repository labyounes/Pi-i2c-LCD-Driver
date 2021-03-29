import lcddriver
from time import *

lcd = lcddriver.lcd()

#lcd.lcd_display_string("TEXT TO PRINT", ROW, COLUMN)

lcd.lcd_display_string("Blog", 1)      #Show on display , 1.Row , 1.Column 

lcd.lcd_display_string("BerryBase", 2) #Show on display , 2.Row , 1.Column 

sleep(3)                               # 3 Seconds

lcd.lcd_clear()                        # Clear display
