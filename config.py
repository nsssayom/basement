import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library

# GPIO configurations

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Buzzer pin Configuration
buzzer_pin = 8      # Set Buzzer Pin
GPIO.setup(buzzer_pin, GPIO.OUT, initial=GPIO.HIGH)

# Indicator LED pin configuration
red_pin = 38
green_pin = 36
blue_pin = 40

GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(blue_pin, GPIO.OUT)

led_frequency = 100     # Setting PWM frequency to 100Hz

red_led_pin = GPIO.PWM(red_pin, led_frequency)
green_led_pin = GPIO.PWM(green_pin, led_frequency)
blue_led_pin = GPIO.PWM(blue_pin, led_frequency)

# Verified Card ID
verified_card_id = 927274965454
