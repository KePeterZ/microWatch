def Clock():
    import ntptime
    ntptime.settime()
    while True:
        dtext("%i:%i:%i" % (time.localtime()[3]+1, time.localtime()[4], time.localtime()[5]), 24)
        d.show()