import sys
from read import rfid_reader


def on_success():
    print("Success")
    rfid_reader.start_scan(on_success, on_failed, on_error)


def on_failed():
    print("Failed")


def on_error(error_msg=None):
    if error_msg:
        print(error_msg)
    sys.exit(0)


rfid_reader.start_scan(on_success, on_failed, on_error)
