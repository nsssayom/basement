import sys
from threading import Thread
from mfrc522 import SimpleMFRC522

from library.buzzer import buzzer           # noqa: F401
from config import verified_card_id
from library.led import led                 # noqa: F401


class Rfid_reader:

    id_reader = SimpleMFRC522()
    reader_thread = None

    def start_scan(self, on_success, on_failed, on_error):
        reader_thread = Thread(target=self.read_card,
                               args=(on_success, on_failed, on_error,),
                               daemon=True)
        try:
            reader_thread.start()
            reader_thread.join()
        except (KeyboardInterrupt, SystemExit):
            on_error("Received keyboard interrupt, quitting reader threads.")
        except Exception as e:
            on_error("Undetected Exception: " + str(e))

    def read_card(self, on_success, on_failed, on_error):
        while(True):
            led.on('Blue', 1, 1, 0, True)    # Scanning LED
            try:
                id, text = self.id_reader.read()
                buzzer.beep(.3, 0.05, 3)        # Scanning tone
                led.on('Yellow', .8, .05, 3, True)    # Scanning LED
                if id == verified_card_id:
                    print("Access Authorized. ID: ", id)
                    # Authorization successful tone
                    buzzer.beep(0.3, 0.2, 2)
                    led.on('Green', 1, 1, 0, True)    # Scanning LED
                    on_success()
                    # break
                else:
                    print("Access Denied. ID: ", id)
                    buzzer.beep(1, 0.4, 1)    # Authorization failed tone
                    led.on('Red', 1, 1, 0, True)    # Scanning LED
                    on_failed()

            except Exception as e:
                on_error("Undetected Exception: " + str(e))

    def stop(self):
        sys.exit()


rfid_reader = Rfid_reader()
