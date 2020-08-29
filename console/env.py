"""
Environment settings.
"""

def setting(mode):
    if mode == 'p':
        velocity = 0.0
        accel = False
    elif mode == 'v':
        velocity = 2.0
        accel = False
    elif mode == 'a':
        velocity = 2.5
        accel = True

    return velocity, accel
