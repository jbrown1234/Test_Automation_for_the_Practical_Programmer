"""add docstring"""
import instrcomms as instr

mysmu = instr.InstrumentCommunicationsInterface()

mysmu.initialize("192.168.1.2", 5025, 5.0)

mysmu.write("*RST")

print(mysmu.query("*IDN?", 128))

mysmu.close()
