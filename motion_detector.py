from time import sleep
from gpiozero import LED, Buzzer, MotionSensor


def buzzer(PIN=23):
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
    sensor = MotionSensor(17)
    red_light_on()
    try:
        while True:
            if sensor.wait_for_motion():
                red_light_off()
                print('Motion detected')
                buzzer()
                green_light_on()
                sleep(2)
            else:
                green_light_buzzer_off()
                print('Motion not detected')
                print('Sleep mode :)')
                red_light_on()
                sleep(2)
    except KeyboardInterrupt:
        print('Exiting with ctrl-c!!!')
        
if __name__ == '__main__':
        main()