# sdc-console-python    

This application is written in Python and is called `sdc-console-python`, where `sdc` stands for *Self Driving Car*.

It is designed as a **console app** that allows you to simulate individual modules of the *sensor system of a self driving car* for different models of vehicle behavior (i.e. when it doesn't move, when it moves at a constant speed, or, for example, when it changes the angle of its movement).

This is done by entering the required commands through the **console**.

## Application modules

At the moment, several modules have been written:
- Kalman filter and Real-Time Locating System;
- Fuzzy controller;
- Neural networks for computer vision module.

### Kalman Filter and Real-Time Locating System

**Kalman filter** allows you to reduce *measurement error* and more accurately estimate the *true value* of the measured parameter based on previously measured values.

In the original version, the **Kalman filter** generated empirical data for a *GPS receiver*, processed this data, drew a graph of the dependence of measurements and calculations and output the calculation results to the console.

It should be noted that the **Kalman filter** was guided by the constant location of the car, and also *process variance* was a constant parameter.

Later, I divided the tasks that the **Kalman filter** performed between different modules and made it so that the *process variance* parameter changes its value with each iteration depending on the calculated *aposteri error* at the previous iteration ("the larger the error value at the previous iteration, the larger step we have to take in the current iteration to reduce this error").

This allowed the **Kalman filter** to be used to add models with *constant speed* and *random acceleration*, and to add a *gyroscope*.

### Fuzzy controller

In a general sense, **fuzzy controller** allows the car to adjust its speed according to the idea that if the pivot point is far away, then you can drive at a high speed, and if it's close, then the speed should be slowed down.

One of the ideas on how to teach a car to independently calculate the speed of its movement may be the following algorithm:
1. Set the starting and ending points of the path,
2. Estimate the location of the car at the current time and mark it on the map,
3. Using the map, calculate the distance that the car will drive in a straight line without turning,
4. Since almost any driver tries to slow down when cornering, it makes sense to teach a car the same (i.e. teach a car to think as a human being in this situation). 
You can copy this thinking model by using a **fuzzy controller**.
5. Determine the boundaries of such **terms** of the **linguistic variables** *distance* and *speed* as *close distance*, *far distance*, *low speed*, *high speed* etc. in numerical values,
2. Build rulebase in the following way: *"if the distance is close then speed should be low"* and *"if distance is far then speed should be high"* and so on,
3. Apply the **fuzzy inference algorithm** (the most used is the **Mamdani algorithm**).    

Thus, the **fuzzy controller** takes the distance to the next pivot point and returns the speed corresponding to that distance.

### Neural networks for computer vision module

A huge amount of information required for self driving car control system is visual (for example, *road markings*, *road signs* and *traffic signals*). 

Moreover, this kind of information can't be obtained using the so-called traditional measurement methods using *radar*, *lidar*, *GPS*, *gyroscope* and *accelerometer*. 

A well-established solution for **computer vision** is currently **neural networks**. So in this app I try to build my own neural networks for handwritten digits recognition and road signs recognition. 

## How to run this app
In order to run this app, you need to enter the following commands into your terminal: 
```
git clone https://github.com/alexeysp11/sdc-console-python.git
cd sdc-console-python/console 
python console.py
```

Then the app starts, and you get the following message: 
```
Welcome to SDC console!
>>
```
And you just need to write some commands described in the next section. 

## Commands
Now I'll briefly talk about the commands you can use in this application.

Commands are entered as follows:
```
app module --operation_mode
```

For example, if you need to simulate the *GPS* module, provided that the car is moving at a constant speed, then you need to enter:
```
sdc gps --v
```

If you need to simulate a *gyroscope* under the condition that the angle at which the car is moving is constant, then you should type: 
```
sdc gyro --const
``` 

Service modules are called as follows:
```
app -service_module
```

For example, 
```
sdc -commands
``` 
or
```
sdc -help
```

More information on commands you can be found by typing:
```
sdc
``` 
or 
```
sdc -commands
``` 

So you'll get the following message: 
```
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

In order to exit the app, just type: 
```
sdc exit
```