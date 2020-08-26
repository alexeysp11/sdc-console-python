"""
CONSOLE APP
When this app starts, user can enter some commands (for gps, 
gyro, fuzzy controller, computer vision etc). 
When user writes some command, the program asks him or her 
if it's okay to use default parameters.
"""

import info
import invoke

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
            invoke.gps(mode='v')
        
        elif command == 'sdc gps --p':
            invoke.gps(mode='p')
        
        elif command == 'sdc gps --a':
            invoke.gps(mode='a')
        
        elif command == 'sdc gyro':
            info.gyro()

        elif command == 'sdc gyro --c':
            invoke.gyro(mode='c')
        
        elif command == 'sdc gyro --nu':
            invoke.gyro(mode='nu')

        elif command == 'sdc lidar':
            invoke.lidar()
        
        elif command == 'sdc nn mnist':
            pass
        
        elif command == 'sdc fuzzy':
            pass

        elif command == 'sdc exit':
            break
