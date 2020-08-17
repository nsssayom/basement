#!/usr/bin/env python

from mfrc522 import SimpleMFRC522
import sys
import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library

from buzzer import Buzzer


reader = SimpleMFRC522()
buzzer = Buzzer()


while(True):
    try:
        id, text = reader.read()
        print("id: ", id)
        print(text)
        buzzer.beep(1, 0.2, 1)

    except KeyboardInterrupt:
        print("Ending program")
        GPIO.output(8, GPIO.HIGH)
        sys.exit(0)
