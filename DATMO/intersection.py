"""
Line intersection
"""

def slope(P1, P2):
    # dy/dx
    # (y2 - y1) / (x2 - x1)
    return(P2[1] - P1[1]) / (P2[0] - P1[0])

def y_intercept(P1, slope):
    # y = mx + b
    # b = y - mx
    # b = P1[1] - slope * P1[0]
    return P1[1] - slope * P1[0]

def line_intersect(m1, b1, m2, b2):
    if m1 == m2:
        print ("These lines are parallel!!!")
        return None
    # y = mx + b
    # Set both lines equal to find the intersection point in the x direction
    # m1 * x + b1 = m2 * x + b2
    # m1 * x - m2 * x = b2 - b1
    # x * (m1 - m2) = b2 - b1
    # x = (b2 - b1) / (m1 - m2)
    x = (b2 - b1) / (m1 - m2)
    # Now solve for y -- use either line, because they are equal here
    # y = mx + b
    y = m1 * x + b1
    return x,y
    
if __name__ == '__main__': 
    A1 = [1,1]
    A2 = [3,3]
    B1 = [1,3]
    B2 = [3,1]
    
    slope_A = slope(A1, A2)
    slope_B = slope(B1, B2)
    y_int_A = y_intercept(A1, slope_A)
    y_int_B = y_intercept(B1, slope_B)
    print(line_intersect(slope_A, y_int_A, slope_B, y_int_B))
