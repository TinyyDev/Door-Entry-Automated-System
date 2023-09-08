from flask import Flask, render_template
from time import sleep
from gpiozero import LED, Buzzer, MotionSensor

app = Flask(__name__)


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
    condition_variable = False
    try:
        while True:
            if sensor.value == 1:
                red.off()
                green.on()
                buzzer_on()
                condition_variable = True
                print('Motion detected')
                sleep(3)
            elif sensor.value == 0:
                green.off()
                buzzer_off()
                red.on()
                condition_variable = False
                print('Motion not detected')
                print('Sleep mode :)')
                sleep(2)
    except KeyboardInterrupt:
        print('Exiting with ctrl-c!!!')
        
if __name__ == '__main__':
    main()


@app.route('/')
def index():
    return render_template('./public/tinnydev.html')

@app.route('/main')
def main():
    return render_template('./public/main.html', condition=condition_variable)


if __name__ == '__main__':
    app.run(debug=True)


