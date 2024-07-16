import json
import os
import subprocess

from menu import Menu, set_status

# Expected format:
# [
# {"ssid": "foo", "key": "S3cr3tP4ssw0rd"},
# {"ssid": "bar", "key": "1234"},
# ]

with open(os.path.expanduser("~/passwords.txt")) as passwords:
    f = passwords.read()
    print(f)
    PASSWORDS = json.loads(f)
    print(PASSWORDS)

print(PASSWORDS)

def wpa(args):
    print("Running wpa: ", args)
    out = subprocess.check_output(["wpa_cli"] + args)
    print("WPA response:\n", out)
    return [line for line in out.decode("utf-8").split("\n") if line]

network_ids = []
for pw in PASSWORDS:
    resp = wpa(["add_network"])
    nid = int(resp[1])
    network_ids.append(nid)
    wpa(["set_network", str(nid), "ssid", '"' + pw["ssid"] + '"'])
    wpa(["psk_passphrase", str(nid), '"' + pw["key"] + '"'])
    
print(wpa(["list_networks"]))

class WifiMenu(Menu):
    def enter(self):
        print("Hello Wifi menu")
        
        self.items = []
        for pw in PASSWORDS:
            self.add(Menu(pw["ssid"]))
        print(self.items)
        return True
    
    def handle(self, key):
        item, idx = self._handle(key)
        if item is not None:
            return item
        wpa(["select_network", str(network_ids[idx])])
        set_status("wifi", PASSWORDS[idx]["ssid"])
        return self