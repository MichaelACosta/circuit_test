import csv

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