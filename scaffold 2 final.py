import time
import neopixel
from machine import Pin

# Pin definitions
NEOPIXEL_PIN = 4  # Change this to the GPIO pin you are using for NeoPixel
NUM_PIXELS = 16   # Number of LEDs in the strip
IN1 = Pin(18, Pin.OUT)
IN2 = Pin(19, Pin.OUT)
IN3 = Pin(21, Pin.OUT)
IN4 = Pin(22, Pin.OUT)

# Initialize NeoPixel
np = neopixel.NeoPixel(Pin(NEOPIXEL_PIN), NUM_PIXELS)

# Define colors (R, G, B)
colors = [
    (255, 0, 0),     # Red
    (255, 105, 180), # Pink
    (128, 0, 128),   # Purple
    (0, 0, 255),     # Blue
    (0, 255, 0),     # Green
    (255, 165, 0)    # Orange
]

# Function to step the motor once
def step_motor():
    IN1.value(1)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)
    time.sleep_ms(2)

    IN1.value(0)
    IN2.value(1)
    IN3.value(0)
    IN4.value(0)
    time.sleep_ms(2)

    IN1.value(0)
    IN2.value(0)
    IN3.value(1)
    IN4.value(0)
    time.sleep_ms(2)

    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(1)
    time.sleep_ms(2)

# Main loop
try:
    while True:
        for color in colors:
            # Set NeoPixel color
            for i in range(NUM_PIXELS):
                np[i] = color
            np.write()

            # Rotate motor for 2 seconds while maintaining this color
            start_time = time.ticks_ms()
            while time.ticks_diff(time.ticks_ms(), start_time) < 2000:  # 2 seconds
                step_motor()

except KeyboardInterrupt:
    # Turn off all LEDs and motor pins when program is interrupted
    for i in range(NUM_PIXELS):
        np[i] = (0, 0, 0)
    np.write()

    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)
