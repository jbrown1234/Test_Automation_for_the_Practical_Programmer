"""
    This module enables the user to make sockets-based connections
    to their LAN-enabled test instrumentation.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
import socket


class InstrumentCommunicationsInterface:
    """
    This class holds the methods and attributes to allow a user to perform
    basic communications with their LAN-enabled test instrumentation.
    Included are the following user-facing methods. For details on their
    specific use, refer to their individual docstrings:
        1. initialize()
        2. write()
        3. read()
        4. query()
        5. close()
    """
    def __init__(self):
        self._sckt = None
        self._timeout_val = 20.0

    def initialize(self,
                   ip_address: str,
                   port_number: int,
                   timeout_value=None):
        """
            Establish the IP4 sockets connection to your instrument.
            Parameters:
                ip_address (str): The IP address of the target instrument.
                port_number (int): The port number to be used with the
                                   sockets connection.
                timeout_value (float=None): This value specifies the
                                amount of time to allow before the
                                expected transaction operation or response
                                will time out and cause an exception.
            Returns:
                None
        """
        self._sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sckt.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        if timeout_value is None:
            self._sckt.settimeout(self._timeout_val)
        else:
            self._sckt.settimeout(timeout_value)
        self._sckt.connect((ip_address, port_number))

    def write(self, command: str):
        """
            Send a command to the instrument.
            Parameters:
                command (str): The instrument command string to be written
                               to the instrument. Note that this method does
                               not define commands for your, you must get
                               these from your instrument's documentation.
            Returns:
                None
        """
        self._sckt.send(f"{command}\n".encode())

    def read(self, receive_size: int):
        """
            Read data back from an instrument.
            Parameters:
                receive_size (int): The receive size is dependent on what
                    you have directed the instrument to return via its
                    output data queue. Most instruments will have a standard
                    format for the particular information your are attempting
                    to retreive. To best understand capabilities and
                    limitations, refer to your instrument's documentation.
            Returns:
                (str) Using this basic read() method implies that the data
                      you are reading back is in ASCII format and, therfore,
                      returned as a string. Any post-processing or data
                      conversion is to be handled by the calling code.
        """
        return self._sckt.recv(receive_size).decode().rstrip()

    def query(self, command: str, receive_size: int):
        """
            Send a command to an instrument and receive a response.
            Parameters:
                command (str): The instrument command string to be written
                               to the instrument. Note that this method does
                               not define commands for your, you must get
                               these from your instrument's documentation.
                receive_size (int): The receive size is dependent on what
                    you have directed the instrument to return via its
                    output data queue. Most instruments will have a standard
                    format for the particular information your are attempting
                    to retreive. To best understand capabilities and
                    limitations, refer to your instrument's documentation.
            Returns:
                (str) Using this basic read() method implies that the data
                      you are reading back is in ASCII format and, therfore,
                      returned as a string. Any post-processing or data
                      conversion is to be handled by the calling code.
        """
        self.write(command)
        return self.read(receive_size)

    def close(self):
        """
            Dispose of the connection to your instrument.
            Parameters:
                None
            Returns:
                None
        """
        self._sckt.close()
