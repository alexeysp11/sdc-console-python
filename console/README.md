# console 
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
>> sdc -commands
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
>> sdc -help
SDC CONSOLE APP

SDC stands for Self-Driving Cars.
So this app allows you to simulate some modules of SDC within a console.

All modules can be called by:
    sdc module --mode

All information modules can be called by:
    sdc -commands
    sdc -help
```
```
>> sdc gps
sdc gps:
    --p             | GPS (position)
    --v             | GPS (velocity)
    --a             | GPS (acceleration)
```
```
>> sdc gyro
sdc gyro:
    --const         | Gyroscope (constant angle)
    --nu            | Gyroscope (non-uniform rotation)
```