"""
Info
"""

def info():
    print('''Information about modules:
    imu         | inertial measurement unit (gps, accelerometer, gyro)
    gps         | gps 
    gyro        | gyroscope 
    lidar       | lidar
    fuzzy       | fuzzy controller 
    nn --mnist  | neural network (mnist)
    test        | unit tests for each module
    exit        | exit 
    ''')


def help():
    print('''SDC CONSOLE APP

SDC stands for Self-Driving Cars. 
So this app allows you to simulate some modules of SDC within a console.

All modules can be called by:
sdc module --mode

All information modules can be called by:
sdc -info
sdc -help
    ''')


def gps(): 
    print('''sdc gps:
    --p     | gps (position) 
    --v     | gps (velocity)
    --a     | gps (acceleration)
    ''')


def gyro():
    print('''sdc gyro:
    --c     | gyro (constant)
    --nu    | gyro (non-uniform) 
    ''')
