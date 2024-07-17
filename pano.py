import subprocess
import time

from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory

from conn import send_keys
from keys import get_key_pressed
from menu import Menu
from oled import disp

subprocess.run(["sudo", "pigpiod"])
time.sleep(3)

factory = PiGPIOFactory()

horiz_servo = AngularServo(14, min_pulse_width=500e-6, max_pulse_width=3600e-6, pin_factory=factory)
horiz_servo.angle = 0

class Range:
    def __init__(self, servo, width, num, pause, name):
        self.width = width
        self.num = num
        self.pause = pause
        self.servo = servo
        self.name = name
        
    def execute(self, start=0):
        disp.fill(0)
        disp.text("Taking panorama", 0, 0, 1)
        disp.show()
        step = 0 if self.num == 1 else self.width / (self.num - 1)
        ang = -self.width/2
        for i in range(self.num):
            disp.fill(0)
            disp.text("Taking panorama", 0, 0, 1)
            disp.text(str(i+1+start) + " / " + str(self.num))
            disp.show()
            self.servo.angle = ang
            ang += step
            time.sleep(self.pause)
            conn.send_keys(" ")
            time.sleep(self.pause)
    
    def describe(self):
        return self.name + ": " + str(self.width) + "x" + str(self.num) + " @ " + str(self.pause) + "s"
        
    def read(self, param):
        def render(value):
            disp.fill(0)
            disp.text("Set " + self.param + " for " + self.name, 0, 0, 1)
            disp.text("Enter number then *", 0, 10, 1)
            disp.text(param + ": " + value + "|", 0, 20, 1)
            disp.show()
        value = ""
        while True:
            render(value)
            k = get_key_pressed()
            if not k:
                continue
            if k in "0123456789":
                value += k
                continue
            if value:
                return int(value)
            return 0
                
    def update(self):
        self.width = self.read("width")
        self.num = self.read("num")
        self.pause = self.read("pause")
            
        

class PanoMenu(Menu):
    horiz = Range(horiz_servo, 180, 5, 2)
    
    def enter():
        self.items = [Menu(horiz.describe()), Menu("Execute!")]
        return True
    
    def handle(self, key):
        item, idx = self._handle(key)
        if item:
            return item
        if idx == 0:
            horiz.update()
        if idx == 1:
            horiz.execute()
        return self
