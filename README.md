# Door-Entry-Automated-System
The "Simple Room Entry Home Automation System" is a cost-effective and user-friendly solution designed to enhance the convenience and energy efficiency of your home. This system is capable of automatically detecting a person's entry into a room, opening the door, and then closing it when the person leaves. It provides a seamless and hands-free experience, making your daily routines more efficient and comfortable.

# Components needed (Tech Stack)
## Hardware
1. **Motion Sensors:** Infrared (IR) motion sensors are used to detect the presence of a person entering the room. These sensors can detect changes in heat signatures and trigger the automation system.
2. **Microcontroller:** A microcontroller, such as an Arduino or Raspberry Pi, serves as the brain of the system. It processes the sensor data and controls the door-opening mechanism.
3. **Door Control Mechanism:** This component includes a motor or actuator responsible for opening and closing the door. It can be connected to the microcontroller and operated based on input from the motion sensor.
4. **User Interface:** A user-friendly interface, such as a smartphone app or a physical control panel, allows users to customize system settings and manually control the door if needed.
5. **Power Supply:** A power supply unit provides the necessary electrical power to the system components.

## Software
Flask, Html, Css, GPIOzero package from python, Git and Github for version control


### How to Download
Open command line and run the following command
```
git clone https://github.com/TinyyDev/Door-Entry-Automated-System.git
```

3. Install python
4. Pip install Flask
5. In your favourite IDE create a python environmennt to help run the web App
6. Connect your PIR sensor, LED and Breadboard to the Raspberry Pi using your Jumper wires
7. Consult the GPIO pin table for the right connections.
8. change directory to "WEbPage" folder and run "python app.py" to start the flask server.

