MICROPYTHON = True
try:
    import machine
except ImportError:
    MICROPYTHON = False

CIRCUITPYTHON = True
try:
    import board
    import busio
    import digitalio
except ImportError:
    CIRCUITPYTHON = False

if not MICROPYTHON and not CIRCUITPYTHON:
    raise Exception("Could not import MicroPython or CircuitPython.")

class RGBKeypad():
    
    KEYPAD_ADDRESS = 32

    class MPDevice():
        
        PIN_SDA = 4
        PIN_SCL = 5
        PIN_CS = 17
        PIN_SCK = 18
        PIN_MOSI = 19

        def __init__(self):
            """
            Class for communicating with the keypad device using
            MicroPython
            """
            # setup i2c
            self._i2c = machine.I2C(
                0, 
                scl=machine.Pin(RGBKeypad.MPDevice.PIN_SCL), 
                sda=machine.Pin(RGBKeypad.MPDevice.PIN_SDA), 
                freq=400000
                )

            # setup spi
            self._spi = machine.SPI(
                0, 
                baudrate=4*1024*1024, 
                sck=machine.Pin(RGBKeypad.MPDevice.PIN_SCK), 
                mosi=machine.Pin(RGBKeypad.MPDevice.PIN_MOSI)
                )
            
            # setup cs
            self._cs = machine.Pin(
                RGBKeypad.MPDevice.PIN_CS, 
                machine.Pin.OUT
                )
            self._cs.high()
        
        def read_keys(self):
            self._i2c.writeto(RGBKeypad.KEYPAD_ADDRESS, bytearray(1), True)
            data = self._i2c.readfrom(RGBKeypad.KEYPAD_ADDRESS, 2, False)
            key_data = int.from_bytes(data, "little")
            return key_data

        def write_leds(self, led_data):
            self._cs.low()
            self._spi.write(led_data)
            self._cs.high()

    class RGBKey():

        def __init__(self, keypad, x, y, red, green, blue, brightness):
            """
            Internal class used to represent a single key of the RGB Keypad. 
            Returned when using RGBKeypad[x,y] or RGBKeypad.get_key(x,y).


            """
            self._keypad = keypad
            self._x = x
            self._y = y
            self._red = red
            self._green = green
            self._blue = blue
            self._brightness = brightness
            
        @property
        def x(self):
            return self._x

        @property
        def y(self):
            return self._y

        @property
        def brightness(self):
            return self._brightness

        @brightness.setter
        def brightness(self, value):
            value = max(min(1, value), 0)
            self._brightness = value
            self._update()

        @property
        def red(self):
            return self._red
        
        @red.setter
        def red(self, value):
            value = max(min(255, value), 0)
            self._red = value
            self._update()

        @property
        def green(self):
            return self._green
        
        @green.setter
        def green(self, value):
            value = max(min(255, value), 0)
            self._green = value
            self._update()

        @property
        def blue(self):
            return self._blue
        
        @blue.setter
        def blue(self, value):
            value = max(min(255, value), 0)
            self._blue = value
            self._update()

        @property
        def color(self):
            return (self.red, self.green, self.blue)

        @color.setter
        def color(self, value):

            auto_update_value = self._keypad.auto_update

            self.red = value[0]
            self.green = value[1]
            self.blue = value[2]

            self.auto_update = self._keypad.auto_update

            self._update()

        def is_pressed(self):
            return self._keypad.get_keys_pressed()[
                (4 * self._y) + (self._x % 4)
            ]

        def clear(self):
            self.color == (0, 0, 0)

        def _update(self):
            if self._keypad.auto_update:
                self._keypad.update()

    def __init__(self, color=(0,0,0), brightness=0.5, auto_update=True):

        # create the device
        self._device = RGBKeypad.MPDevice()

        # setup all the keys before setting auto update
        self.auto_update = False

        # setup keys
        self._keys = []
        for y in range(4):
            for x in range(4):
                self._keys.append(
                    RGBKeypad.RGBKey(self, x, y, color[0], color[1], color[2], brightness)
                    )
        
        self.update()
        
        self.auto_update = auto_update
        self._color = color
        self._brightness = brightness

    def clear(self):
        self.color = (0, 0, 0)

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        auto_update_value = self.auto_update

        self.auto_update = False
        for key in self._keys:
            key.color = (value[0], value[1], value[2])
        self.update()

        self.auto_update = auto_update_value
    
    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, value):
        auto_update_value = self.auto_update

        self.auto_update = False
        for key in self._keys:
            key.brightness = value
        self.update()

        self.auto_update = auto_update_value
    
    @property
    def keys(self):
        return self._keys
    
    def get_keys_pressed(self):
        button_data = self._device.read_keys()
        
        # button states
        button_states = []
        for button in range(16):
            button_states.append(0 == (button_data & (1<<button)))

        return button_states

    def get_key(self, x, y):
        return self._keys[(4 * y) + (x % 4)]

    def update(self):
        led_data = bytearray((16*4) + 8)
        data_pos = 4

        for key in self._keys:
            led_data[data_pos] = int(255 - 31 + (31 * key.brightness))
            led_data[data_pos + 1] = key.blue
            led_data[data_pos + 2] = key.green
            led_data[data_pos + 3] = key.red

            data_pos += 4

        self._device.write_leds(led_data)

    def __getitem__(self, index):
        return self.get_key(index[0], index[1])


from random import randint
from utime import sleep

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
                print("key",x,y,"pressed")
                
    sleep(0.1)

# for i in range(10):
#     for x in range(4):
#         for y in range(4):
#             key = keypad[x,y]
#             key.color = (
#                 randint(0,255),
#                 randint(0,255),
#                 randint(0,255))

# keypad.clear()


# key = keypad[3,3]
# key.color = (255,255,0)
# key.brightness = 0.1
