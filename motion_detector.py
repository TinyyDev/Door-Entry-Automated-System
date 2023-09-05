import RPi.GPIO as GPIO
from time import sleep
from gpiozero import LED, Buzzer, Button
from signal import pause

def motion_detect(PIN: int):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.IN)
    motion = GPIO.input(17)
    GPIO.cleanup()
    return motion

def buzzer(PIN=27):
    buzz = Buzzer(PIN)
    buzz.on()
    sleep(0.9)
    buzz.off()
    sleep(0.1)
    
def red_light_on(PIN=22):
    LED(PIN).on()

def red_light_off(PIN=22):
    return LED(PIN).on()
    
def green_light_on(PIN=27):
    return LED(PIN).on()

def green_light_buzzer_off(PIN=27):
    LED(PIN).off()
    Buzzer(PIN).off()
    
def main():
    button = Button(17)
    red_light_on()
    try:
        while True:
            if button.is_pressed:
                red_light_off()
                print('Button pressed!')
                buzzer()
                green_light_on()
                sleep(2)
            else:
                green_light_buzzer_off()
                print('Sleep mode :)')
                red_light_on()
                sleep(2)
    except KeyboardInterrupt:
        print('Exiting with ctrl-c!!!')
        
if __name__ == '__main__':
        main()