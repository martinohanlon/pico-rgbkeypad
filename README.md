# rgbkeypad

A Python class for controlling the [Pimoroni RGB Keypad](https://shop.pimoroni.com/products/pico-rgb-keypad-base) for the [Raspberry Pi Pico](https://www.raspberrypi.org/documentation/pico/getting-started/).

![pimoroni rgb keypad](https://cdn.shopify.com/s/files/1/0174/1800/products/pico-addons-2_1024x1024.jpg?v=1611177905)

# Status

Not even alpha... Currently works with MicroPython, planning a CircuitPython implementation. Documentation, particularly how to use and API needs a lot more work.

## Install

Copy the [rbgkeypad code](https://github.com/martinohanlon/pico-rgbkeypad/blob/main/rgbkeypad/rgbkeypad.py) into your program.

## Usage

> Below is some typical use cases and examples for using the `RGBKeypad` class. See the [API](API.md) documentation for more information.

Create a keypad object.

```python
keypad = RGBKeypad()
```

### Display

The color of all the keys can be changed by setting the key pad's `color` property to a tuple of (red, green, blue) values between `0` and `255`.

```python
# red
keypad.color = (255, 0, 0)

# green
keypad.color = (0, 255, 0)

# blue
keypad.color = (0, 0, 255)

# white
keypad.color = (255, 255, 255)

# yellow
keypad.color = (255, 255, 0)

# purple
keypad.color = (128, 0, 128)
```

The brightness can be changed by setting the `brightness` property to a value between `0` and `1`. Where `1` is full brightness and `0` is off. By default the brightness is set to `0.5`.

```python
keypad.brightness = 1
```

The keypad can be cleared (turned off) using the `clear()` method.

```python
keypad.clear()
```

Individual keys can be referenced using their x,y position e.g. [0,0]

```python
key1 = keypad[0, 0]
```

Individual key's color and brightness can be set using the `color` and `brightness` properties.

```python
# red
key1.color = (255, 0, 0)

# full brightness
key1.brightness = 1
```

An individual key can also be cleared using the `clear()` method.

```python
key1.clear()
```

### Press

The status of the key can be retrieved using the `is_pressed()` method of an individual key.

```python
key1 = keypad[0, 0]
pressed = key1.is_pressed()
```

Use a loop to continuously check the status of a key.

```python
while True:
    if key1.is_pressed():
        print("key 1 pressed")
```

To check the status of all the keys, loop through the keypad's `keys` property, check each individually.

```python
while True:
    for key in keypad.keys:
        if key.is_pressed():
            print("key", key.x, key.y, "pressed)
```

Alternatively a list of all the keys pressed status can be obtained using the key pad's `get_keys_pressed()` method.

```python
keys_pressed = keypad.get_keys_pressed()
print(keys_pressed)
```
