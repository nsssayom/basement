import sys
from library.rfid_reader import rfid_reader
from time import sleep
import socketio
from config import socket_io_server, socket_io_server_namespace
from library.buzzer import buzzer


# callback functions for rfid reader
def on_success():
    print("Successful RFID Read. Waiting for Reset Signal.")


def on_failed():
    print("Failed")
    sleep(2)
    sio.emit('on_begin_scan', "Starting RFID Scan",
             namespace=socket_io_server_namespace)
    print("Reinitiating Scan")


def on_error(error_msg=None):
    if error_msg:
        print(error_msg)
    sys.exit(0)


# initiate socket.io connection
# sio = socketio.Client()

sio = socketio.Client(ssl_verify=False)

try:
    sio.connect(socket_io_server, namespaces=[socket_io_server_namespace])
except socketio.exceptions.ConnectionError:
    print("Socket Server unavailable or unreachable at {}"
          .format(socket_io_server))
    sys.exit(0)
except Exception as ex:
    print(ex)
    sys.exit(0)


@sio.on('connect', namespace=socket_io_server_namespace)
def on_io_connect():
    print("Connected with Socket Server")

    welcome_msg = "Hello, Socket Server!"
    print("Msg to Socket Server: " + welcome_msg)
    sio.emit('on_connected', welcome_msg, namespace=socket_io_server_namespace)


@sio.event(namespace=socket_io_server_namespace)
def on_connected(msg):
    print("Msg from Socket Server: " + msg)


@sio.event(namespace=socket_io_server_namespace)
def on_product_found(msg):
    print(msg)
    buzzer.beep(0.3, 0.2, 2)


@sio.event(namespace=socket_io_server_namespace)
def on_product_not_found(msg):
    print(msg)
    buzzer.beep(1, 0.4, 1)


@sio.event(namespace=socket_io_server_namespace)
def on_end_session(msg):
    print("Reinitiating Scan")
    sio.emit('on_begin_scan', "Starting RFID Scan",
             namespace=socket_io_server_namespace)
    buzzer.beep(0.7, .1, 3)
    rfid_reader.start_scan(on_success, on_failed, on_error)


@sio.event(namespace=socket_io_server_namespace)
def on_refresh(msg):
    buzzer.beep(.2, 0.05, 4)


rfid_reader.start_scan(on_success, on_failed, on_error)
