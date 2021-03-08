# Usage :
1/ Connect the i2c LCD to the Pi :

  i2c_LCD pin :                  Pi pin :
    VCC                           VCC (5v)
    GND                           GND
    SCL                           SCL
    SDA                           SDA

2/ Log into the Pi and enabling i2c :
  - Enter "sudo raspi-config"
  - Advanced Options -> I2C -> Enable
  - Install SMBUS "sudo apt-get install python-smbus"
  - How to get my i2c device address ? Enter "sudo i2cdetect -y 1"

3/ Installing the library 
  - Clone this repository 
  - "cd Pi-i2c-LCD-Driver"
  - Next , put your i2c address in the library code (file "lcddriver.py")
  - Run test.py to test your LCD module
