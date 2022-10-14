from picar import front_wheels, back_wheels
from picar.SunFounder_PCA9685 import Servo
import picar
from time import sleep
import cv2
import numpy as np
import picar
import os

class basic_car():
    __INITIAL_SPEED = 0    
    bw = back_wheels.Back_Wheels()
    fw = front_wheels.Front_Wheels()

    pan_servo = Servo.Servo(1)
    tilt_servo = Servo.Servo(2)
    fw_angle = 0

    DELAY = 0.01

    def __init__(self):
        picar.setup()
        rear_wheels_enable  = True
        front_wheels_enable = True
        FW_ANGLE_MAX    = 90+30
        FW_ANGLE_MIN    = 90-30

        self.bw.speed = 0
        self.fw.offset = 0
        self.fw_angle = 72               #initial front wheel direction
                
        pan_tilt_enable     = True
        MIDDLE_TOLERANT = 5
        PAN_ANGLE_MAX   = 170
        PAN_ANGLE_MIN   = 10
        TILT_ANGLE_MAX  = 150
        TILT_ANGLE_MIN  = 70

        self.pan_servo.offset = 10
        self.tilt_servo.offset = 0
        pan_angle = 90              # initial angle for pan
        tilt_angle = 90             # initial angle for tilt

        self.pan_servo.write(pan_angle)
        self.tilt_servo.write(tilt_angle)

    def testDrive(self, speed=__INITIAL_SPEED):
        fw_angle = self.fw_angle

        self.fw.turn(fw_angle)
        self.bw.speed = speed
        
        self.bw.backward()
        sleep(100*self.DELAY)

        self.bw.forward()
        sleep(100*self.DELAY)

    def turn(self, fw_angle):
        self.fw.turn(fw_angle)        

    def driveForward(self, speed):
        self.bw.speed = speed
        self.bw.forward()

    def driveBackward(self, speed):
        self.bw.speed = speed
        self.bw.backward()
        
    def stop(self):
        self.bw.stop()
                    
def main():  
    car = basic_car()
    car.testDrive(40)

    car.turn(90)
    car.driveForward(40)
    sleep(100*car.DELAY)

    car.turn(120)
    car.driveBackward(60)
    sleep(100*car.DELAY)
    
    car.stop()
    
def destroy():
    self.bw.stop()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        destroy()
