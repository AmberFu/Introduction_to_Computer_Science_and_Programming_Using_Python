def polysum(n, s):
    '''
    n : number of sides, s : length.
    
    The area of a regular polygon is: (0.25*n*s^2)/tan(pi/n).
    
    The perimeter of a polygon is: length of the boundary of the polygon.
    
    This function should sum the area and square of the perimeter of the regular polygon.
    
    Returns the sum, rounded to 4 decimal places.
    '''
    
    import math
    
    area = round((0.25*n*math.pow(s,2))/math.tan(math.pi/n),4)
    perimeter = n*s
    result = area+math.pow(perimeter,2)
    
    return result