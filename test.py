from time import sleep
from gpiozero import LED

while True:
    LED(22).on()
    LED(27).on()
    