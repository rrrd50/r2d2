import time
import roboclaw

print "Starting motor test"

#Windows comport name
#roboclaw.Open("COM3",115200)
#Linux comport name
roboclaw.Open("/dev/ttyACM0",115200)

address = 0x80

# Turn both motors off
roboclaw.ForwardM1(address,0)
roboclaw.ForwardM2(address,0)

print "Motor shut down"
