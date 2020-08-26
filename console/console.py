"""
CONSOLE APP
When this app starts, user can enter some commands (for gps, 
gyro, fuzzy controller, computer vision etc). 
When user writes some command, the program asks him or her 
if it's okay to use default parameters.

NOTES: 
- Divide commands into submodules (sdc gps -p, sdc gps -v, sdc gps -a; 
sdc gyro -s, sdc gyro -r). 
"""

import sys
sys.path.append('../RTLS')
sys.path.append('../DATMO')
import info
import input_data
from sensors.gps import GpsKF
from sensors.gyro import GyroKF
from lidar import Lidar


if __name__ == '__main__':
    print('Welcome to SDC console!')
    
    while True:
        command = input('>> ')
        

        if command == 'sdc -info':
            info.info()
        

        elif command == ('sdc -h' or 'sdc -help'):
            info.help()
        

        elif command == 'sdc gps':
            info.gps()


        elif command == 'sdc gps --v':
            velocity = 2.0

            kf_1d = GpsKF()
            init_data = input_data.custom_or_default_data(dimension=1, init_velocity=velocity)
            kf_1d.callkf(dimension=1, init_data=init_data)
            
            kf_2d = GpsKF()
            init_data = input_data.custom_or_default_data(dimension=2, init_velocity=velocity)
            kf_2d.callkf(dimension=2, init_data=init_data)
        

        elif command == 'sdc gps --p':
            velocity = 0.0

            kf_1d = GpsKF()
            init_data = input_data.custom_or_default_data(dimension=1, init_velocity=velocity)
            kf_1d.callkf(dimension=1, init_data=init_data)
            
            kf_2d = GpsKF()
            init_data = input_data.custom_or_default_data(dimension=2, init_velocity=velocity)
            kf_2d.callkf(dimension=2, init_data=init_data)
        

        elif command == 'sdc gps --a':
            velocity = 2.5

            kf_1d = GpsKF()
            init_data = input_data.custom_or_default_data(dimension=1, init_velocity=velocity, accel=True)
            kf_1d.callkf(dimension=1, init_data=init_data)
            
            kf_2d = GpsKF()
            init_data = input_data.custom_or_default_data(dimension=2, init_velocity=velocity, accel=True)
            kf_2d.callkf(dimension=2, init_data=init_data)
        

        elif command == 'sdc gyro':
            info.gyro()


        elif command == 'sdc gyro --c':
            gyro_1d = GyroKF()
            gyro_1d.callkf(dim=2)
        

        elif command == 'sdc gyro --nu':
            gyro_1d = GyroKF()
            gyro_1d.callkf(dim=2, const_rotation=False)


        elif command == 'sdc lidar':
            lidar = Lidar()
            lidar.call_lidar()
        

        elif command == 'sdc nn mnist':
            pass
        

        elif command == 'sdc exit':
            break
        