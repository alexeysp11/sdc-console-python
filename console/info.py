"""
Info
"""

def info():
    print('''Information:
    imu         | inertial measurement unit (gps, accelerometer, gyro)
    gps         | gps (constant velocity)
    position    | gps (constant position) 
    accel       | gps (acceleration)
    gyro        | gyroscope (constant rotation)
    gyro dif    | gyroscope (non-constant rotation)
    lidar       | lidar
    fuzzy       | fuzzy controller 
    nn mnist    | neural network (mnist)
    test        | unit tests for each module
    exit        | exit 
    ''')


def gps(): 
    print('''gps module:
    velocity    | gps (non-constant velocity)
    position    | gps (constant velocity) 
    ''')


def gyro():
    pass
