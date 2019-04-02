"""
    Stub for handling the capacitive touch sensor
"""

import sys, time   # these are just standard modules most python programs require
import Adafruit_MPR121.MPR121 as MPR121

cap = MPR121.MPR121()  # initialize the capacitive sensor
nbr_of_buttons = 3 # 0 = Camera, 1 = Overlay selection, 2 = Twitter

if not cap.begin():
	print("Error initializing MPR121, check wiring.  Terminating!")
	sys.exit(1)

last_touched = cap.touched()
while True:
	current_touched = cap.touched()
	pinbit = 0
	for i in range(0, nbr_of_buttons):
		pin_bit = 1 << i   # this allows us to determine which of the capacitive sensor's pins were touched
		if current_touched & pin_bit and not last_touched & pin_bit:
			sys.stdout.write('Pin {0} touched!\r'.format(i))
			time.sleep(0.5)
			sys.stdout.flush()  # this just allows the messages from this program to stay on one line

		if not current_touched & pin_bit and last_touched & pin_bit:
			sys.stdout.write ('Pin {0} released!\r'.format(i))
			sys.stdout.flush()

	last_touched = current_touched
	time.sleep(0.1)