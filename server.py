import zmq
import time

#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#


context=zmq.Context()
socket=context.socket(zmq.REP)
socket.bind('tcp://*:5555')



while True:
    #  Wait for next request from client
    message = socket.recv_json()
    # message = socket.recv()
    print("Received request: %s" % message)
    name=message[0]['name']
    print(type(message))

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send(b"World")
