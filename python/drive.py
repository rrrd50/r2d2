#!/usr/bin/python3

from r2d2_lib.roboclaw3 import RoboClaw
# from roboclaw import RoboClaw
import time
import sys

if len(sys.argv) < 2:
	print('Usage: ./drive.py speed\nspeed = -64 to 63')
	sys.exit(0)

roboclaw1 = RoboClaw('/dev/ttyACM0', 0x80)
# roboclaw1.drive_to_position_raw(motor=1, accel=0, speed=0, deccel=0, position=25, buffer=1)
# while True:
#     print(roboclaw1.read_position(1))
# time.sleep(0.5)
roboclaw1.drive_motor(motor=1, speed=int(sys.argv[1]))
time.sleep(5)
roboclaw1.stop_motor(1)
# print(roboclaw1.read_position(1))
print("finished")
