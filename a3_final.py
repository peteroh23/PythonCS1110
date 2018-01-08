""" 
Functions for Assignment A3

This file contains the functions for the assignment.  You should replace the stubs
with your own implementations.

Magd Bayoumi mb2363
Junghwan (Peter) Oh jo299
October 2, 2017
"""
import cornell
import math


def complement_rgb(rgb):
    """
    Returns: the complement of color rgb.
    
    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object
    """
    
    complement = cornell.RGB(0,0,0)

    complement.red = 255 - rgb.red
    complement.green = 255 - rgb.green
    complement.blue = 255 - rgb.blue
    

    return complement


def round(number, places):
    """
    Returns: the number rounded to the given number of decimal places.
    
    The value returned is a float.
    
    This function is more stable than the built-in round.  The built-in round
    has weird behavior where round(100.55,1) is 100.5 while round(100.45,1) is
    also 100.5.  We want to ensure that anything ending in a 5 is rounded UP.
    
    It is possible to write this function without the second precondition on
    places. If you want to do that, we leave that as an optional challenge.
    
    Parameter number: the number to round to the given decimal place
    Precondition: number is an int or float
    
    Parameter places: the decimal place to round to
    Precondition: places is an int; 0 <= places <= 3
    """
    # To get the desired output, do the following
    #   1. Shift the number "to the left" so that the position to round to is left of 
    #      the decimal place.  For example, if you are rounding 100.556 to the first 
    #      decimal place, the number becomes 1005.56.  If you are rounding to the second 
    #      decimal place, it becomes 10055.6.  If you are rounding 100.556 to the nearest 
    #      integer, it remains 100.556.
    #   2. Add 0.5 to this number
    #   3. Convert the number to an int, cutting it off to the right of the decimal.
    #   4. Shift the number back "to the right" the same amount that you did to the left.
    #      Suppose that in step 1 you converted 100.556 to 1005.56.  In this case, 
    #      divide the number by 10 to put it back.
    if places == 0:
        return int(number * (1) + 0.5)
    else:
        return int(number * (10**places) + 0.5) / (10**places)


def str5(value):
    """
    Returns: value as a string, but expand or round to be exactly 5 characters.
    
    The decimal point counts as one of the five characters.
   
    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.
    
    Parameter value: the number to conver to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    # Note:Obviously, you want to use the function round() that you just defined. 
    # However, remember that the rounding takes place at a different place depending 
    # on how big value is. Look at the examples in the specification.
    
    # Add decimal for int values
    value = float(value)
    # Find places after decimal
    decimal = str(value).index('.')
    # Max number of places after the decimal is 4, 
    #places after decimal depend on numbers before
    places = 4 - decimal
    # Get the rounded value 
    num = round(value,(places))
    # Convert to String
    string1 = str(num)
    # Return the string
    
    # Numbers such as "22.00" or "1.000" are not valid floats
    # need to add "0"s to the end
    if len(string1) < 5:
        string1 = string1 + '0'*(5-len(string1))
    
    return string1     # Stub


def str5_cmyk(cmyk):
    """
    Returns: String representation of cmyk in the form "(C, M, Y, K)".
    
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    
    Example: if str(cmyk) is 
    
          '(0.0,31.3725490196,31.3725490196,0.0)'
    
    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter cmtk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    """
    return "({cyan}, {magenta}, {yellow}, {black})".format(cyan=str5(cmyk.cyan),
     magenta=str5(cmyk.magenta),yellow=str5(cmyk.yellow),black=str5(cmyk.black))


def str5_hsv(hsv):
    """
    Returns: String representation of hsv in the form "(H, S, V)".
    
    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)
    
    Example: if str(hsv) is 
    
          '(0.0,0.313725490196,1.0)'
    
    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object.
    """
    return "({hue}, {saturation}, {value})".format(hue=str5(hsv.hue), 
        saturation=str5(hsv.saturation), value=str5(hsv.value))


def rgb_to_cmyk(rgb):
    """
    Returns: color rgb in space CMYK, with the most black possible.

    Formulae from en.wikipedia.org/wiki/CMYK_color_model.

    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change the RGB numbers to the range 0..1 by dividing them by 255.0.

    #Initial Varibles
    red = rgb.red
    green = rgb.green
    blue = rgb.blue

    red_1 = red/ 255.0
    green_1 = green/255.0
    blue_1 = blue/255.0

    C_1 = 1-red_1
    M_1 = 1-green_1
    Y_1 = 1 -blue_1
    K_1 = 0

    #Determing K value
    if (C_1 ==1 and M_1 ==1 and Y_1 ==1):
        K_1= 1

    if (C_1 <= M_1 and C_1 <= Y_1):
        K_1 = C_1

    if (M_1 <= C_1 and M_1 <= Y_1):
        K_1 = M_1

    if (Y_1 <= M_1 and Y_1 <= C_1):
        K_1 = Y_1

    #Changing CMY values based on new K
    if (K_1 ==1):
        C_1 = 0
        M_1 = 0
        Y_1 = 0

    if (K_1 != 1):
        C_2 = (C_1 - K_1)/(1 -K_1)
        M_2 = (M_1 - K_1)/(1 -K_1)
        Y_2 = (Y_1-K_1)/(1-K_1)

    #Converting CMYK values to proper range
    if (K_1 ==1):
        C_3 = C_1 *100
        M_3 = M_1 *100
        Y_3 = Y_1 *100
        K_3 = K_1 *100

    if(K_1 != 1):
        C_3 = C_2 *100
        M_3 = M_2 *100
        Y_3 = Y_2 *100
        K_3 = K_1 * 100

    #Return CMYK Object
    return cornell.CMYK(C_3, M_3, Y_3, K_3)



def cmyk_to_rgb(cmyk):
    """
    Returns : color CMYK in space RGB.

    Formulae from en.wikipedia.org/wiki/CMYK_color_model.

    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    # The CMYK numbers are in the range 0.0..100.0.  Deal with them in the
    # same way as the RGB numbers in rgb_to_cmyk()

    # Initial Values/Variables
    C = cmyk.cyan
    M =cmyk.magenta
    Y = cmyk.yellow
    K = cmyk.black

    #Changing the range of the CMYK Numbers to 0.0 ..1.0
    C_1 = C /100
    M_1 = M/100
    Y_1 = Y/100
    K_1 = K/100

    #Conversion to RGB values
    R = (1-C_1)*(1-K_1)
    G = (1-M_1)*(1-K_1)
    B = (1-Y_1)*(1-K_1)

    # Changing range of RGB to 0 ..255, Rounding involved
    R_1 = round(R*255,0)
    G_1 = round(G*255,0)
    B_1 = round(B*255,0)

    #Converting to int
    R_2 = int(R_1)
    G_2 = int(G_1)
    B_2 = int(B_1)

    #Return new RGB object
    return cornell.RGB(R_2, G_2, B_2)


def rgb_to_hsv(rgb):
    """
    Return: color rgb in HSV color space.
    
    Formulae from wikipedia.org/wiki/HSV_color_space.
   
    Parameter rgb: the color to convert to a HSV object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.
    r = rgb.red/255.0
    g = rgb.green/255.0
    b = rgb.blue/255.0

    MAX = max(r,g,b)
    MIN = min(r,g,b)

    if MAX == MIN:
        h = 0
    elif MAX == r and g >=b:
        h = 60.0 * (g - b) / (MAX-MIN)
    elif MAX == r and g < b:
        h = 60.0 * (g - b) / (MAX-MIN)+360.0
    elif MAX == g:
        h = 60.0 * (b-r) / (MAX-MIN)+120.0
    else:
        h = 60.0 * (r-g) / (MAX-MIN)+240.0
    
    if MAX == 0:
        s = 0
    else:
        s = 1 - (MIN/MAX)

    v = MAX

    hsv = cornell.HSV(h,s,v)

    return hsv


def hsv_to_rgb(hsv):
    """
    Returns: color in RGB color space.
    
    Formulae from http://en.wikipedia.org/wiki/HSV_color_space.
    
    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object.
    """

    h = hsv.hue
    s = hsv.saturation
    v = hsv.value

    h_i = math.floor(h/60)
    f = h/60 - h_i
    p = v*(1-s)
    q = v*(1-f*s)
    t = v*(1-(1-f)*s)
    
    if h_i == 0:
        r = v
        g = t
        b = p
    elif h_i == 1:
        r = q
        g = v
        b = p
    elif h_i == 2:
        r = p
        g = v
        b = t
    elif h_i == 3:
        r = p
        g = q
        b = v
    elif h_i == 4:
        r = t
        g = p
        b = v
    elif h_i == 5:
        r = v
        g = p
        b = q

    r = round(r*255,0)
    g = round(g*255,0)
    b = round(b*255,0)

    rgb = cornell.RGB(r,g,b)    

    return rgb
