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
    try:
        startMovimentTurnRight()
    except rospy.ROSInterruptException:
        pass
    while not leftValue >= 953:
        rospy.spin()
    try:
        stopMoviment()
    except rospy.ROSInterruptException:
        pass

def startMovimentTurnRight():
    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    move = rospy.Publisher('channel_x', Int16, queue_size=1)
    move.publish(95)

def stopGoAhead(odemetryValue, meters):
    return (odemetryValue/1200.0)*3.14*0.34 >= meters

def goAhead(meters):
    global leftValue
    global rightValue
    try:
        startMovimentAhead()
    except rospy.ROSInterruptException:
        pass
    while not (stopGoAhead(rightValue, meters) or stopGoAhead(leftValue, meters)):
        rospy.spin()
    try:
        stopMoviment()
    except rospy.ROSInterruptException:
        pass

def startMovimentAhead():
    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    move = rospy.Publisher('channel_y', Int16, queue_size=1)
    move.publish(175)

def stopMoviment():
    pub = rospy.Publisher('pattern', Bool, queue_size=1)
    pub.publish(True)
    stop = rospy.Publisher('channel_y', Int16, queue_size=1)
    stop.publish(135)

def makeCircuit():
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

def callbackLeft(data):
    global leftValue
    leftValue = int(data.data)

def callbackRight(data):
    global rightValue
    rightValue = int(data.data)

def callbackWalk(data):
    if (data.data == 'makeCircuit'):
        makeCircuit()

def listener():
    rospy.Subscriber("left_sensor", Int16, callbackLeft)
    rospy.Subscriber("right_sensor", Int16, callbackRight)
    rospy.Subscriber("walk", String, callbackWalk)
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('test', anonymous=True)
    listener()