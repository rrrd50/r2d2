#!/usr/bin/python3

from math import sin, cos, pi
import time
import roboclaw
# from roboclaw import R2D2


class R2D2:
    def __init__(self):
        self.x_coord = 0
        self.y_coord = 0
        self.angle = 0
        self.speed = 64
        self.stime = 2

    def forward_1(self):
        d = 1  # future distance variable
        a = self.angle / 360 * 2 * pi
        self.x_coord += d * sin(a)
        self.y_coord += d * cos(a)
        # perform movement
        print("Moving Forward")
        roboclaw.ForwardM1(address, self.speed)
        roboclaw.ForwardM2(address, self.speed)
        time.sleep(self.stime)
        self.stop()  # Turn both motors off

    def reverse_1(self):
        d = 1  # future distance variable
        a = self.angle / 360 * 2 * pi
        self.x_coord -= d * sin(a)
        self.y_coord -= d * cos(a)
        # perform movement
        print("Moving Backward")
        roboclaw.BackwardM1(address, self.speed)
        roboclaw.BackwardM1(address, self.speed)
        time.sleep(self.stime)
        self.stop()  # Turn both motors off

    def left_90(self):
        self.angle -= 90
        if self.angle < 0:
            self.angle += 360
        elif self.angle >= 360:
            self.angle -= 360
        # perform movement
        print("Turning Left")
        roboclaw.ForwardM1(address, self.speed)
        roboclaw.BackwardM1(address, self.speed)
        time.sleep(self.stime)
        self.stop()  # Turn both motors off

    def right_90(self):
        self.angle += 90
        if self.angle < 0:
            self.angle += 360
        elif self.angle >= 360:
            self.angle -= 360
        # perform movement
        print("Turning Right")
        roboclaw.BackwardM1(address, self.speed)
        roboclaw.ForwardM1(address, self.speed)
        time.sleep(self.stime)
        self.stop()  # Turn both motors off

    @staticmethod
    def stop():
        # Turn both motors off
        roboclaw.ForwardM1(address, 0)
        roboclaw.ForwardM2(address, 0)
        print("Stopping\n")


if __name__ == '__main__':
    from argparse import ArgumentParser

# set up roboclaw interface
roboclaw.Open("/dev/ttyACM0", 115200)
# address = bytes([0x80])
address = 0x80

# Instantiate the R2D2 class
r2d2 = R2D2()

# Test function and interface
print("Testing Motion Functions\n")
r2d2.forward_1()
time.sleep(5)
r2d2.left_90()
time.sleep(5)
r2d2.right_90()
time.sleep(5)
r2d2.reverse_1()
time.sleep(5)
print("Test Complete")
