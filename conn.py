import subprocess

def get_devices():
    out = subprocess.check_output(["kdeconnect-cli", "-a", "--id-name-only"]).decode("utf-8")
    devices = [line for line in out.split("\n") if line]
    print(devices)
    return [(part.split()[0], " ".join(part.split()[1:])) for part in devices]
