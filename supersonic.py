#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# ultrasonic_1.py
# Measure distance using an ultrasonic module
#
# Author : Matt Hawkins
# Date   : 09/01/2013

# Import required Python libraries
import time
import RPi.GPIO as GPIO
import os
import sys
import urllib

print "Ultrasonic Measurement"

while True:
    GPIO.setwarnings(False)
    # Use BCM GPIO references
    # instead of physical pin numbers
    GPIO.setmode(GPIO.BCM)

    # Define GPIO to use on Pi
    GPIO_TRIGGER = 23
    GPIO_ECHO = 24

    # Set pins as output and input
    GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
    GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo
    GPIO.setup(18,GPIO.IN)             # Light Sensor
    GPIO.setup(11,GPIO.OUT)           # Led Light

    # Set trigger to False (Low)
    GPIO.output(GPIO_TRIGGER, False)

    # Allow module to settle
    time.sleep(0.5)

    # Send 10us pulse to trigger
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()
    while GPIO.input(GPIO_ECHO)==0:
      start = time.time()

    while GPIO.input(GPIO_ECHO)==1:
      stop = time.time()

    # Calculate pulse length
    elapsed = stop-start

    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound (cm/s)
    distance = elapsed * 34000

    # That was the distance there and back so halve the value
    distance = distance / 2

    sys.stdout.write("\rDistance : %.1f" % distance)
    sys.stdout.flush()

    if distance<=50:
        if GPIO.input(18) == False:
            sys.stdout.write("\rLED On")
            sys.stdout.flush()
            GPIO.cleanup()
            GPIO.setmode(GPIO.BOARD)
            GPIO.setup(11,GPIO.OUT)
            GPIO.output(11,True)
            time.sleep(5)
            urllib.urlretrieve("http://10.32.21.164:8080/?action=snapshot", filename="/var/www/output.jpg")
            GPIO.output(11,False)
            sys.stdout.write("\rLED Off")
            sys.stdout.flush()
        else:
            urllib.urlretrieve("http://10.32.21.164:8080/?action=snapshot", filename="/var/www/output.jpg")
        os.system('/home/pi/Pushbullet.sh "Human Detected. Watch your monitor at http://www.interactivemonitor.com"')

    # Reset GPIO settings
    GPIO.cleanup()
