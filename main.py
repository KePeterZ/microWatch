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
    
addZeroes = lambda num : "0"+str(num) if len(str(num)) < 2 else str(num)
splitMinutes = lambda secs : "%s:%s" % (addZeroes(int(secs/60)), addZeroes(secs%60))
def dtext2(string, x, y):
    d.fill(0); d.text(string, x, y, 1); d.show();

firstMenu = menu(["Time", "Wifi", "Siren", "Client", "Weather", "Music"])
if firstMenu == "Time":
    timeMenu = menu(["Clock", "Timer", "Stopwatch"])
    if timeMenu == "Clock":
        while not wifi.isconnected(): pass 
        import ntptime
        ntptime.settime()
        while True:
            d.fill(0)
            dtext("%s:%s:%s" % (
                addZeroes(time.localtime()[3]+1), 
                addZeroes(time.localtime()[4]), 
                addZeroes(time.localtime()[5])
            ), 16)
            dtext("%i. %i. %i." % (
                time.localtime()[0], 
                time.localtime()[1],
                time.localtime()[2]
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
                currentSetTime -= 1
            if not rightButton.value():
                currentSetTime += 1
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
elif firstMenu == "Wifi":
    colNums = [0, 8, 16, 24, 32]
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
    s.connect(socket.getaddrinfo("192.168.0.33", 80)[0][-1])
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
    s.connect(socket.getaddrinfo("192.168.0.33", 80)[0][-1])
    s.sendall(b'weather')
    data = s.recv(1024).decode('utf-8')
    s.close()
    # d.fill(0)
    # d.text(data, 0, 0, 1)
    # d.show()
    dtext2(data, 0, 0)
elif firstMenu == "Music":
    while not wifi.isconnected(): pass 
    s = socket.socket()
    s.connect(socket.getaddrinfo("192.168.0.33", 80)[0][-1])
    s.sendall(b'music')
    mStatus = s.recv(512).decode('utf-8').rstrip()
    dtext(mStatus, 24)
    d.show()
    cnt = 1
    while True:

        d.fill(0)
        if not leftButton.value():
            s = socket.socket()
            s.connect(socket.getaddrinfo("192.168.0.33", 80)[0][-1])
            s.sendall(b'music-prev')
            mStatus = s.recv(512).decode('utf-8').rstrip()
        elif not rightButton.value():
            s = socket.socket()
            s.connect(socket.getaddrinfo("192.168.0.33", 80)[0][-1])
            s.sendall(b'music-next')
            mStatus = s.recv(512).decode('utf-8').rstrip()
        elif not centerButton.value():
            s = socket.socket()
            s.connect(socket.getaddrinfo("192.168.0.33", 80)[0][-1])
            s.sendall(b'music-pp')
            mStatus = s.recv(512).decode('utf-8').rstrip()
        elif cnt%10 == 1:
            s = socket.socket()
            s.connect(socket.getaddrinfo("192.168.0.33", 80)[0][-1])
            s.sendall(b'music')
            mStatus = s.recv(512).decode('utf-8').rstrip()
        try: 
            mStats = mStatus.split("-")
            dtext(str(mStatus.split("-")[0]), 16)
            dtext(str(mStats[1]).strip(), 24)
        except: 
            d.fill(0)
            dtext(str(mStatus.split("-")[0]), 16)
            pass
        finally:
            d.show()
            cnt += 1