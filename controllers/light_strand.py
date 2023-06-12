import os
from astral import LocationInfo
from astral.sun import sun
from astral.geocoder import database, lookup
from datetime import date, datetime, timedelta, timezone
from time import sleep


"""
Main method. Turn lights on and off based on time of day.
"""
def main():
    # Track Light state
    lastLightState = ""

    # Loop indefinitely
    while True:
        # Update the sun schedule.
        currentTime = datetime.now(timezone.utc) - timedelta(hours = 6)
        city        = lookup("Salt Lake City", database())
        sunToday    = sun(city.observer, date=datetime.now())
        sunrise     = sunToday["sunrise"] - timedelta(hours = 6)
        sunset      = sunToday["sunset"]  - timedelta(hours = 6)

        # See if lights need to be turned on/off.
        if currentTime < sunrise or currentTime > sunset:
            if lastLightState != "on":
                lastLightState = "on"
                os.system('/usr/bin/python3 /home/pi/LightStrand/update_lights.py on')
        else:
            if lastLightState != "off":
                lastLightState = "off"
                os.system('/usr/bin/python3 /home/pi/LightStrand/update_lights.py off')

        # Only execute the loop once a minute.
        sleep(60)


"""
Entry point to the program.
"""
if __name__ == "__main__":
    main()
