"""add docstring"""
import socket


def instrument_connect(sckt: socket,
                       ip_address: str,
                       port_number: int,
                       timeout_val: int):
    """add docstring"""
    sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sckt.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    sckt.settimeout(timeout_val)
    sckt.connect((ip_address, port_number))
    return sckt


def instrument_disconnect(sckt: socket):
    """add docstring"""
    sckt.close()


def instrument_write(sckt: socket,
                     command: str):
    """add docstring"""
    sckt.send(f"{command}\n".encode())


def instrument_read(sckt: socket,
                    rec_size: int):
    """add docstring"""
    return sckt.recv(rec_size).decode().rstrip()
    

def instrument_query(sckt: socket,
                     command: str,
                     rec_size: int):
    """add docstring"""
    instrument_write(sckt, command)
    return instrument_read(sckt, rec_size)


TIMEOUT_VAL = 20000
IP4_ADDR = "192.168.1.200"
PORT_NUM = 5025
RCV_SZ = 128
INSTR = None

INSTR = instrument_connect(INSTR, IP4_ADDR, PORT_NUM, TIMEOUT_VAL)
instrument_write(INSTR, "*IDN?")
print(instrument_read(INSTR, RCV_SZ))

print(instrument_query(INSTR, "*IDN?", RCV_SZ))
instrument_disconnect(INSTR)
