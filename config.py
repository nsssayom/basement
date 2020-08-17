import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library

# GPIO configurations

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Buzzer PIN Configuration
buzzer_pin = 8      # Set Buzzer Pin
GPIO.setup(buzzer_pin, GPIO.OUT, initial=GPIO.HIGH)
