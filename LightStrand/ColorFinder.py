import board
import neopixel
import sys

# Output
DATA_PIN     = board.D18
LIGHT_COUNT  = 50
BRIGHTNESS   = 0
LIGHTS = neopixel.NeoPixel(DATA_PIN, LIGHT_COUNT, brightness = 1, auto_write=True)

"""
Main method. Cycle through light schedule.
"""
def main():
    colorFinder()

"""
User interation to find color values.
"""
def colorFinder():
    G = 0
    R = 0
    B = 0
    step = 10
    while True:
        selection = input()
        if selection == "q":
            G = G + step
            if G > 255:
                G = 255
        if selection == "w":
            R = R + step
            if R > 255:
                R = 255
        if selection == "e":
            B = B + step
            if B > 255:
                B = 255
        if selection == "a":
            G = G - step
            if G < 0:
                G = 0
        if selection == "s":
            R = R - step
            if R < 0:
                R = 0
        if selection == "d":
            B = B - step
            if B < 0:
                B = 0
        LIGHTS.fill((G,R,B))
        print(G, ", ", R, ", ", B)

"""
Entry point to the program.
"""
if __name__ == "__main__":
    main()
