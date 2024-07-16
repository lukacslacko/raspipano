import subprocess
import time

from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory

subprocess.run(["sudo", "pigpiod"])
time.sleep(3)

factory = PiGPIOFactory()

servo = AngularServo(14, min_pulse_width=500e-6, max_pulse_width=3600e-6, pin_factory=factory)
servo.angle = 45

while True:
    pass
    