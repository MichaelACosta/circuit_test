def stop():
    print('Stop')

def turnLeft():
    print('Turn Left')

def turnRight():
    print('Turn Right')

def stopGoAhead(odometry, meters):
    return (odometry/1200.0)*3.14*0.34 >= meters

def goAhead(meters):
    print(stopGoAhead(4320.0, meters))

def listener():
    goAhead(9.0)
    turnLeft()
    goAhead(5.0)
    turnRight()
    goAhead(7.8)
    turnLeft()
    goAhead(3.6)
    turnLeft()
    goAhead(3.0)
    turnLeft()
    goAhead(3.6)
    turnRight()
    goAhead(13.2)
    turnLeft()
    goAhead(5.4)
    stop()

if __name__ == '__main__':
    listener()