from time import sleep
from gpiozero import LED, Buzzer, MotionSensor


def buzzer_on(PIN=23):
    buzz = Buzzer(PIN)
    buzz.on()
    sleep(0.9)
    buzz.off()
    sleep(0.1)
    
def buzzer_off(PIN=23):
    buzz = Buzzer(PIN)
    buzz.off()
    
def main():
    sensor = MotionSensor(17)
    red = LED(22)
    green = LED(27)
    
    try:
        while True:
            if sensor.value == 1:
                red.off()
                green.on()
                buzzer_on()
                print('Motion detected')
                sleep(2)
            elif sensor.value == 0:
                green.off()
                buzzer_off()
                red.on()
                print('Motion not detected')
                print('Sleep mode :)')
                sleep(1.5)
    except KeyboardInterrupt:
        print('Exiting with ctrl-c!!!')
        
if __name__ == '__main__':
    main()