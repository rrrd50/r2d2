#!/usr/bin/python3

import time
from roboclaw_python.roboclaw_3 import Roboclaw

#Windows comport name
#rc = Roboclaw("COM11",115200)
#Linux comport name, can be ttyACM1, run $ ls /dev/ttyACM* (to find the correct one)
rc = Roboclaw("/dev/ttyACM0",115200)

rc.Open()
address = 0x80

print('Forward M1')
rc.ForwardM1(address,32)    #1/4 power forward
rc.BackwardM2(address,32)   #1/4 power backward
time.sleep(5)

print('Backward M1')
rc.BackwardM1(address,32)   #1/4 power backward
rc.ForwardM2(address,32)    #1/4 power forward
time.sleep(5)

rc.BackwardM1(address,0)    #Stopped
rc.ForwardM2(address,0)     #Stopped
time.sleep(2)

# ForwardBackward stops at 64, reverse < 64, forward > 64
print('ForwardBackward M1')
m1duty = 16
m2duty = -16
rc.ForwardBackwardM1(address,64+m1duty) #1/4 power forward
rc.ForwardBackwardM2(address,64+m2duty) #1/4 power backward
time.sleep(5)

print('ForwardBackward M1')
m1duty = -16
m2duty = 16
rc.ForwardBackwardM1(address,64+m1duty) #1/4 power backward
rc.ForwardBackwardM2(address,64+m2duty) #1/4 power forward
time.sleep(5)

rc.ForwardBackwardM1(address,64)    #Stopped
rc.ForwardBackwardM2(address,64)    #Stopped
time.sleep(1)
    
rc.BackwardM1(address,0)    #Stopped
rc.ForwardM2(address,0)     #Stopped
time.sleep(1)

print('Test Complete')
