from neopixel import NeoPixel
from machine import Pin
import time

np = NeoPixel(Pin(32), 64)

def board_idx(x, y):
    return y * 8 + x

def clear():
    for i in range(64):
        np[i] = (0, 0, 0)
    np.write()
    time.sleep_ms(10)  # ← add here

# Test 1: chase
print("Test 1: chase")
clear()
for i in range(64):
    if i > 0:
        np[i-1] = (0, 0, 0)
    np[i] = (60, 60, 60)
    np.write()
    time.sleep_ms(10)  # ← add here
    time.sleep_ms(40)
time.sleep(1)

# Test 2: red fill
print("Test 2: red fill")
clear()
for i in range(64):
    np[i] = (150, 0, 0)
np.write()
time.sleep_ms(10)  # ← add here
time.sleep(2)

# Test 3: green cross
print("Test 3: green cross")
clear()
for x in range(8):
    np[board_idx(x, 3)] = (0, 150, 0)
for y in range(8):
    np[board_idx(3, y)] = (0, 150, 0)
np.write()
time.sleep_ms(10)  # ← add here
time.sleep(2)

# Test 4: rainbow rows
print("Test 4: rainbow rows")
colors = [
    (150, 0, 0), (150, 60, 0), (120, 120, 0), (0, 150, 0),
    (0, 120, 120), (0, 0, 150), (100, 0, 150), (150, 0, 100)
]
clear()
for y in range(8):
    for x in range(8):
        np[board_idx(x, y)] = colors[y]
np.write()
time.sleep_ms(10)  # ← add here
time.sleep(3)

clear()
print("Done!")