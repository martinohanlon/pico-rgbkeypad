<a name="rgbkeypad"></a>
# rgbkeypad

<a name="rgbkeypad.RGBKeypad"></a>
## RGBKeypad

```python
class RGBKeypad()
```

<a name="rgbkeypad.RGBKeypad.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(color=(0,0,0), brightness=0.5, auto_update=True)
```

Represents a pimoroni RGB Keypad device connected to a Raspberry Pi
pico running either MicroPython or CircuitPython.

```python
rgbkeypad = RGBKeyPad()
```

A single key can be obtained using its x, y coordinate ::

```python
key = rgbkeypad[0, 0]
```

##### color (tuple):

The initial color for all the keys.
A tuple of (red, green, blue) values between 0 and 255.

The default is (0, 0, 0), black or off.

##### brightness (int):
The initial brightness of the keys.

A value between 0 and 1 where 0 is off and 1 is full brightness.

The default is 0.5.

##### auto_update (bool):
When True, the key pad will be automatically updated
when the color or brightness of a key is changed.

If False, the update() method will need to be called
before any changes are reflected on the keypad.

The default is True

<a name="rgbkeypad.RGBKeypad.clear"></a>
#### clear

```python
 | clear()
```

Clears all the keys color. 

Clear is the same as setting the color to black (0, 0, 0).

<a name="rgbkeypad.RGBKeypad.color"></a>
#### color

```python
 | @property
 | color()
```

Sets the color of all the keys as a tuple of (red, green, blue) values
between 0 and 255.

> Note: color will return the "default" or "initial" color of the keys. 
If an individual key's color has been change this wont be represented.

<a name="rgbkeypad.RGBKeypad.brightness"></a>
#### brightness

```python
 | @property
 | brightness()
```

Sets the brightness of all the keys as a value between 0 and 1 where 
0 is off and 1 is full brightness.

> Note: brightness will return the "default" or "initial" brightness 
of the keys. If an individual key's brightness has been change this 
wont be represented.

<a name="rgbkeypad.RGBKeypad.keys"></a>
#### keys

```python
 | @property
 | keys()
```

Returns a list of all the keys as RGBKey objects.

<a name="rgbkeypad.RGBKeypad.get_keys_pressed"></a>
#### get\_keys\_pressed

```python
 | get_keys_pressed()
```

Returns a list of 16 booleans represent the current pressed
state of all the keys.

<a name="rgbkeypad.RGBKeypad.get_key"></a>
#### get\_key

```python
 | get_key(x, y)
```

Returns a key as an RGBKey object.

get_key(x, y) is the equivalent of RGBKeypad[x, y].

##### x (int):
The x position of the key.

##### y (int):
The y position of the key.

<a name="rgbkeypad.RGBKeypad.update"></a>
#### update

```python
 | update()
```

Updates the RGB Keypad with the current color and brightness.

> Note: is only required to be called when `auto_update = False`.

<a name="rgbkeypad.RGBKeypad.RGBKey"></a>
## RGBKey

```python
class RGBKey()
```

<a name="rgbkeypad.RGBKeypad.RGBKey.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(keypad, x, y, red, green, blue, brightness)
```
Represents a single key on the RGB Keypad. 

Returned when using `RGBKeypad[x, y]` or `RGBKeypad.get_key(x,y)`

```python
keypad = RGBKeypad()
key = keypad[0, 0]
```

<a name="rgbkeypad.RGBKeypad.RGBKey.x"></a>
#### x

```python
 | @property
 | x()
```

Returns the x position of the key.

<a name="rgbkeypad.RGBKeypad.RGBKey.y"></a>
#### y

```python
 | @property
 | y()
```

Returns the y position of the key.

<a name="rgbkeypad.RGBKeypad.RGBKey.brightness"></a>
#### brightness

```python
 | @property
 | brightness()
```

Sets or returns the brightness of the key. 

A value between 0 and 1 where 0 is off and 1 is full brightness.

<a name="rgbkeypad.RGBKeypad.RGBKey.red"></a>
#### red

```python
 | @property
 | red()
```

Sets or returns the red color of the key.

A value between 0 and 255.

<a name="rgbkeypad.RGBKeypad.RGBKey.green"></a>
#### green

```python
 | @property
 | green()
```

Sets or returns the green color of the key.

A value between 0 and 255.

<a name="rgbkeypad.RGBKeypad.RGBKey.blue"></a>
#### blue

```python
 | @property
 | blue()
```

Sets or returns the blue color of the key.

A value between 0 and 255.

<a name="rgbkeypad.RGBKeypad.RGBKey.color"></a>
#### color

```python
 | @property
 | color()
```

Sets or returns the color of the key.

A tuple of (red, green, blue) values between 0 and 255.

<a name="rgbkeypad.RGBKeypad.RGBKey.is_pressed"></a>
#### is\_pressed

```python
 | is_pressed()
```

Returns True if the key is pressed when called.

<a name="rgbkeypad.RGBKeypad.RGBKey.clear"></a>
#### clear

```python
 | clear()
```

Clears the key color. 

> Note: clear() is the same as setting the color to black (0, 0, 0).

