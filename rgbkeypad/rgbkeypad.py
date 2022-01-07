MICROPYTHON = True
try:
    import machine
    
    PIN_SDA = 4
    PIN_SCL = 5
    PIN_CS = 17
    PIN_SCK = 18
    PIN_MOSI = 19

except ImportError:
    MICROPYTHON = False

CIRCUITPYTHON = True
try:
    import board
    import busio
    import digitalio
    
    PIN_SDA = board.GP4
    PIN_SCL = board.GP5
    PIN_CS = board.GP17
    PIN_SCK = board.GP18
    PIN_MOSI = board.GP19
        
except ImportError:
    CIRCUITPYTHON = False

if not MICROPYTHON and not CIRCUITPYTHON:
    raise Exception("Could not find MicroPython or CircuitPython.")

class RGBKeypad():
    
    KEYPAD_ADDRESS = 32

    class MPDevice():
        
        def __init__(self):
            """
            Internal class used to communicate with the keypad device when
            using MicroPython.
            """
            # setup i2c
            self._i2c = machine.I2C(
                0, 
                scl=machine.Pin(PIN_SCL), 
                sda=machine.Pin(PIN_SDA), 
                freq=400000
                )

            # setup spi
            self._spi = machine.SPI(
                0, 
                baudrate=4*1024*1024, 
                sck=machine.Pin(PIN_SCK), 
                mosi=machine.Pin(PIN_MOSI)
                )
            
            # setup cs
            self._cs = machine.Pin(
                PIN_CS, 
                machine.Pin.OUT
                )
            self._cs.high()
        
        def read_keys(self):
            self._i2c.writeto(RGBKeypad.KEYPAD_ADDRESS, bytearray(1), True)
            data = self._i2c.readfrom(RGBKeypad.KEYPAD_ADDRESS, 2, False)
            return data

        def write_leds(self, led_data):
            self._cs.low()
            self._spi.write(led_data)
            self._cs.high()
            
    class CPDevice():
        


        def __init__(self):
            """
            Internal class used to communicate with the keypad device when
            using CircuitPython.
            """
            
            PIN_SDA = board.GP4
            PIN_SCL = board.GP5
            PIN_CS = board.GP17
            PIN_SCK = board.GP18
            PIN_MOSI = board.GP19
            # setup i2c
            self._i2c = busio.I2C(
                scl=PIN_SCL, 
                sda=PIN_SDA,
                frequency=400000
                )
            self._i2c.try_lock()

            # setup spi
            self._spi = busio.SPI(
                clock=PIN_SCK, 
                MOSI=PIN_MOSI
                )
            self._spi.try_lock()
            self._spi.configure(baudrate=4*1024*1024)
            
            # setup cs
            self._cs = digitalio.DigitalInOut(PIN_CS)
            self._cs.direction = digitalio.Direction.OUTPUT
            self._cs.value = True
        
        def read_keys(self):
            self._i2c.writeto(RGBKeypad.KEYPAD_ADDRESS, bytearray(1))
            data = bytearray(2)
            self._i2c.readfrom_into(RGBKeypad.KEYPAD_ADDRESS, data)
            return data

        def write_leds(self, led_data):
            self._cs.value = False
            self._spi.write(led_data)
            self._cs.value = True

    class RGBKey():

        def __init__(self, keypad, x, y, red, green, blue, brightness):
            """
            Represents a single key of the RGB Keypad. 

            Returned when using RGBKeypad[x,y] or RGBKeypad.get_key(x,y)::

                keypad = RGBKeypad()
                key = keypad[0, 0]

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
            """
            Returns the x position of the key.
            """
            return self._x

        @property
        def y(self):
            """
            Returns the y position of the key.
            """
            return self._y

        @property
        def brightness(self):
            """
            Sets or returns the brightness of the key. 

            A value between 0 and 1 where 0 is off and 1 is full brightness.
            """
            return self._brightness

        @brightness.setter
        def brightness(self, value):
            value = max(min(1, value), 0)
            self._brightness = value
            self._update()

        @property
        def red(self):
            """
            Sets or returns the red color of the key.

            A value between 0 and 255.
            """
            return self._red
        
        @red.setter
        def red(self, value):
            value = max(min(255, value), 0)
            self._red = value
            self._update()

        @property
        def green(self):
            """
            Sets or returns the green color of the key.

            A value between 0 and 255.
            """
            return self._green
        
        @green.setter
        def green(self, value):
            value = max(min(255, value), 0)
            self._green = value
            self._update()

        @property
        def blue(self):
            """
            Sets or returns the blue color of the key.

            A value between 0 and 255.
            """
            return self._blue
        
        @blue.setter
        def blue(self, value):
            value = max(min(255, value), 0)
            self._blue = value
            self._update()

        @property
        def color(self):
            """
            Sets or returns the color of the key.

            A tuple of (red, green, blue) values between 0 and 255.
            """
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
            """
            Returns True if the key is pressed when called.
            """
            return self._keypad.get_keys_pressed()[
                (4 * self._y) + (self._x % 4)
            ]

        def clear(self):
            """
            Clears the key color. 

            Clear is the same as setting the color to black (0, 0, 0).
            """
            self.color = (0, 0, 0)

        def _update(self):
            if self._keypad.auto_update:
                self._keypad.update()

    def __init__(self, color=(0,0,0), brightness=0.5, auto_update=True):
        """
        Represents a pimoroni RGB Keypad device connected to a Raspberry Pi
        pico running either MicroPython or CircuitPython.

        ::

            rgbkeypad = RGBKeyPad()

        A single key can be obtained using its x, y coordinate ::

            key = rgbkeypad[0, 0]

        :param tuple color:
            The initial color for all the keys. 

            A tuple of (red, green, blue) values between 0 and 255.

            The default is (0, 0, 0), black or off.

        :param int brightness:
            The initial brightness of the keys.

            A value between 0 and 1 where 0 is off and 1 is full brightness.

            The default is 0.5.

        :param bool auto_update:
            When True, the key pad will be automatically updated
            when the color or brightness of a key is changed.

            If False, the update() method will need to be called
            before any changes are reflected on the keypad.

            The default is True
        """
        # create the device
        if MICROPYTHON:
            self._device = RGBKeypad.MPDevice()
        else:
            self._device = RGBKeypad.CPDevice()

        # setup all the keys before setting aut o update
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
        """
        Clears all the keys color. 

        Clear is the same as setting the color to black (0, 0, 0).
        """
        self.color = (0, 0, 0)

    @property
    def color(self):
        """
        Sets the color of all the keys as a tuple of (red, green, blue) values
        between 0 and 255.

        Note - color will return the "default" or "initial" color of the keys. 
        If an individual key's color has been change this wont be represented.
        """
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
        """
        Sets the brightness of all the keys as a value between 0 and 1 where 
        0 is off and 1 is full brightness.

        Note - brightness will return the "default" or "initial" brightness 
        of the keys. If an individual key's brightness has been change this 
        wont be represented.
        """
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
        """
        Returns a list of all the keys as RGBKey objects.
        """
        return self._keys
    
    def get_keys_pressed(self):
        """
        Returns a list of 16 booleans represent the current pressed
        state of all the keys.
        """
        data = self._device.read_keys()
        button_data = int.from_bytes(data, "little")
        
        # button states
        button_states = []
        for button in range(16):
            button_states.append(0 == (button_data & (1<<button)))

        return button_states

    def get_key(self, x, y):
        """
        Returns a key as an RGBKey object.

        get_key(x, y) is the equivalent of RGBKeypad[x, y].

        :param int x:
            The x position of the key.

        :param int y:
            The y position of the key.
        """
        return self._keys[(4 * y) + (x % 4)]

    def update(self):
        """
        Updates the RGB Keypad with the current color and brightness.

        Is only required to be called when auto_update = False.
        """
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
