from machine import Pin, I2C
from neopixel import NeoPixel
import sh1106 # Import Display module
import time # Import time module
import network # Import network module
import random
import usocket as socket

# Declare NeoPixel LED as "l"
l = NeoPixel(Pin(15, Pin.OUT), 1) 
# create NeoPixel driver on GPIO0 for 1 pixel

# Declare display variables as "d"
d = sh1106.SH1106_I2C(
    132, 64, I2C(scl=Pin(4), 
    sda=Pin(5), freq=400000))
# Rotate screen into correct orientation
d.rotate(180)

dtext = lambda string, row : d.text(str(string), int((132-len(string)*8)/2)-8, row, 1)
btext = lambda string, row : d.text(string, int((132-len(string)*8)/2)-8, row, 1)

dtext("Made by", 16)
dtext("KePeterZ", 24)
dtext("Connecting", 40)
d.show()

buttons = {
    "up": 12, 
    "down": 13, 
    "center": 14, 
    "left": 2,
    "right": 0
    }
for button in buttons.keys(): 
    exec(
        button+
        "Button = Pin(buttons[button], Pin.IN, Pin.PULL_UP)")

# Declare network parameters as "wifi" 
wifi = network.WLAN(network.STA_IF); 
# Create wifi class
wifi.active(True) 
# Activate interface
wifi.connect('AppleRouter', 'Boglya2018')

# Wait until connected to wifi
while not wifi.isconnected(): pass 