#Libraries
import RPi.GPIO as GPIO
import time
from gpiozero import PWMLED

#GPIO Mode
GPIO.setmode(GPIO.BCM)

#GPIO Pins
TRIGGER = 23
ECHO = 24
LED = PWMLED(17)

#GPIO direction
GPIO.setup(TRIGGER, GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def distance():

    GPIO.output(TRIGGER, False)
    time.sleep(1)

    GPIO.output(TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(TRIGGER, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    
    duration = pulse_end - pulse_start
    distance = duration * 17150
    distance = round(distance, 2)
    return distance

MAX_DISTANCE = 30 #Longest distance in the room

try:
    while True:
        currentDistance = distance()
        if currentDistance > 30:
            LED.value = 0
        if currentDistance <= 30:
            proximity = 1-(currentDistance / MAX_DISTANCE)
            LED.value = proximity
        time.sleep(.01)
except KeyboardInterrupt:
    GPIO.cleanup()