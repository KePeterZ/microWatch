from machine import Pin, I2C
from neopixel import NeoPixel # Import led module
import sh1106 # Import Display module


# Declare NeoPixel LED as "l"
l = NeoPixel(Pin(15, Pin.OUT), 1) # create NeoPixel driver on GPIO0 for 8 pixels
l[0] = (0, 0, 0)
l.write() # write data to all pixels

upButton = Pin(12, Pin.IN, Pin.PULL_UP) # Up
downButton = Pin(13, Pin.IN, Pin.PULL_UP) # Down
centerButton = Pin(14, Pin.IN, Pin.PULL_UP) # Center
leftButton = Pin(2, Pin.IN, Pin.PULL_UP) # Left
rightButton = Pin(0, Pin.IN, Pin.PULL_UP) # Right

# Declare display variables as "d"
i2c = I2C(scl=Pin(4), sda=Pin(5), freq=400000)
d = sh1106.SH1106_I2C(132, 64, i2c)
d.rotate(180)
d.sleep(False)
d.fill(0)
d.show()

red = 1
while True:
    d.fill(0)
    if upButton.value() == 0 or rightButton.value() == 0:
        red = red + 1
        l[0] = (red, 0, 0)
        l.write()
    if centerButton.value() == 0:
        pass
    if downButton.value() == 0 or leftButton.value() == 0:
        red = red - 1
        l[0] = (red, 0, 0)
        l.write()
    d.text(str(red), 0, 0, 1)
    d.show()