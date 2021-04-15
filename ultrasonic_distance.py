#Libraries
import RPi.GPIO as GPIO
import time
from gpiozero import PWMLED #This is used to control the LED brightness

#GPIO Mode
GPIO.setmode(GPIO.BCM)

#GPIO Pins
TRIGGER = 23
ECHO = 24
LED = PWMLED(17)

#GPIO direction for proximity sensor
GPIO.setup(TRIGGER, GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def distance():

    GPIO.output(TRIGGER, False) #This stops the sensor from firing too often
    time.sleep(1)

    GPIO.output(TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(TRIGGER, False)
    
    #This measures the time it takes to receive the information
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    
    duration = pulse_end - pulse_start
    distance = duration * 17150
    distance = round(distance, 2

    return distance

MAX_DISTANCE = 30 #This is how far you want the sensor data to be monitored by the LED
                  #I chose 30cm so that I could easily demo my project in the video

try:
    while True:
        currentDistance = distance()
        if currentDistance > MAX_DISTANCE:
            LED.value = 0
        if currentDistance <= MAX_DISTANCE:
            proximity = 1-(currentDistance / MAX_DISTANCE) #The PWM value needs to be reversed so the LED gets brighter as you get closer
            LED.value = proximity
        time.sleep(.01)
except KeyboardInterrupt:
    GPIO.cleanup()
