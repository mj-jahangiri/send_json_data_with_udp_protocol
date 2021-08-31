import socket
import pickle

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  ###SOCK_DGRAM baray udp ast
address = ('127.0.0.1', 5002)  ###avalish ip local host ast ip sistem ma ast va dovomi port
## port hastesh az port hae k estefade nemishe estefade kon bein 500 ta 50000
sock.bind(address)  ### inja socket ro bind kardim ba addresemon
while True:
    # data, addr = sock.recvfrom(1024)  ### 1024 maximom size data ast k mitonim daryaft konim one kilobyte 1 kilo byte
    ##rezive bessorate yek list ast k avalish data gerefte shode ast va dovomish addresi k ono ferestade

    data = pickle.loads(sock.recvfrom(1024)[0])
    print(type(data))
    # dict_json_data=pickle.loads(data)
    print(data)
    # print(addr)
