#!/usr/bin/python3
""" Serves a web page to control the drive motors """

from flask import Flask, jsonify, request, render_template
from math import sin, cos, pi
import time
from roboclaw_python.roboclaw_3 import Roboclaw
from stepper import Stepper, GPIO
# from stepper import *
from signal import signal, SIGINT
from sys import exit

#Linux comport name, can be ttyACM1, run $ ls /dev/ttyACM* (to find the correct one)
rc = Roboclaw("/dev/ttyACM0",115200)

rc.Open()
address = 0x80

step = Stepper()

# handler to gracefully exit on cntl-c
def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    print("GPIO", GPIO)
    GPIO.cleanup()
    exit(0)



class R2D2:
    def __init__(self):
        self.x_coord = 0
        self.y_coord = 0
        self.angle = 0
        self.speed = 32
        self.m_time = 2

    def forward_1(self):
        d = 1  # future distance variable
        a = self.angle / 360 * 2 * pi  # convert degrees to radians
        self.x_coord += d * sin(a)  # calculate new x coordinate
        self.y_coord += d * cos(a)  # calculate new y coordinate
        # perform movement
        rc.ForwardM1(address,self.speed)
        rc.ForwardM2(address,self.speed)
        time.sleep(self.m_time)
        self.stop()  # Turn both motors off

    def reverse_1(self):
        d = 1  # future distance variable
        a = self.angle / 360 * 2 * pi
        self.x_coord -= d * sin(a)
        self.y_coord -= d * cos(a)
        # perform movement
        rc.BackwardM1(address,self.speed)
        rc.BackwardM2(address,self.speed)
        time.sleep(self.m_time)
        self.stop()  # Turn both motors off

    def left_90(self):
        self.angle -= 90
        if self.angle < 0:
            self.angle += 360
        elif self.angle >= 360:
            self.angle -= 360
        # perform movement
        rc.ForwardM1(address,self.speed)
        rc.BackwardM2(address,self.speed)
        #rc.drive_motor(motor=1, speed=int(self.speed))
        #rc.drive_motor(motor=2, speed=-int(self.speed))
        time.sleep(self.m_time)
        self.stop()  # Turn both motors off

    def right_90(self):
        self.angle += 90
        if self.angle < 0:
            self.angle += 360
        elif self.angle >= 360:
            self.angle -= 360  # perform movement
        rc.BackwardM1(address,self.speed)
        rc.ForwardM2(address,self.speed)
        #rc.drive_motor(motor=1, speed=-int(self.speed))
        #rc.drive_motor(motor=2, speed=int(self.speed))
        time.sleep(self.m_time)
        self.stop()  # Turn both motors off

    @staticmethod
    def stop():
        # Turn both motors off
        rc.ForwardM1(address,0)
        rc.ForwardM2(address,0)
        #rc.drive_motor(motor=1, speed=0)
        #rc.drive_motor(motor=2, speed=0)
        print("Turning off")

    @staticmethod
    def turn_head(direction, speed=0.25, angle=0.5):
        step.turn_motor(direction=direction, speed=speed, angle=angle)  # (cw/ccw, rev/sec, angle)


# Instantiate the Flask Node
app = Flask(__name__)

# Instantiate the R2D2 class
r2d2 = R2D2()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/move', methods=['POST'])
def move():
    values = request.get_json()
    print('In route /move, Values:', values)
    # Set the variables sent from the web page form
    r2d2.speed = int(values["motion_speed"])
    r2d2.m_time = float(values["motion_time"])

    if values["direction"] == "forward":
        r2d2.forward_1()
    elif values["direction"] == "reverse":
        r2d2.reverse_1()
    elif values["direction"] == "left":
        r2d2.left_90()
    elif values["direction"] == "right":
        r2d2.right_90()
    elif values["direction"] == "stop":
        r2d2.stop()
    elif values["direction"] == "head_left":
        r2d2.turn_head(direction='cw', speed=float(values["head_speed"]), angle=int(values["head_degrees"]))
    elif values["direction"] == "head_right":
        r2d2.turn_head(direction='ccw', speed=float(values["head_speed"]), angle=int(values["head_degrees"]))

    response = {'x': str(r2d2.x_coord), 'y': str(r2d2.y_coord), 'angle': str(r2d2.angle)}

    return jsonify(response), 201


if __name__ == '__main__':
    # add cntl-c handler
    # Tell Python to run the handler() function when SIGINT is recieved
    signal(SIGINT, handler)

    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=4000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='192.168.0.130', port=port)
