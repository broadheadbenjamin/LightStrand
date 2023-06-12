import board
import datetime
import neopixel
import sys
import holidays
import random
from datetime import date

# Output
DATA_PIN     = board.D18
LIGHT_COUNT  = 50
BRIGHTNESS   = 0
LIGHTS       = ""

# Colors (Green, Red, Blue)
COLOR_SCHEME = ""
BLUE         = (0, 0, 255)
DIM_WHITE    = (70, 70, 70)
DARK_ORANGE  = (30, 185, 0)
GREEN        = (255, 0, 0)
GOLD         = (85, 255, 0)
HALLOWEEN_PURPLE = (0, 120, 155)
LEPERCHAUN_GREEN = (255,250,0)
LIGHT_ORANGE = (60, 255, 0)
LIGHT_PURPLE = (60, 240, 250)
LIGHT_PINK   = (40, 255, 90)
LIGHT_YELLOW = (140, 255, 30)
MINT_GREEN   = (70, 0, 20)
ORANGE       = (40,255,0)
PINK         = (0, 120, 40)
SUMMER_PINK  = (20,255,70)
PURPLE       = (0, 35, 85)
RED          = (0, 255, 0)
TEAL         = (100, 0, 100)
TURQUOISE    = (100, 0, 90)
WHITE        = (255, 255, 255)
YELLOW       = (110,200,0)

# Supported holidays.
NEW_YEARS        = [(255,255,255),(255,255,245),(255,255,235),(255,255,225)]
VALENTINES_DAY   = [(0,255,255),(0,205,255),(0,165,255),(0,135,255)]
ST_PATRICKS_DAY  = [GREEN, GOLD, WHITE, GOLD, GREEN]
EASTER           = [LIGHT_PURPLE, LIGHT_YELLOW, PINK, LIGHT_PURPLE, LIGHT_YELLOW]
INDEPENDENCE_DAY = [RED, WHITE, BLUE]
BENS_BIRTHDAY    = [MINT_GREEN, MINT_GREEN, WHITE, MINT_GREEN, MINT_GREEN]
RANDEES_BIRTHDAY = ""
GENERIC_FALL     = [DARK_ORANGE, LIGHT_ORANGE]
HALLOWEEN        = [(0,80,255), (30,255,0), (255,0,0), (30,255,0), (0,80,255)]
THANKSGIVING     = ""
CHRISTMAS        = [(0, 100, 90), (70, 0, 160), (0, 0, 255), (70, 0, 160), (0, 100, 90)]
DEFAULT          = [WHITE, PURPLE, PURPLE, PURPLE, TEAL, PURPLE, PURPLE, PURPLE]
SUMMER           = [(0,255,190), (0,255,70), (100,255,0), (40,255,0), (100,255,0), (0,255,20), (0,255,190)] 
SUMMER_PINK_ONLY = [SUMMER_PINK]
JOE_BIDEN        = [(0,0,255),(50,0,255),(100,0,255),(150,0,255),(200,0,255)]

"""
Main method. Cycle through light schedule.
"""
def main():
    # Check Holidays
    #us_holidays = holidays.UnitedStates()
    #for date, name in sorted(holidays.US(years=datetime.datetime.now().year).items()):
    #    print(date, name)
    #print("Easter ", easter(datetime.datetime.now().year))

    # See if lights should be turned on.
    if sys.argv[1] == "on":
        BRIGHTNESS = 1
    else:
        BRIGHTNESS = 0

    # Set color scheme based on time of the year.
    # Green, Red, Blue
    random_colors = []
    for i in range (LIGHT_COUNT):
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        random_colors.append(random_color)


    COLOR_SCHEME = CHRISTMAS

    # Set light strand
    LIGHTS = neopixel.NeoPixel(DATA_PIN, LIGHT_COUNT, brightness = BRIGHTNESS, auto_write=True)
    for i in range(LIGHT_COUNT):
        LIGHTS[i] = COLOR_SCHEME[i % len(COLOR_SCHEME)]


def easter(year):
    "Returns Easter as a date object."
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1
    return date(year, month, day)

"""
Entry point to the program.
"""
if __name__ == "__main__":
    main()
