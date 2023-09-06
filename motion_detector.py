from time import sleep
from gpiozero import LED, Buzzer, MotionSensor


def buzzer(PIN=23):
    buzz = Buzzer(PIN)
    buzz.on()
    sleep(0.9)
    buzz.off()
    sleep(0.1)
    
def red_light_on(PIN=22):
    return LED(PIN).on()

def red_light_off(PIN=22):
    return LED(PIN).on()
    
def green_light_on(PIN=27):
    return LED(PIN).on()

def green_light_buzzer_off(PIN=27):
    LED(PIN).off()
    Buzzer(PIN).off()
    
def main():
    sensor = MotionSensor(17)
    LED(22).on()
    try:
        while True:
            if sensor.value == 1:
                LED(22).off() # red led
                print('Motion detected')
                buzzer()
                LED(27).on() # green led
                sleep(2)
            elif sensor.value == 0:
                LED(27).on() # green led
                print('Motion not detected')
                print('Sleep mode :)')
                red_light_on()
                sleep(2)
    except KeyboardInterrupt:
        print('Exiting with ctrl-c!!!')
        
if __name__ == '__main__':
    main()