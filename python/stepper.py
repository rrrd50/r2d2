#!/usr/bin/python3

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  # set the pin numbering to the Broadcom chip numbers
GPIO.setup(21, GPIO.OUT)  # set BCM pin 21 (connector pin 40) to an output, White
GPIO.setup(20, GPIO.OUT)  # set BCM pin 20 (connector pin 38) to an output, Blue
GPIO.setup(16, GPIO.OUT)  # set BCM pin 16 (connector pin 36) to an output, Green
GPIO.setup(12, GPIO.OUT)  # set BCM pin 12 (connector pin 32) to an output, Brown

# Ground is on pin 34, Black

# stepper motor lingo
# A = pin 21, White
# B = pin 20, Blue
# AN = pin 16, Green
# BM = pin 12, Brown

class Stepper:
    def __init__(self):
        self.states = [1, 1, 0, 0]
        self.outputs = [21, 20, 16, 12]
        self.head_angle = 0  # 0 is straight ahead, 90 is to the right, -90 is to the left

    @staticmethod
    def shift_left(l, n):
        return l[n:] + l[:n]

    @staticmethod
    def shift_right(l, n):
        return l[-n:] + l[:-n]

    def turn_motor(self, direction="cw", speed=1.0, angle=1):  # (cw/ccw, rev/sec, seconds)
        # global states, outputs
        delay = 0.01 / speed
        steps = round(angle / 3.6)
        i = 0
        while i < steps:
            for x, output in enumerate(self.outputs):
                GPIO.output(output, self.states[x])
            if direction == 'cw':
                self.states = self.shift_left(self.states, 1)
            elif direction == 'ccw':
                self.states = self.shift_right(self.states, 1)
            i += 1
            sleep(delay)
        if direction == "cw":
            self.head_angle = self.head_angle + steps * 3.6
        elif direction =="ccw":
            self.head_angle = self.head_angle - steps * 3.6

    def turn_motor_save(self, direction="cw", speed=1, duration=1):  # (cw/ccw, rev/sec, seconds)
        # global states, outputs
        delay = 0.01 / speed
        steps = duration / delay
        i = 0
        while i < steps:
            for x, output in enumerate(self.outputs):
                GPIO.output(output, self.states[x])
            if direction == 'cw':
                self.states = self.shift_left(self.states, 1)
            elif direction == 'ccw':
                self.states = self.shift_right(self.states, 1)
            i += 1
            sleep(delay)
        if direction == "cw":
            self.head_angle = self.head_angle + steps * 3.6
        elif direction =="ccw":
            self.head_angle = self.head_angle - steps * 3.6

if __name__ == '__main__':
    step = Stepper()
    step.turn_motor(direction="cw", speed=0.5, angle=180)  # (cw/ccw, rev/sec, angle)
    sleep(0.5)
    step.turn_motor(direction="ccw", speed=0.5, angle=180)  # (cw/ccw, rev/sec, angle)

    GPIO.cleanup()
