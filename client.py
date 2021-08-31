#
#   Hello World client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends "Hello" to server, expects "World" back
#

import zmq

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print("Sending request %s …" % request)
    json_data = [{
        "name": "mj",
        "toll_per_cross": 2000,
    }
    ]
    # json_data = str(json_data)
    # socket.send(b"Hello")
    # socket.send(b"json_data")
    socket.send_json(json_data)

    #  Get the reply.

    message = socket.recv()
    print(message)
    print("Received reply %s [ %s ]" % (request, message))