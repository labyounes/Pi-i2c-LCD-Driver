import lcddriver
from time import *

lcd = lcddriver.lcd()

#lcd.lcd_display_string("TEXT TO PRINT", ROW, COLUMN)
lcd.lcd_display_string("Hello world", 1)
