import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)  

while True:
    if ser.in_waiting > 0: 
        data = ser.readline().decode('utf-8').strip() 
        print("Received:", data)
