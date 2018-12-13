#!/usr/bin/env python
import rospy
from std_msgs.msg import Int16
from std_msgs.msg import Bool

leftValue = 0
rightValue = 0

def stop():
    print('Stop')

def turnLeft():
    global rightValue
    clearOdeometry = rospy.Publisher('pattern', Bool, queue_size=1)
    clearOdeometry.publish(True)
    move = rospy.Publisher('channel_x', Int16, queue_size=1)
    move.publish(175)
    while not rightValue >= 953:
        None
    clearOdeometry.publish(True)
    move.publish(135)

def turnRight():
    print('Turn Right')

def stopGoAhead(odemetryValue, meters):
    return (odemetryValue/1200.0)*3.14*0.34 >= meters

def goAhead(meters):
    global leftValue
    global rightValue
    clearOdeometry = rospy.Publisher('pattern', Bool, queue_size=1)
    clearOdeometry.publish(True)
    move = rospy.Publisher('channel_y', Int16, queue_size=1)
    move.publish(175)
    while not (stopGoAhead(rightValue, meters) or stopGoAhead(leftValue, meters)):
        None
    clearOdeometry.publish(True)
    move.publish(135)

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