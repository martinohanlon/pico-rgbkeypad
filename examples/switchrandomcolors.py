from random import randint

keypad = RGBKeypad()

while True:
    for x in range(4):
        for y in range(4):
            key = keypad[x,y]
            if key.is_pressed():
                
                key.color = (
                    randint(0,255),
                    randint(0,255),
                    randint(0,255)
                    )
                print("key", x, y, "pressed")
                