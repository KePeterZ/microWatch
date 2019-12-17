from machine import Pin, I2C
from neopixel import NeoPixel
import sh1106 # Import Display module
import time # Import time module
import network # Import network module
import random
import usocket as socket

# Declare NeoPixel LED as "l"
l = NeoPixel(Pin(15, Pin.OUT), 1) 
l[0] = (0, 0, 0); l.write()
# create NeoPixel driver on GPIO0 for 1 pixel

# Declare display variables as "d"
d = sh1106.SH1106_I2C(
    132, 64, I2C(scl=Pin(4), 
    sda=Pin(5), freq=400000))
# Rotate screen into correct orientation
d.rotate(180)

dtext = lambda string, row : d.text(str(string), int((132-len(string)*8)/2), row, 1)
btext = lambda string, row : d.text(string, int((132-len(string)*8)/2), row, 1)

def getFile(fileLoc, RorW="r", whatToWrite=None):
    if RorW == "r":
        with open(fileLoc, "r") as fileThing:
            return fileThing.readline().strip()
    elif RorW == "w":
        with open(fileLoc, "w") as fileThing:
            fileThing.write(whatToWrite)
            return True

wifiNetwork = getFile("/now.config", "r")
dtext("Made by", 8)
dtext("KePeterZ", 16)
dtext("Connecting", 32)
dtext(wifiNetwork.split(":")[0], 40)
try: dtext(wifiNetwork.split(":")[1], 48)
except: pass
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

# If rightButton pressed on bootup, reflash main.py to working one
if not rightButton.value():
    d.fill(0)
    dtext("FLASING", 16)
    dtext("BACK", 24)
    d.show()
    workingCodeFile = open("/mainWorking.py", "r")
    lastCode = workingCodeFile.readlines()
    workingCodeFile.close()
    newMain = open("/main.py", "w")
    for line in lastCode: newMain.write(line)
    newMain.close()

# Declare network parameters as "wifi" 
wifi = network.WLAN(network.STA_IF); 
# Create wifi class
wifi.active(True) 
# Activate interface
with open("./now.config", "r") as w: wifiNetwork = w.readline().strip().split(":")
try: wifi.connect(wifiNetwork[0], wifiNetwork[1])
except: wifi.connect(wifiNetwork[0])

# Wait until connected to wifi
# But set timeout to 3 seconds
# t1 = time.time()
# while not wifi.isconnected(): pass 
# while True:
#     if time.time()-t1 > 1: break
#     if wifi.isconnected(): break