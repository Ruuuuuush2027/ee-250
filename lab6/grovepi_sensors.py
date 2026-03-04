# team members: Junsoo Kim, Mo Jiang
# link: https://github.com/Ruuuuuush2027/ee-250.git

import sys
sys.path.append('~/grove_pi_examples')
import time
import grovepi
from grove_rgb_lcd import *

# Grove Ultrasonic Ranger connectd to digital port 2
ultrasonic_ranger = 2
# potentiometer connected to analog port A0 as input
potentiometer = 0
grovepi.pinMode(potentiometer,"INPUT")

# clear lcd screen  before starting main loop
setText("")
last_state = (None, None)

while True:
  try:
    # TODO:read distance value from Ultrasonic Ranger and print distance on LCD
    ults_value = grovepi.ultrasonicRead(ultrasonic_ranger)

    # TODO: read threshold from potentiometer
    pot_value = grovepi.analogRead(potentiometer)
    
    current_state = (pot_value, ults_value)
    # TODO: format LCD text according to threshhold
    if current_state != last_state:
        last_state = current_state
        pres_txt = ""
        if pot_value < ults_value: # not in range
            setRGB(0, 255, 0)
        else:
            pres_txt = "OBJ PRES"
            setRGB(255, 0, 0)

        txt = "{0}cm {1}\n{2}cm".format(pot_value, pres_txt, ults_value)
        setText(txt)
    time.sleep(0.2)

  except IOError:
    print("Error")
