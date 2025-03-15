import serial
import struct

DLE = 0x10
SOM = 0x01
EOM = 0x04

if __name__ == "__main__":
    ser = serial.Serial("COM6", 115200, timeout=1)
    data = struct.pack('<BBBBBBB', DLE, SOM, 0x01, 0x02, 0x03, DLE, EOM)
    data2 = struct.pack('<BBBBBBB', DLE, SOM, 0x55, 0x50, 0x05, DLE, EOM)
    data3 = struct.pack('<BBBBBBB', DLE, SOM, 0x01, 0x50, 0x03, DLE, EOM) #CRC should fail
    data4 = struct.pack('<BBBBBBB', DLE, SOM, 0x99, 0x98, 0x01, DLE, EOM)
    data5 = struct.pack('<BBBBBBB', DLE, SOM, 0x55, 0x50, 0x05, DLE, EOM)
    ser.write(data)
    ser.write(data2)
    ser.write(data3)
    ser.write(data4)
    ser.write(data5)
    print("Data Sent")
