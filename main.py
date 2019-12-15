req = 1
reqSaved = []

while True:
    d.fill(0)
    if not upButton.value():
        req += 1
    if not centerButton.value():
        reqSaved.append(req)
    if not downButton.value():
        req -= 1
    d.text(str(reqSaved), int((132-len(str(reqSaved))*8)/2)-8, 40, 1)
    d.text(str(req), 0, 0, 1)
    d.show()