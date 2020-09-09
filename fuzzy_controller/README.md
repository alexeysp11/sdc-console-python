# fuzzy_controller
The **Fuzzy Controller** module is used for counting speed of a car according to the *distance* between it and *next* and *previous* points on the map.    
In this program we need to pass a value of distance to the input of the **fuzzy controller** and get a value of speed as an output. 
## How this module works
```
Welcome to SDC console!
>> sdc
SDC CONSOLE APP

SDC stands for Self-Driving Cars.
So this app allows you to simulate some modules of SDC within a console.

All modules can be called by:
    sdc module --mode

All information modules can be called by:
    sdc -commands
    sdc -help

Main modules:
    imu             | Inertial Measurement Unit (GPS, gyro, accelerometer)
    gps             | GPS
    gyro            | Gyroscope
    accel           | Accelerometer
    lidar           | Lidar
    fuzzy           | Fuzzy Controller
    nn              | Neural Network
    test            | Unit-tests for each module
    exit            | Exit
```
```
>> sdc fuzzy
Select one of these options:
            1) Enter distance and get speed once,
            2) Describe relationship between distance and speed in the graph.

Please, enter 1 or 2: 1
Distance (m): 14
Speed = 30.0 km/h
```
```
>> sdc fuzzy
Select one of these options:
            1) Enter distance and get speed once,
            2) Describe relationship between distance and speed in the graph.

Please, enter 1 or 2: 2
```