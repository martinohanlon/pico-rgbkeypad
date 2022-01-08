# rgbkeypad

A Python class for controlling the [Pimoroni RGB Keypad](https://shop.pimoroni.com/products/pico-rgb-keypad-base) for the [Raspberry Pi Pico](https://www.raspberrypi.org/documentation/pico/getting-started/).

Compatible with MicroPython and CircuitPython.

```python
keypad = RGBKeypad()

# make all the keys red
keypad.color = (255, 0, 0)

# turn a key blue when pressed
while True:
    for key in keypad.keys:
        if key.is_pressed():
            key.color = (0, 0, 255)
```

![pimoroni rgb keypad](https://cdn.shopify.com/s/files/1/0174/1800/products/pico-addons-2_1024x1024.jpg?v=1611177905)

# Status

Beta - version 0.2

## Install

There are a few options for installing `pico rgbkeypad`:

1. Copy the [rbgkeypad.py code](https://github.com/martinohanlon/pico-rgbkeypad/blob/main/rgbkeypad/rgbkeypad.py) into the top of your program.

2. Copy the [rgbkeypad folder](https://github.com/martinohanlon/pico-rgbkeypad/blob/main/rgbkeypad) to the lib folder on your pico (useful if you are using CircuitPython).

3. Install the [pico-rgbkeypad package from PyPi](https://pypi.org/project/pico-rbgkeypad) using `upip` or the [Manage Packages tool](https://github.com/thonny/thonny/wiki/InstallingPackages) in [Thonny](https://thonny.org/).

## Usage

Here you will find some typical use cases and examples for using `rgbkeypad`. See the [API](API.md) documentation for more information.

Import the `RGBKeypad` class from the `rgbkeypad` module.

> Note - you do not need to import the module if you copied the `rgbkeypad.py` code directly into your program.

```python
from rgbkeypad import RGBKeypad
```

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

## Deploy

These are instructions for how to deploy the `pico-rgbkeypad` to [PyPI](https://pypi.org/project/pico-rbgkeypad)

1. Install pre-requisites

~~~bash
pip3 install setuptools twine
~~~

2. Increment version numbers in `setup.py` and `README.md`

3. Build for deployment

~~~bash
python setup.py sdist
~~~

3. Deploy to PyPI

~~~bash
twine upload dist/* --skip-existing
~~~
