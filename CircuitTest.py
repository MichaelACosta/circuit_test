#!/usr/bin/env python
import rospy
import csv
from std_msgs.msg import Int16
from std_msgs.msg import Bool

leftValue = 0
rightValue = 0

def stop():
    print('Stop')

def turnLeft():
    global rightValue
    try:
        startMovimentTurnLeft()
    except rospy.ROSInterruptException:
        pass
    while not rightValue >= 953:
        rospy.spin()
    try:
        stopMoviment()
    except rospy.ROSInterruptException:
        pass

def startMovimentTurnLeft():
    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    move = rospy.Publisher('channel_x', Int16, queue_size=1)
    move.publish(175)

def turnRight():
    global leftValue
    clearOdeometry = rospy.Publisher('pattern', Bool, queue_size=1)
    clearOdeometry.publish(True)
    move = rospy.Publisher('channel_x', Int16, queue_size=1)
    move.publish(95)
    while not leftValue >= 953:
        None
    clearOdeometry.publish(True)
    move.publish(135)

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

def stopMoviment():
    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    stop = rospy.Publisher('channel_y', Int16, queue_size=1)
    stop.publish(135)

def listener():
    with open('circuit.csv') as csvfile:
        readLine = csv.reader(csvfile, delimiter='\n')
        for line in readLine:
            if line[0] == 'R':
                turnRight()
            elif line[0] == 'L':
                turnLeft()
            elif line[0] == 'S':
                stop()
            else:
                goAhead(line[0])

if __name__ == '__main__':
    listener()