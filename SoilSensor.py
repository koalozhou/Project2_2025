# !/usr/bin/env python3

# Use Comments
# Program Title: SoilSensor.py
# Program Description: The script monitors soil moisture levels using a moisture sensor on a RaspberryPi
# Name: Renjie Zhou
# Student ID: 202283890006  W20110010
# Course & Year: Project Semester 3 & Grade 3
# Date: 16/4/2025

import RPi.GPIO as GPIO
import time

# GPIO SETUP
channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        print("The soil is moist and does not need watering!")
    else:
        print("The soil is dry, please water in time!")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

#infinite loop
while True:
    time.sleep(0)
