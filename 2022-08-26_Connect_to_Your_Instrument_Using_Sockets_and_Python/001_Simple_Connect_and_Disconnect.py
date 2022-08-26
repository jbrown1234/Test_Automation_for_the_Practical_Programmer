import socket


TIMEOUT_VAL = 20000

# See for documentation: https://docs.python.org/3/library/socket.html 
instr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # Establish a TCP/IP socket object
                                                            # AF_INET is used for IPv4 type connections
                                                            # SOCK_STREAM is one option of four that
                                                            #  define the socket type
instr.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1) # optional - need to find out what this
                                                            #  does and share it in follow up video
                                                            # For the TCP protocol, disabling Nagle's
                                                            #  algorithm to get better user experience
                                                            #  and performance out of your network
                                                            # see https://www.extrahop.com/company/blog/2016/tcp-nodelay-nagle-quickack-best-practices/
instr.settimeout(TIMEOUT_VAL)        # time to wait for a response before a timeout exception is thrown

IP4_ADDR = "192.168.1.200" # string
PORT_NUM = 5025  # integer
instr.connect((IP4_ADDR, PORT_NUM))  # input must be a tuple


# Send an instrument a simple or basic command
instr.send("*RST\n".encode())  # should see the instrument interface update and indicate remote operation

instr.send("*IDN?\n".encode())  # 
RCV_SZ = 128
RCV_DATA = instr.recv(RCV_SZ).decode().rstrip()
print(RCV_DATA)

instr.close()
