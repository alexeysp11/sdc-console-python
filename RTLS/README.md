# RTLS 
Here I implement and test different models of **Kalman filter**. 
## Sensors 
This module should simulate sensor observations of the values that has been generated in *env* module. 
## Predictive models
I'm going to use simple **Kalman filter** model that can change value of *process variance* depending on that how large *aposteri error* is.  
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
>> sdc gps
sdc gps:
    --p             | GPS (position)
    --v             | GPS (velocity)
    --a             | GPS (acceleration)
```
```
>> sdc gps --p
1-DIMENSIONAL SPACE
Default parameters (yes or no)? no
INITIAL DATA
Truth value: 450
Initial guess: 430
Velocity (m/s): 0.0
Time (sec): 40
Measures of central tendency of error:
median = 4.0, mean = 5.0
```
![sdc gps --p 1D](https://github.com/alexeysp11/sdc-console-python/blob/master/RTLS/img/sdc%20gps%20--p%20%201D.png)
```
2-DIMENSIONAL SPACE
Default parameters (yes or no)? yes
Real coordinates (at the beggining): (163.0, 55.0)
Initial coordinates: (152.0, 68.0)
Velocity_x: 0.0 m/s
Velocity_y: 0.0 m/s
Time (sec): 60
Measures of central tendency of error:
median_X = 12.683, mean_X = 12.665
median_Y = 8.382, mean_Y = 9.078
```
![sdc gps --p 2D](https://github.com/alexeysp11/sdc-console-python/blob/master/RTLS/img/sdc%20gps%20--p%20%202D.png)
```
>> sdc gps --v
1-DIMENSIONAL SPACE
Default parameters (yes or no)? y
Truth value: 45.0
Initial guess: 55.0
Velocity (m/s): 2.0
Time (sec): 50
Measures of central tendency of error:
median = 10.0, mean = 11.0
```
![sdc gps --v 2D](https://github.com/alexeysp11/sdc-console-python/blob/master/RTLS/img/sdc%20gps%20--v%20%201D.png)
```
2-DIMENSIONAL SPACE
Default parameters (yes or no)? no
INITIAL DATA
Truth value X: 43
Truth value Y: 27
Initial guess X: 30
Initial guess Y: 45
Velocity X (m/s): 3.2
Velocity Y (m/s): 1.7
Time (sec): 40
Measures of central tendency of error:
median_X = 9.112, mean_X = 12.966
median_Y = 7.239, mean_Y = 7.926
```
![sdc gps --v 2D](https://github.com/alexeysp11/sdc-console-python/blob/master/RTLS/img/sdc%20gps%20--v%20%202D.png)
```
>> sdc gps --a
1-DIMENSIONAL SPACE
Default parameters (yes or no)? yeah
Default parameters (yes or no)? y
Truth value: 45.0
Initial guess: 55.0
Velocity (m/s): 2.5
Time (sec): 50
Measures of central tendency of error:
median = 6.0, mean = 7.0
```
![sdc gps --a 1D](https://github.com/alexeysp11/sdc-console-python/blob/master/RTLS/img/sdc%20gps%20--a%20%201D.png)
```
2-DIMENSIONAL SPACE
Default parameters (yes or no)? y
Real coordinates (at the beggining): (163.0, 55.0)
Initial coordinates: (152.0, 68.0)
Velocity_x: 2.5 m/s
Velocity_y: 4.5 m/s
Time (sec): 60
Measures of central tendency of error:
median_X = 23.735, mean_X = 23.575
median_Y = 9.919, mean_Y = 11.518
```
![sdc gps --a 2D](https://github.com/alexeysp11/sdc-console-python/blob/master/RTLS/img/sdc%20gps%20--a%20%202D.png)