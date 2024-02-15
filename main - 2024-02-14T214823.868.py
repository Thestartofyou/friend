import board
import neopixel
import time

# Number of LEDs
num_leds = 10

# Define the pin for the NeoPixel strip
pixel_pin = board.D18  # Change to the appropriate pin

# Initialize the NeoPixel strip
pixels = neopixel.NeoPixel(pixel_pin, num_leds, brightness=0.5, auto_write=False)

# Define some preset colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)

# Function to set color of all LEDs
def set_color(color):
    pixels.fill(color)
    pixels.show()

# Function to fade in/out
def fade_in_out(color, duration):
    steps = 100
    for i in range(steps):
        brightness = i / steps
        pixels.fill((int(color[0]*brightness), int(color[1]*brightness), int(color[2]*brightness)))
        pixels.show()
        time.sleep(duration / steps)
    for i in range(steps, 0, -1):
        brightness = i / steps
        pixels.fill((int(color[0]*brightness), int(color[1]*brightness), int(color[2]*brightness)))
        pixels.show()
        time.sleep(duration / steps)

# Function for a color wipe effect
def color_wipe(color, wait):
    pixels.fill((0, 0, 0))
    pixels.show()
    for i in range(num_leds):
        pixels[i] = color
        pixels.show()
        time.sleep(wait)

# Main loop
while True:
    # Set color to red and fade in/out
    fade_in_out(RED, 2)
    
    # Set color to green and fade in/out
    fade_in_out(GREEN, 2)
    
    # Set color to blue and fade in/out
    fade_in_out(BLUE, 2)
    
    # Color wipe with yellow
    color_wipe(YELLOW, 0.05)
