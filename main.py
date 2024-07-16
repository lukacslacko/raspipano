from conn import DeviceMenu
from menu import Menu, set_status
from keys import get_key_pressed

ROOT = Menu("RASPIPANO")
CONNECT = Menu("Connect", ROOT)
PANO = Menu("Panorama", ROOT)
LIST_DEVICES = DeviceMenu("Device", CONNECT)
TEST_HELLO = Menu("Say hello", CONNECT)
TEST_SPACE = Menu("3 spaces", CONNECT)

current_menu = ROOT
current_menu.show()

while True:
    key = get_key_pressed()
    current_menu = current_menu.handle(key)
    current_menu.show()
