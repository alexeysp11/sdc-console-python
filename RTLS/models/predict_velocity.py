"""
VELOCITY ESTIMATING. 

Velovity can be measured by GPS (velocity = distance / time), by speedometer 
or pridicted by formula of speed and acceleration relying on accelerometer data 
(velocity = acceleration * time).

So in this module we need to import 1) time module, 2) module that measures 
or generates acceleration data and 3) position data estimated by KF devided 
by time (velocity = (pos_2 - pos_1) / time). 

In this module speed is measured in meters per second. 
Because of that we have speed limit 60 kmh, the speed of vehicle should be less 
than 16.67 m/s. 
So we can get necessary speed limit in kmh from another module and transfer the 
value of speed in kmh into m/s by following formula: 
speed_limit = speed_limit_kmh / 3.6. 

When we get estimation of velocity in this module, we can pass its value to the 
KF prepocessing module where we estimate truth_value and invoke KF module. 

I do not know if it is necessary to invoke KF several times when we can pass all 
data to the KF module and process it there. 
I guess the problem is that all sensors have different frequency and we cannot 
pass all data to the KF without prepocessing. 
"""