# Usage :
1/ Connect the LCD to the Pi via the i2c-adapter 

2/ Log into the Pi and enable i2c :
  - Enter "sudo raspi-config"
  - Advanced Options -> I2C -> Enable
  - Install SMBUS "sudo apt-get install python-smbus"
  - How to get my i2c device address ? Enter "sudo i2cdetect -y 1"

3/ Install the library 
  - Clone this repository 
  - "cd Pi-i2c-LCD-Driver"
  - Next , put your i2c address in the library code "lcddriver.py"
  - Run test.py to test your LCD 
