def stop():
    print('Stop')

def turnLeft():
    print('Turn Left')

def turnRight():
    print('Turn Right')

def goAhead(meters):
    print(meters)

def listener():
    goAhead(9)
    turnLeft()
    goAhead(5)
    turnRight()
    goAhead(7.8)
    turnLeft()
    goAhead(3.6)
    turnLeft()
    goAhead(3)
    turnLeft()
    goAhead(3.6)
    turnRight()
    goAhead(13.2)
    turnLeft()
    goAhead(5.4)
    stop()

if __name__ == '__main__':
    listener()