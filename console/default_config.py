

def setting(mode, dim):
    """
    Set default configurations for GPS module.
    """
    if mode == 'p':
        if dim == 1:
            velocity = 0.0
        else:
            velocity = [0.0, 0.0]
        
        is_accel = False
    
    elif mode == 'v':
        if dim == 1:
            velocity = 2.0
        else:
            velocity = [2.0, 1.5]
        
        is_accel = False
    
    elif mode == 'a':
        if dim == 1:
            velocity = 2.5
        else: 
            velocity = [2.5, 4.5]
        
        is_accel = True

    return velocity, is_accel
