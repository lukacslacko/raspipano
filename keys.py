import RPi.GPIO as GPIO

# white to red
pins = [0, 6, 13,19, 26, 21, 20, 16]
out_pins = pins[:4]
in_pins = pins[4:]

for i in in_pins:
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
for o in out_pins:
    GPIO.setup(o, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
    
KEYS_STATE = [1 for _ in range(16)]

def current_keys():
    state = []
    for o in out_pins:
        GPIO.setup(o, GPIO.OUT)
        GPIO.output(o, GPIO.LOW)
        for i in in_pins:
            state.append(GPIO.input(i))
        GPIO.setup(o, GPIO.IN, pull_up_down=GPIO.PUD_OFF)
    return state
    
def get_key_pressed():
    global KEYS_STATE
    keys_now = current_keys()
    pressed = -1
    for i in range(16):
        if not keys_now[i] and KEYS_STATE[i]:
            pressed = i
    KEYS_STATE = keys_now
    if pressed < 0:
        return ""
    return "123A456B789C*0#D"[pressed]
