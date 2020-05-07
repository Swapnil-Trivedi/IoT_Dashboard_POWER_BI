# IoT_Dashboard_POWER_BI
A simple attempt to make an IoT Dashboard using POWER BI Arduino and  Python programming. 
The Project is meant to show smart Garbage Monitoring system.

## INTRODUCTION
The project aims on making a smart Garbage Monitoring system with the help of IoT and POWER BI

### Contents

- ARDUINO_PROG.ino file contains the program required to run the arduino code with an ULTRASONIC sensor
- Upload_script.py file is used to upload data to Power BI API to our Dashboard
- Screenshots folder have the necessary output screens and a video describing the working of our BI Dashboard
## Understanding the Project
There is a complete pdf showing the complete description of the project.
But here i'll try to keep it short and go through everything i did in the two files above.

### What we need to do ??
The plan here is simple, we need to make a smart monitoring system that can alert us when our "trash can" is  empty or in general just the  capacity of the can at the moment.
##### so how do i plan to do it you might think ????
well it's pretty simple all we need is some couple of electronics and we're good to go.

#### COMPONENTS
first of all we need something that can tell us the depth of our can or the distance a layer of proximity sensors or a weight sensor could help but let just keep it simple.
also a way to process the data from our sensor so a conroller and some more things.
so our list in the end looks omething like this :
- Arduino UNO
- Ultrasonic Sensor HC-SR04
- A pizeo Buzzer (to make things irritating)
- couple of jumper wires (M-F) and (M-M) pairs
- Breadboard 
- And our serial cable for Arduino

so this list won't help without a layout for the connecctions. so let's draw !!!
well this is what our circuit looks like
![](screenshots/circuit_layout.png)

now if you have ever worked with an arduino earlier you know that the circuit without a source code for the controller is well garbage!!!
so let's get our head into some coding the code source file is [ARDUINO_PROG.ino](/ARDUINO_PROG.ino) it's simple c++ but let me explain the process.

