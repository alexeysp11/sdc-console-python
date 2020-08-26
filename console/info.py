"""
Info
"""

def info():
    print('''Information:
    imu         | inertial measurement unit (gps, accelerometer, gyro)
    gps         | gps 
    gyro        | gyroscope 
    lidar       | lidar
    fuzzy       | fuzzy controller 
    nn mnist    | neural network (mnist)
    test        | unit tests for each module
    exit        | exit 
    ''')


def help():
    pass


def gps(): 
    print('''sdc gps:
    --v     | gps (velocity)
    --p     | gps (position) 
    --a     | gps (acceleration)
    ''')


def gyro():
    print('''sdc gyro:
    --c     | gyro (constant)
    --nu    | gyro (non-uniform) 
    ''')
