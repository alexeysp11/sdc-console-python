# sdc-console-python 
[Click here](https://github.com/alexeysp11/sdc-console-python/blob/master/README_RU.md) to read russian version of README file.    
This application is written in Python and is called `sdc-console-python`, where` sdc` stands for *Self Driving Car*.    
It is designed as a **console application** that allows you to simulate individual modules of the *sensor system of a self driving car* for different models of vehicle behavior (i.e. when it doesn't move, when it moves at a constant speed, or, for example, when it changes the angle of its movement).    
This is done by entering the required commands through the **console**.
## Application modules
At the moment, several modules have been written:
- Kalman filter and Real-Time Locating System,
- Fuzzy controller,
- A neural network for handwritten digit recognition.
### Kalman Filter and Real-Time Locating System
**Kalman filter** allows you to reduce *measurement error* and more accurately estimate the *true value* of the measured parameter based on previously measured values.    
In the original version, the **Kalman filter** generated empirical data for a *GPS receiver*, processed this data, drew a graph of the dependence of measurements and calculations and output the calculation results to the console.    
It should be noted that the **Kalman filter** was guided by the constant location of the car, and also *process variance* was a constant parameter.    
Later, I divided the tasks that the **Kalman filter** performed between different modules and made it so that the *process variance* parameter changes its value with each iteration depending on the calculated *aposteri error* at the previous iteration ("the larger the error value at the previous iteration, the larger step we have to take in the current iteration to reduce this error").    
This allowed the **Kalman filter** to be used to add models with *constant speed* and *random acceleration*, and to add a *gyroscope*.
### Fuzzy regulator
One of the ideas on how to teach a car to independently calculate the speed of its movement may be the following algorithm:
1. Set the starting and ending points of the path,
2. Estimate the location of the car at the current time and mark it on the map,
3. Using the map, calculate the distance that the car will drive in a straight line without turning,
4. Since almost any driver tries to slow down when cornering, it makes sense to teach a car the same (i.e. teach a car to think as a human being in this situation). 
You can copy this thinking model by using a **fuzzy controller**.    
In a general sense, **fuzzy controller** allows the car to adjust its speed according to the idea that if the pivot point is far away, then you can drive at a high speed, and if it's close, then the speed should be slowed down.
1. Determine the boundaries of such **terms** of the **linguistic variables** *distance* and *speed* as *"close distance"*, *"far distance"*, *"low speed"* and *"high speed"* in numerical values,
2. Build rulebase in the following way: *"if the distance is close then speed should be low"* and *"if distance is far then speed should be high"* and so on,
3. Apply the **fuzzy inference algorithm** (the most used is the **Mamdani algorithm**).    
Thus, the task of the **fuzzy controller** is to take the distance to the next pivot point and return the speed corresponding to that distance.
### Neural network for handwritten number recognition
A huge amount of information required for self driving car control system is visual (for example, *road markings*, *road signs* and *traffic signals*).    
Moreover, this kind of information cannot be obtained using the so-called traditional measurement methods using *radar*, *lidar*, *GPS*, *gyroscope* and *accelerometer*. A well-established solution for **computer vision** is currently **neural networks**.    
Now I only added a **neural network algorithm for recognizing handwritten numbers (MNIST)** to this app.
## Commands
Now I will briefly talk about the commands you can use in this application.
Commands are entered as follows:
```
app module --operation_mode
```
For example, if you need to simulate the *GPS* module, provided that the car is moving at a constant speed, then you need to enter `sdc gps --v`.    
If you need to simulate the operation of a *gyroscope* under the condition that the angle at which the car is moving is unchanged, then you should enter `sdc gyro --const`, etc.    
More information on commands you can be found by typing `sdc` or `sdc -commands`.    
Service modules are called as follows:
```
app -service_module
```
For example, `sdc -commands` or` sdc -help`.
