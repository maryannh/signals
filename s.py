from gpiozero import PiStop, Button, Servo, TrafficLights, Buzzer
from time import sleep
from signal import pause
import random

traffic = PiStop('D', False, False)
servo = Servo(18)

def train_coming():
   traffic.red.blink(on_time=0.5, off_time=0.5)
   traffic.green.off()
   traffic.amber.off()
   servo.min()
   sleep(20)

def all_clear():
   traffic.green.on()
   traffic.red.off()
   traffic.amber.off()
   servo.max()
   interval = random.randint(10,30)
   sleep(interval)

while True:
   all_clear()
   train_coming()  
