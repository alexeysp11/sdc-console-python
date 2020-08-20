"""
Add position, computer vision, fuzzy controller and Car2D modules.
"""

import sys
sys.path.append('../RTLS')
sys.path.append('../DATMO')
import info
from sensors.gps import GpsKF
from sensors.gyro import GyroKF
from lidar import Lidar


if __name__ == '__main__':
    print('Welcome to SDC console!')
    
    while True:
        command = input('>> ')
        
        if command == 'sdc -info':
            info.info()
        
        elif command == 'sdc gps':
            plot = True
            
            # enter custom position, speed and time!
            
            kf_1d = GpsKF()
            kf_1d.callkf(plot=plot, dimension=1)
            
            kf_2d = GpsKF()
            kf_2d.callkf(plot=plot, dimension=2)
        
        elif command == 'sdc position':
            velocity = 0 
            
            # then you need to pass velocity to GpsKF
            kf_1d = GpsKF()
            kf_1d.callkf(plot=plot, dimension='1D', velocity=0)
            
            kf_2d = GpsKF()
            kf_2d.callkf(plot=plot, dimension='2D', velocity=0)
        
        elif command == 'sdc accel':
            kf_1d = GpsKF()
            kf_1d.callkf(dimension=1, accel=True)
            
            kf_2d = GpsKF()
            kf_2d.callkf(dimension=2, accel=True)
        
        elif command == 'sdc gyro':
            gyro_1d = GyroKF()
            gyro_1d.callkf(dim=2)
        
        elif command == 'sdc gyro dif':
            gyro_1d = GyroKF()
            gyro_1d.callkf(dim=2, const_rotation=False)

        elif command == 'sdc lidar':
            lidar = Lidar()
            lidar.call_lidar()
        
        elif command == 'sdc nn mnist':
            pass
        
        elif command == 'sdc exit':
            break
        