from controller import Robot

TIME_STEP = 1000
robot = Robot()

left=[1,1,1,1,1,1,1,1,1,1,1,1,-1,-1,-1,-1,1,1,1,1]
right=[1,1,1,1,-1,-1,-1,-1,1,1,1,1,1,1,1,1,1,1,1,1]
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
i=0

while robot.step(TIME_STEP)!=-1:

    leftSpeed=left[i]*power
    rightSpeed=right[i]*power       
                
    wheels[0].setVelocity(leftSpeed)
    wheels[1].setVelocity(rightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)

    if i<19:
        i=i+1
    if i==19:
        i=0
        
    print (i)
    