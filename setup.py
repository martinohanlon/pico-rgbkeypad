from setuptools import setup

__project__ = 'pico-rbgkeypad'
__packages__ = ['rgbkeypad']
__desc__ = 'A Python class for controlling the Pimoroni RGB Keypad for the Raspberry Pi Pico.'
__version__ = '0.2.0'
__author__ = "Martin O'Hanlon"
__author_email__ = 'martin@ohanlonweb.com'
__license__ = 'MIT'
__url__ = 'https://github.com/martinohanlon/pico-rbgkeypad'
__keywords__ = [
    'raspberry',
    'pi',
    'pico',
    'rgb',
    'keypad',
    'pimoroni',
]
__classifiers__ = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: Implementation :: MicroPython',
    ]
__long_description__ = """A Python class for controlling the [Pimoroni RGB Keypad](https://shop.pimoroni.com/products/pico-rgb-keypad-base) for the [Raspberry Pi Pico](https://www.raspberrypi.org/documentation/pico/getting-started/).

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

![pimoroni rgb keypad](https://cdn.shopify.com/s/files/1/0174/1800/products/pico-addons-2_1024x1024.jpg?v=1611177905)"""

setup(
    name=__project__,
    version=__version__,
    description=__version__,
    long_description=__long_description__,
    long_description_content_type='text/markdown',
    url=__url__,
    author=__author__,
    author_email=__author_email__,
    license=__license__,
    classifiers=__classifiers__,
    keywords=__keywords__,
    packages=__packages__,
)