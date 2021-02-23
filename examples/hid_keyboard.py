# This example uses CircuitPython and needs the adafruit_hid library
# Download the library bundle from https://learn.adafruit.com/welcome-to-circuitpython/circuitpython-libraries
# Copy adafruit_hid directory to the lib directory on the pico
# You are going to need the rgbkeypad code as well so copy it into the top of this example

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# map the position of the keys on the RGBKeypad to keyboard strokes
# circuitpython keycodes can be found here - 
#   https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/master/adafruit_hid/keycode.py
KEYBOARD_MAP = {
    (0,0): (Keycode.SHIFT, Keycode.M,),
    (1,0): (Keycode.A,),
    (2,0): (Keycode.R,),
    (3,0): (Keycode.T,),
    (0,1): (Keycode.SHIFT, Keycode.W,),
    (1,1): (Keycode.O,),
    (2,1): (Keycode.Z,),
    (0,2): (Keycode.SHIFT, Keycode.E,),
    (1,2): (Keycode.R,),
    (2,2): (Keycode.E,),
    (3,2): (Keycode.SHIFT, Keycode.ONE,),
    (3,3): (Keycode.ENTER,)
}

# what colors to use if an assigned/unassigned key is pressed
VALID_KEY_COLOR = (0, 0, 255)
INVALID_KEY_COLOR = (255, 0, 0)

keypad = RGBKeypad()
kbd = Keyboard(usb_hid.devices)

while True:
    # loop through all the keys
    for key in keypad.keys:
        # has a key been pressed?
        if key.is_pressed():
            # does this key have a keyboard mapping
            if (key.x, key.y) in KEYBOARD_MAP.keys():
                # debug - print out the keyboard strokes
                # print(KEYBOARD_MAP[(key.x, key.y)])
                key.color = VALID_KEY_COLOR
                # send the keyboard strokes
                kbd.send(*KEYBOARD_MAP[(key.x, key.y)]) 
            else:
                key.color = INVALID_KEY_COLOR
            
            # what for the key to be released
            while key.is_pressed():
                pass
            key.clear()
