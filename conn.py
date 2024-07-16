import subprocess

from menu import Menu, set_status

def get_devices():
    out = subprocess.check_output(["kdeconnect-cli", "-a", "--id-name-only"]).decode("utf-8")
    devices = [line for line in out.split("\n") if line]
    print(devices)
    return [(part.split()[0], " ".join(part.split()[1:])) for part in devices]

DEVICES = []
DEVICE_IDX = None

def choose_device(idx):
    global DEVICE_IDX, DEVICES
    DEVICE_IDX = idx
    set_status(DEVICES[DEVICE_IDX][1])

class DeviceMenu(Menu):
    def enter(self):
        self.items = []
        global DEVICES, DEVICE_IDX
        DEVICES = get_devices()
        if not DEVICES:
            DEVICE_IDX = None
            set_status("No devices")
            return
        for device in DEVICES:
            self.add(Menu(device[1]))
        choose_device(0)
    
    def handle(self, key):
        item, idx = self._handle(key)
        if item:
            return item
        choose_device(idx)
        return self
        