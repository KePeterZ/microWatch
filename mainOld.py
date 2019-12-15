from machine import Pin, I2C
import sh1106 # Import Display module
import time # Import time module
import network # Import network module
from neopixel import NeoPixel # Import led module
import random

# Declare NeoPixel LED as "l"
l = NeoPixel(Pin(15, Pin.OUT), 1) # create NeoPixel driver on GPIO0 for 8 pixels
l[0] = (0, 0, 0)
l.write() # write data to all pixels

# Declare display variables as "d"
i2c = I2C(scl=Pin(4), sda=Pin(5), freq=400000)
d = sh1106.SH1106_I2C(132, 64, i2c)
d.rotate(180)
d.sleep(False)
d.fill(0)
d.show()

# Declare wifi data as "wifi"
wifi = network.WLAN(network.STA_IF) # create station interface
wifi.active(True)
wifi.connect('AppleRouter', 'Boglya2018')
while not wifi.isconnected():
    pass
l[0] = (16, 16, 16); l.write()

# colNums = [0, 8, 16, 24, 32, 40, 48, 56]
# for value in range(4):
#     d.text(wifi.ifconfig()[value], 0, colNums[value])
# d.show()

upButton = Pin(12, Pin.IN, Pin.PULL_UP) # Up
downButton = Pin(13, Pin.IN, Pin.PULL_UP) # Down
centerButton = Pin(14, Pin.IN, Pin.PULL_UP) # Center
leftButton = Pin(2, Pin.IN, Pin.PULL_UP) # Left
rightButton = Pin(0, Pin.IN, Pin.PULL_UP) # Right

romeo = '''
KAR
(jön) Két nagy család élt a szép Veronába,
Ez lesz a szín, utunk ide vezet.
Vak gyűlölettel harcoltak hiába,
S polgárvér fertezett polgárkezet.
Vad ágyékukból két baljós szerelmes
Rossz csillagok világán fakadott,
És a szülők, hogy gyermekük is elvesz,
Elföldelik az ősi haragot.
Szörnyű szerelmüket, mely bírhatatlan,
Szülők tusáját, mely sosem apad,
Csak amikor már sarjuk föld alatt van:
Ezt mondja el a kétórás darab.
Néző, türelmes füllel jöjj, segédkezz,
És ami csonka itten, az egész lesz.
'''
# baseArray = ["alma", "korte", "potato"]
baseArray = romeo.split(" ")
curr = 1

while True:
    d.fill(0)
    if upButton.value() == 0 or rightButton.value() == 0:
        d.fill_rect(127, 0, 5, 20, 1)
        curr =  curr + 1
    if centerButton.value() == 0:
        d.fill_rect(127, 22, 5, 20, 1)
        curr =+ curr
    if downButton.value() == 0 or leftButton.value() == 0:
        d.fill_rect(127, 44, 5, 20, 1)
        curr = curr - 1
    d.text(baseArray[curr%len(baseArray)], 0, 0, 1)
    d.text(str(curr), 0, 8, 1)
    d.text(str(time.time()), 0, 16, 1)
    d.show()

# d.fill_rect(0, 0, 10, 10, 1)
# d.show()