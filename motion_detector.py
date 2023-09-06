from time import sleep
from gpiozero import LED, Buzzer, MotionSensor


def buzzer_on(PIN=23):
    buzz = Buzzer(PIN)
    buzz.on()
    sleep(0.9)
    buzz.off()
    sleep(0.1)
    
def red_light_on(PIN=22):
    red = LED(PIN)
    red.on()

def red_light_off(PIN=22):
    red = LED(PIN)
    red.off()
    
def green_light_on(PIN=27):
    green = LED(PIN)
    green.on()

def green_light_off(PIN=27):
    green = LED(PIN)
    green.on()
    
def buzzer_off(PIN=23):
    buzzer = Buzzer(PIN)
    buzzer.off()
    
def main():
    sensor = MotionSensor(17)
    red_light_on()
    try:
        while True:
            if sensor.value == 1:
                red_light_off() # red led
                buzzer_on()
                print('Motion detected')
                sleep(1.5)
            elif sensor.value == 0:
                green_light_off()
                buzzer_off()
                red_light_on()
                red_light_on()
                print('Motion not detected')
                print('Sleep mode :)')
                sleep(1.5)
    except KeyboardInterrupt:
        print('Exiting with ctrl-c!!!')
        
if __name__ == '__main__':
    main()