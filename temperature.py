import time
import serial


board = serial.Serial("COM4",115200,timeout=1)
time.sleep(2)

def temp_check():
    temp = board.readline().decode("utf-8")
    return temp
