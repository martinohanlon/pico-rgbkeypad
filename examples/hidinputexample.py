# From the example of martinohanlon at https://github.com/martinohanlon/pico-rgbkeypad/blob/main/examples/hid_keyboard.py
# Using adafruit dotstar colorwheel examples

import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
from rgbkeypad import *

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

KEYBOARD_MAP = {
    (0,0): ("volu",),
    (1,0): ("mpc next",),
    (2,0): ("rad4",),
    (3,0): ("mpc next",),
    (0,1): ("vold",),
    (1,1): ("mpc prev",),
    (2,1): ("rad3",),
    (3,1): ("mpc prev",),
    (0,2): ("toggle_disp1",),
    (1,2): ("mpc stop",),
    (2,2): ("rad2",),
    (3,2): ("mpc stop",),
    (0,3): ("ssh pi\"192.168.9.97 picade_switch",),
    (1,3): ("mpc toggle",),
    (2,3): ("rad1",),
    (3,3): ("mpc toggle",)
}

def colorwheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3)

KEYBOARD_COLOUR = {
    (0,0): colorwheel(0 * 16),
    (1,0): colorwheel(1 * 16),
    (2,0): colorwheel(2 * 16),
    (3,0): colorwheel(3 * 16),
    (0,1): colorwheel(4 * 16),
    (1,1): colorwheel(5 * 16),
    (2,1): colorwheel(6 * 16),
    (3,1): colorwheel(7 * 16),
    (0,2): colorwheel(8 * 16),
    (1,2): colorwheel(9 * 16),
    (2,2): colorwheel(10 * 16),
    (3,2): colorwheel(11 * 16),
    (0,3): colorwheel(12 * 16),
    (1,3): colorwheel(13 * 16),
    (2,3): colorwheel(14 * 16),
    (3,3): colorwheel(15 * 16)
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
                key.color = (KEYBOARD_COLOUR[(key.x, key.y)])
                layout.write(*KEYBOARD_MAP[(key.x, key.y)])
                kbd.send(Keycode.ENTER)
                key.color = (0,0,0)
            else:
                key.color = INVALID_KEY_COLOR
            
            # what for the key to be released
            while key.is_pressed():
                pass
            key.clear()
