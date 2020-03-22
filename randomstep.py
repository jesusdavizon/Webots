from controller import Robot
import random

TIME_STEP = 1000 #miliseconds
robot = Robot()

left=[1,1,1,1,1,1,1,1,1]
right=[1,1,1,1,1,1,1,1,1]
power=1

ds = []
dsNames = ['ds_right', 'ds_left']
for i in range(2):
    ds.append(robot.getDistanceSensor(dsNames[i]))
    ds[i].enable(TIME_STEP)
    
wheels = []
wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
for i in range(4):
    wheels.append(robot.getMotor(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)
    
avoidObstacleCounter = 0
step=0

avoidObstacleCounter = 0
while robot.step(TIME_STEP)!=-1:

    leftSpeed=random.randrange(0,5)*power
    rightSpeed=random.randrange(0,5)*power

    if avoidObstacleCounter > 0:
        avoidObstacleCounter -= 10
        leftSpeed = 1
        rightSpeed = -1
    else:  # read sensors
        for i in range(2):
            if ds[i].getValue() < 950.0:
                avoidObstacleCounter = 35
                
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)

    if step<9:
        step=step+1
    if step==9:
        step=0
        
    print (step)
