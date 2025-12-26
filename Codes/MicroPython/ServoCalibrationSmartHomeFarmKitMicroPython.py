# Libraries
from picobricks import MotorDriver
from machine import Pin, I2C

doorClosed = 80
windowClosed = 50

i2c = I2C(0, scl=Pin(5), sda=Pin(4))   # Init I2C using pins
motor = MotorDriver(i2c)

#Close window and door
motor.servo(4, doorClosed)
motor.servo(2, windowClosed)
