"""
CONSOLE APP
When this app starts, user can enter some commands (for gps, 
gyro, fuzzy controller, computer vision etc). 
When user writes some command, the program asks him or her 
if it's okay to use default parameters.

All modules can be called by:
    sdc module --mode
All information can be called by:
    sdc -info
    sdc -help
"""

import os
import sys
import info
import invoke

if __name__ == '__main__':
    print()
    print('Welcome to SDC console!')
    
    while True:
        try:
            command = input('>> ')
            
            # ignore if user just pressed Enter
            if command == '':
                pass
            
            elif command == 'sdc':
                info.help()
                info.commands()

            elif command == 'sdc -commands':
                info.commands()
            
            elif command == 'sdc -h' or command == 'sdc -help':
                info.help()
            
            elif command == 'sdc imu':
                info.imu()
            
            elif command == 'sdc imu --p':
                invoke.imu(mode='p')

            elif command == 'sdc imu --v':
                invoke.imu(mode='v')
            
            elif command == 'sdc imu --a':
                invoke.imu(mode='a')

            elif command == 'sdc gps':
                info.gps()

            elif command == 'sdc gps --p':
                invoke.gps(mode='p')

            elif command == 'sdc gps --v':
                invoke.gps(mode='v')
            
            elif command == 'sdc gps --a':
                invoke.gps(mode='a')
            
            elif command == 'sdc accel':
                invoke.accel()
            
            elif command == 'sdc gyro':
                info.gyro()

            elif command == 'sdc gyro --const':
                invoke.gyro(mode='c')
            
            elif command == 'sdc gyro --nu':
                invoke.gyro(mode='nu')

            elif command == 'sdc lidar':
                invoke.lidar()
            
            elif command == 'sdc nn':
                info.neural_network()

            elif command == 'sdc nn --mnist default':
                invoke.neural_network(mode='mnist', default=True)
            
            elif command == 'sdc nn --mnist custom':
                invoke.neural_network(mode='mnist', default=False)
            
            elif command == 'sdc nn --signs':
                invoke.neural_network(mode='signs', default=True)
            
            elif command == 'sdc fuzzy':
                invoke.fuzzy()

            elif command == 'sdc exit':
                sys.exit()
            
            else:
                print('Incorrect command!')
        
        except Exception as e:
            print('Info for developer:'.upper)
            print(e)
