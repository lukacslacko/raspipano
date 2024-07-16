import time

from conn import DeviceMenu, send_keys
from menu import Menu, set_status
from keys import get_key_pressed

def say_hello():
    send_keys("Hello")
    
def three_spaces():
    for _ in range(3):
        send_keys(" ")
        time.sleep(1)

ROOT = Menu("RASPIPANO")
CONNECT = Menu("Connect", ROOT)
PANO = Menu("Panorama", ROOT)
LIST_DEVICES = DeviceMenu("Device", CONNECT)
TEST_HELLO = Menu("Say hello", CONNECT, on_enter=say_hello)
TEST_SPACE = Menu("3 spaces", CONNECT, on_enter=three_spaces)

current_menu = ROOT
current_menu.show()

while True:
    key = get_key_pressed()
    current_menu = current_menu.handle(key)
    current_menu.show()
