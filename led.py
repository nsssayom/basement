from time import sleep
import RPi.GPIO as GPIO
from threading import Thread

from config import red_led_pin, green_led_pin, blue_led_pin


class LED:

    # Color parameters
    red_duty_cycle = 0
    green_duty_cycle = 0
    blue_duty_cycle = 0

    # LED parameters
    flash_count = 0
    high_time = 0
    low_time = 0

    colors = {
        "Red":      (100, 0, 0),
        "Green":    (0, 100, 0),
        "Blue":     (0, 0, 100),
        "Cyan":     (0, 100, 100),
        "Fuchsia":  (100, 0, 100),
        "Yellow":   (100, 100, 0),
        "White":    (100, 100, 100)
    }

    def on(self, color, duty_cycle: float, single_flash_length: float,
           number_of_flash: int = 1, background=False):
        '''
        number_of_flash = 0, for continuous flashing
        '''
        if (duty_cycle > 1 or duty_cycle < 0 or number_of_flash < 0):
            raise ValueError

        if (number_of_flash == 0 and not background):
            raise ValueError

        if (color not in self.colors):
            raise ValueError

        self.flash_count = number_of_flash
        self.high_time = single_flash_length * duty_cycle
        self.low_time = single_flash_length * (1 - duty_cycle)

        self.red_duty_cycle = self.colors[color][0]
        self.green_duty_cycle = self.colors[color][1]
        self.blue_duty_cycle = self.colors[color][2]

        led_thread = Thread(target=self._flash, daemon=True)

        led_thread.start()
        if not background:
            led_thread.join()

    def _flash(self):
        if self.flash_count > 0:
            for i in range(0, self.flash_count):
                red_led_pin.start(self.red_duty_cycle)
                green_led_pin.start(self.green_duty_cycle)
                blue_led_pin.start(self.blue_duty_cycle)
                sleep(self.high_time)
                red_led_pin.stop()
                green_led_pin.stop()
                blue_led_pin.stop()
                sleep(self.low_time)

        elif self.flash_count == 0:
            while(True):
                red_led_pin.start(self.red_duty_cycle)
                green_led_pin.start(self.green_duty_cycle)
                blue_led_pin.start(self.blue_duty_cycle)
                sleep(self.high_time)
                red_led_pin.stop()
                green_led_pin.stop()
                blue_led_pin.stop()
                sleep(self.low_time)

led = LED()

led.on('Fuchsia', 0.5, .5, 5)
led.on('Green', 0.5, .5, 5)
led.on('Blue', 0.5, .5, 5)