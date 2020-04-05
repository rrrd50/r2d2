# ***Before using this example the motor/controller combination must be -
# ***tuned and the settings saved to the Roboclaw using IonMotion.
# ***The Min and Max Positions must be at least 0 and 50000

import time
import roboclaw


def displayspeed():
    enc1 = roboclaw.ReadEncM1(address)
    enc2 = roboclaw.ReadEncM2(address)
    speed1 = roboclaw.ReadSpeedM1(address)
    speed2 = roboclaw.ReadSpeedM2(address)

    print("Encoder1:"),
    if (enc1[0] == 1):
        print enc1[1],
        print format(enc1[2], '02x'),
    else:
        print "failed",
    print "Encoder2:",
    if (enc2[0] == 1):
        print enc2[1],
        print format(enc2[2], '02x'),
    else:
        print "failed ",
    print "Speed1:",
    if (speed1[0]):
        print speed1[1],
    else:
        print "failed",
    print("Speed2:"),
    if (speed2[0]):
        print speed2[1]
    else:
        print "failed "


# Windows comport name
# roboclaw.Open("COM3",38400)
# Linux comport name
roboclaw.Open("/dev/ttyACM0", 115200)

address = 0x80
roboclaw.ResetEncoders(address)  # reset the encoders to 0

x = 0
print "Starting"
roboclaw.ForwardM1(address, 64)
roboclaw.ForwardM2(address, 64)
for i in range(0, 10):
    displayspeed()
    time.sleep(0.5)

# Turn both motors off
roboclaw.ForwardM1(address, 0)
roboclaw.ForwardM2(address, 0)

'''
x = 0
while(x < 10):
	print "Pos 50000"
	roboclaw.SpeedAccelDeccelPositionM1(address,32000,12000,32000,50000,0)
	for i in range(0,8):
		displayspeed()
		time.sleep(0.1)

	#time.sleep(2)
	
	print "Pos 0"
	roboclaw.SpeedAccelDeccelPositionM2(address,32000,12000,32000,0,0)
	for i in range(0,8):
		displayspeed()
		time.sleep(0.1)
  
	#time.sleep(2)
	x += 1

# Turn both motors off
roboclaw.ForwardM1(address,0)
roboclaw.ForwardM2(address,0)
'''
