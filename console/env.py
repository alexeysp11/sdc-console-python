"""
Environment settings.
"""

def setting(mode, dim):
    if mode == 'p':
        if dim == 1:
            velocity = 0.0
        else:
            velocity = [0.0, 0.0]
        
        accel = False
    
    elif mode == 'v':
        if dim == 1:
            velocity = 2.0
        else:
            velocity = [2.0, 1.5]
        
        accel = False
    
    elif mode == 'a':
        if dim == 1:
            velocity = 2.5
        else: 
            velocity = [2.5, 4.5]
        
        accel = True

    return velocity, accel
