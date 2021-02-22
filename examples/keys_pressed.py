keypad = RGBKeypad()

while True:
    for key in keypad.keys:
        if key.is_pressed():
            print("key", key.x, key.y, "pressed")

            