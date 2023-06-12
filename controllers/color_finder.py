import board
import neopixel
import pytz
from astral import LocationInfo
from astral.sun import sun
from astral.geocoder import database, lookup
from datetime import date, datetime, timedelta, timezone
from time import sleep

# Output
DATA_PIN     = board.D18
LIGHT_COUNT  = 50
BRIGHTNESS   = 1
LIGHTS       = neopixel.NeoPixel(DATA_PIN, LIGHT_COUNT, brightness = 1, auto_write=True)

# City and Sun
city    = lookup("Salt Lake City", database())
s       = sun(city.observer, date=datetime.now())
dawn    = s["dawn"]    - timedelta(hours = 6)
sunrise = s["sunrise"] - timedelta(hours = 6)
noon    = s["noon"]    - timedelta(hours = 6)
sunset  = s["sunset"]  - timedelta(hours = 6)
dusk    = s["dusk"]    - timedelta(hours = 6)

# Colors (Green, Red, Blue)
BLUE         = (0, 0, 255)
GREEN        = (255, 0, 0)
LIGHT_PURPLE = (60, 240, 250)
LIGHT_YELLOW = (0, 140, 255, 30)
PINK         = (40, 255, 90)
RED          = (0, 255, 0)
TURQUOISE    = (100, 0, 90)
WHITE        = (255, 255, 255)

# Current light scheme
currentColorScheme = [WHITE]

"""
Main method. Cycle through light schedule.
"""
def main():
    #colorFinder()

    while True:
        updateSun()

        # Set color scheme based nearest holiday.
        currentColorScheme = [LIGHT_PURPLE, LIGHT_YELLOW, PINK, LIGHT_PURPLE, LIGHT_YELLOW]

        # Set light brightness based on time of day.
        if now() > dawn and now() < sunrise:
            sleepDelay = int((sunrise - dawn).total_seconds()) / 100
            for i in range(1, 100):
                brightnessLevel = i / 100.0
                LIGHTS = neopixel.NeoPixel(DATA_PIN, LIGHT_COUNT, brightness = brightnessLevel, auto_write=True)
                setColorScheme(LIGHTS, currentColorScheme)
                sleep(sleepDelay)
        elif now() > sunset and now() < dusk:
            sleepDelay = int((dusk - sunset).total_seconds()) / 100
            for i in range(1, 100):
                brightnessLevel = 1 - i / 100.0
                LIGHTS = neopixel.NeoPixel(DATA_PIN, LIGHT_COUNT, brightness = brightnessLevel, auto_write=True)
                setColorScheme(LIGHTS, currentColorScheme)
                sleep(sleepDelay)
        else:
            for i in range(1, 100):
                brightnessLevel = i / 100.0
                print("Brightness: ", brightnessLevel)
                TEST = neopixel.NeoPixel(DATA_PIN, LIGHT_COUNT, brightness = 1, auto_write=True)
                print(TEST.brightness)
                setColorScheme(TEST, currentColorScheme)
                sleep(1)

        sleep(60)

"""
Sets the color scheme for the light strand.
"""
def setColorScheme(lightStrand, colors):
    for i in range(1, LIGHT_COUNT):
        lightStrand[i] = colors[i % len(colors)]

def now():
    return datetime.now(timezone.utc) - timedelta(hours = 6) 

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

def updateSun():
    s       = sun(city.observer, date=datetime.now())
    dawn    = s["dawn"]    - timedelta(hours = 6)
    sunrise = s["sunrise"] - timedelta(hours = 6)
    noon    = s["noon"]    - timedelta(hours = 6)
    sunset  = s["sunset"]  - timedelta(hours = 6)
    dusk    = s["dusk"]    - timedelta(hours = 6)

"""
Entry point to the program.
"""
if __name__ == "__main__":
    main()
