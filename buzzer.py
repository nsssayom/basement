from threading import Thread
import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
from time import sleep

from config import buzzer_pin


class Buzzer:

    # Buzzer parameters
    beep_count = 0
    high_time = 0
    low_time = 0

    def beep(self, duty_cycle: float, single_beep_length: float,
             number_of_beep: int = 1, background=False):
        '''
        Create a multi-threaded beep

        :param float duty_cycle: Ratio of High and Low state length of the
        buzzer; if n, 0<n<=1
        :param float single_beep_length: Length of a single beep in second
        :param int number_of_beep: Number of beep to be executed.
        0 for infinite loop. For 0, background must be True.
        :param bool background: If True, main thread would not wait for beep
        to finish
        :return True if success, False if failed
        :raises ValueError: if duty cycle is greater than 1 and less than 0
        '''
        if (duty_cycle > 1 or duty_cycle < 0 or number_of_beep < 0):
            raise ValueError

        if (number_of_beep == 0 and not background):
            raise ValueError

        self.beep_count = number_of_beep
        self.high_time = single_beep_length * duty_cycle
        self.low_time = single_beep_length * (1 - duty_cycle)

        buzzer_thread = Thread(target=self._beep, daemon=True)

        buzzer_thread.start()
        if not background:
            buzzer_thread.join()

    def _beep(self):
        if self.beep_count > 0:
            for i in range(0, self.beep_count):
                GPIO.output(buzzer_pin, GPIO.LOW)    # Turn on the buzzer
                sleep(self.high_time)
                GPIO.output(buzzer_pin, GPIO.HIGH)   # Turn off the buzzer
                sleep(self.low_time)

        elif (self.beep_count == 0):
            while(True):
                GPIO.output(buzzer_pin, GPIO.LOW)    # Turn on the buzzer
                sleep(self.high_time)
                GPIO.output(buzzer_pin, GPIO.HIGH)   # Turn off the buzzer
                sleep(self.low_time)


buzzer = Buzzer()
