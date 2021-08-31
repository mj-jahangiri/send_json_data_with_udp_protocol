##sender
import socket
import zmq
import pickle

json_data = [{
    "name": "mj",
    "toll_per_cross": 2000,
}
]


###mitoni to ye halghe bezarish
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# sock.sendto(b'SUP', ('127.0.0.1', 5002))  ##avalin parametr on chizi hast k mikhahim befrestim va dovomin
sock.sendto(pickle.dumps(json_data), ('127.0.0.1', 5002))
# sock.send_json(json_data, ('127.0.0.1', 5002))
##argoman addres jae ast k mikhahim befrestim
##addres on yeki socke ast k mikhahim behesh data befrestim

###mitoni chandin socket besazi va data ha ro rosh befreste