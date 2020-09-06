import sys
from library.rfid_reader import rfid_reader
from time import sleep
import socketio
from config import socket_io_server, socket_io_server_namespace


# callback functions for rfid reader

def on_success():
    print("Success")
    sleep(2)
    sio.emit('on_begin_scan', "Starting RFID Scan",
             namespace=socket_io_server_namespace)
    print("Reinitiating Scan")
    rfid_reader.start_scan(on_success, on_failed, on_error)


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
sio = socketio.Client()
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


rfid_reader.start_scan(on_success, on_failed, on_error)
