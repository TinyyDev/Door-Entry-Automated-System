from time import sleep
import motion_detector
from gpiozero import LED, Buzzer, Button

"""
if __name__ == "__main__":
    while True:
        if motion_detector.motion_detect():
            print("Somebody is closing")
        else:
            print("Nobody")
        time.sleep(1)
"""

while True:
    # LED(22).on()
    # LED(27).on()
    Buzzer(23).on()
    print('LED on')
    sleep(2)
    Buzzer(23).off()
    sleep(2)
    # sleep(2)
    # Buzzer(27).off()
    # print('LED off')
    # sleep(2)