import serial

ser = serial.Serial('COM4', 19200)
while  True:
    bytesToRead = ser.inWaiting()
    ser.read(bytesToRead)
    print(bytesToRead)

