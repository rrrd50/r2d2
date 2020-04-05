#!/usr/bin/python3

from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  # set the pin numbering to the Broadcom chip numbers
GPIO.setup(21, GPIO.OUT)  # set BCM pin 21 (connector pin 40 to an output)
GPIO.setup(20, GPIO.OUT)  # set BCM pin 20 (connector pin 38 to an output)
GPIO.setup(16, GPIO.OUT)  # set BCM pin 16 (connector pin 36 to an output)
GPIO.setup(12, GPIO.OUT)  # set BCM pin 12 (connector pin 32 to an output)
# Ground is on pin 34

# make stepper motor lingo variables for pin numbers
# A = 21
# B = 20
# AN = 16
# BM = 12

def shift_left(l, n):
	return l[n:] + l[:n]


def shift_right(l, n):
	return l[-n:] + l[:-n]


states = [1, 1, 0, 0]
outputs = [21, 20, 16, 12]

def turn_motor(direction, speed, duration):  # (cw/ccw, rev/sec, seconds)
	global states, outputs
	delay = 0.01 / speed
	steps = duration / delay
	i = 0
	while i < steps:
		for x, output in enumerate(outputs):
			GPIO.output(output, states[x])
		if direction == 'cw':
			states = shift_left(states, 1)
		elif direction == 'ccw':
			states = shift_right(states, 1)
		i += 1
		sleep(delay)

turn_motor(direction="cw", speed=2, duration=2)  # (cw/ccw, rev/sec, seconds)
turn_motor(direction="ccw", speed=0.5, duration=2)  # (cw/ccw, rev/sec, seconds)

GPIO.cleanup()

