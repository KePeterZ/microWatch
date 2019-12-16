def menu(options):
    currentSelected = 1
    while True:
        d.fill(0)
        colNums = [0, 8, 16, 24, 32, 40, 48, 56][:len(options)]
        for option in range(len(options)):
            d.text(options[option], 3, colNums[option])
        if not upButton.value():
            currentSelected -= 1
        if not downButton.value():
            currentSelected += 1
        d.rect(0, colNums[(currentSelected-1)%len(options)], 2, 8, 1)
        d.show()
        if not centerButton.value():
            d.fill(0)
            d.show()
            return options[(currentSelected-1)%len(options)]

def selecter(numOfNums):
    pass

addZeroes = lambda num : "0"+str(num) if len(str(num)) < 2 else str(num)
splitMinutes = lambda secs : "%s:%s" % (addZeroes(int(secs/60)), addZeroes(secs%60))

def dtext2(string, x, y):
    d.fill(0); d.text(string, x, y, 1); d.show();

def lwrite(r, g, b):
    l[0] = (r, g, b)
    l.write()

def sendSystemCmd(cmd, pcHost="188.6.197.143", pcPort=445):
        s = socket.socket()
        s.connect(socket.getaddrinfo(pcHost, pcPort)[0][-1])
        s.sendall(cmd.encode("utf-8"))
        return s.recv(512).decode('utf-8').rstrip()

def playIcon(positionX, positionY, size=0):
    d.line(positionX, positionY, positionX, positionY+16+size, 1)
    d.line(positionX, positionY, positionX+14+size, positionY+8+size, 1)
    d.line(positionX, positionY+16+size, positionX+14+size, positionY+8+size, 1)

def pauseIcon(positionX, positionY, size=0):
    d.rect(positionX, positionY, 6+int(size/2), 16+size, 1)
    d.rect(positionX+10+int(size/2), positionY, 6+int(size/2), 16+size, 1)

def nextIcon(positionX, positionY, size=0, secondOffset=5):
    d.line(positionX, positionY, positionX, positionY+16+size, 1)
    d.line(positionX, positionY, positionX+14+size, positionY+8+size, 1)
    d.line(positionX, positionY+16+size, positionX+14+size, positionY+8+size, 1)
    d.line(positionX+secondOffset, positionY, positionX+secondOffset, positionY+16+size, 1)
    d.line(positionX+secondOffset, positionY, positionX+14+size+secondOffset, positionY+8+size, 1)
    d.line(positionX+secondOffset, positionY+16+size, positionX+14+size+secondOffset, positionY+8+size, 1)

def prevIcon(positionX, positionY, size=0, secondOffset=5):
    d.line(positionX, positionY, positionX, positionY+16+size, 1)
    d.line(positionX, positionY, positionX-14-size, positionY+8+size, 1)
    d.line(positionX, positionY+16+size, positionX-14-size, positionY+8+size, 1)
    d.line(positionX-secondOffset, positionY, positionX-secondOffset, positionY+16+size, 1)
    d.line(positionX-secondOffset, positionY, positionX-14-size-secondOffset, positionY+8+size, 1)
    d.line(positionX-secondOffset, positionY+16+size, positionX-14-size-secondOffset, positionY+8+size, 1)

def dotDot(string, length):
    if len(string) > length:
        strTemp = string[:length-3]
        strTemp += "..."
    else:
        strTemp = string
    return strTemp

currScroll = 0
currBack = False

f = lambda string, max, iter : string[iter:max+iter]

# firstMenu = menu(["Time", "Music", "DrawTest"])
d.fill(0)
# firstMenu = "DrawTest"
firstMenu = menu(["Time",  "Music", "LEDs", "Networking", "Settings"])

if firstMenu == "LEDs":
    firstMenu = menu(["Siren", "Flashlight"])
if firstMenu == "Networking":
    firstMenu = menu(["Client", "Weather"])
if firstMenu == "Settings":
    firstMenu = menu(["Wifi info"])

if firstMenu == "Time":
    timeMenu = menu(["Clock", "Timer", "Stopwatch"])
    if timeMenu == "Clock":
        while not wifi.isconnected(): pass 
        import ntptime
        try: ntptime.settime()
        except: pass
        while True:
            d.fill(0)
            dtext("%s:%s:%s" % (
                addZeroes(time.localtime()[3]+1), 
                addZeroes(time.localtime()[4]), 
                addZeroes(time.localtime()[5])
            ), 16)
            dtext("%i. %i. %i." % (
                addZeroes(time.localtime()[0]), 
                addZeroes(time.localtime()[1]),
                addZeroes(time.localtime()[2])
            ), 40)
            try: d.rect(2, 2, 124, 62, 1)
            except: pass
            d.show()
    elif timeMenu == "Timer":
        currentSetTime = 0
        while True:
            d.fill(0)
            if not upButton.value():
                currentSetTime += 10
            if not downButton.value():
                currentSetTime -= 10
            if not leftButton.value():
                currentSetTime -= 120
            if not rightButton.value():
                currentSetTime += 120
            currentSetTime = currentSetTime if currentSetTime > 0 else 0
            dtext(splitMinutes(currentSetTime), 24)
            d.show()
            if not centerButton.value():
                break
        while currentSetTime > -1:
            d.fill(0)
            dtext(splitMinutes(currentSetTime), 24)
            d.show()
            currentSetTime -= 1
            time.sleep(1)
        while True:
            l[0] = (255, 0, 0)
            l.write()
            time.sleep(0.5)
            l[0] = (0, 0, 0)
            l.write()
            time.sleep(0.5)
    elif timeMenu == "Stopwatch":
        pass
elif firstMenu == "Wifi info":
    colNums = [0, 8, 16, 24, 32, 40, 48, 56]
    while not wifi.isconnected(): pass 
    for col in range(3):
        d.text(wifi.ifconfig()[col], 0, colNums[col], 1)
    d.show()
elif firstMenu == "Siren":
    while True:
        for c in range(254):
            l[0] = (c, 0, 0)
            l.write()
        for c in range(254):
            l[0] = (0, 0, c)
            l.write()
elif firstMenu == "Client":
    while not wifi.isconnected(): pass 
    s = socket.socket()
    s.connect(socket.getaddrinfo("192.168.0.33", 445)[0][-1])
    s.sendall(b'Hello, world')
    data = s.recv(1024).decode('utf-8')
    s.close()
    # d.fill(0)
    # d.text(data, 0, 0, 1)
    # d.show()
    dtext2(data, 0, 0)
elif firstMenu == "Weather":
    while not wifi.isconnected(): pass 
    s = socket.socket()
    s.connect(socket.getaddrinfo("192.168.0.33", 445)[0][-1])
    s.sendall(b'weather')
    data = s.recv(1024).decode('utf-8')
    s.close()
    # d.fill(0)
    # d.text(data, 0, 0, 1)
    # d.show()
    dtext2(data, 0, 0)
elif firstMenu == "Music":
    pcHost = "188.6.197.143"
    pcPort = 445
    while not wifi.isconnected(): pass 
    s = socket.socket()
    s.connect(socket.getaddrinfo(pcHost, pcPort)[0][-1])
    s.sendall(b'music')
    mStatus = s.recv(512).decode('utf-8').rstrip()
    dtext(mStatus, 24)
    d.show()
    cnt = 1
    while True:
        d.fill(0)
        if not leftButton.value():
            mStatus = sendSystemCmd('music-prev')
        elif not rightButton.value():
            mStatus = sendSystemCmd('music-next')
        elif not centerButton.value():
            mStatus = sendSystemCmd('music-pp')
        else:
            if cnt%5 == 1:
                mStatus = sendSystemCmd("music")
        try: 
            mStats = mStatus.split("-")
            dtext(str(mStatus.split("-")[0]), 8)
            szamNev = str(mStats[1].split("??")[0].strip())
            dtext(str(mStats[1].split("??")[0].strip()), 20)
            if str(mStatus.split("??")[-1]).strip() == "playing":
                pauseIcon(54, 40, 4)
            elif str(mStatus.split("??")[-1]).strip() == "paused":
                playIcon(54, 40, 4)
            prevIcon(28, 40, 0, 7)
            nextIcon(98, 40, 0, 7)

        except: 
            d.fill(0)
            dtext(str(mStatus.split("-")[0]), 16)
            pass
        finally:
            d.show()
            cnt += 1
elif firstMenu == "Flashlight":
    lwrite(255, 255, 255)
elif firstMenu == "DrawTest":
    # Test 
    playIcon(16, 0, 5)
    pauseIcon(16, 32, 4)
    prevIcon(64, 16, 0, 7)
    d.show()
    pass
