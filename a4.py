"""
A module to draw cool shapes with the Tk Turtle.

The module can be run as a script to show off the various functions. Unimplemented 
functions will do nothing.

YOUR NAME(S) AND NETID(S) HERE
DATE COMPLETED HERE
"""

import cornell
import math


################# Helpers for Precondition Verification #################

def is_number(x):
    """
    Returns: True if value x is a number; False otherwise.
    
    Parameter x: the value to check
    Precondition: NONE (x can be any value)
    """
    return type(x) in [float, int]


def is_window(w):
    """
    Returns: True if w is a cornell Window; False otherwise.
    
    Parameter w: the value to check
    Precondition: NONE (w can be any value)
    """
    return type(w) == cornell.Window


def is_valid_color(c):
    """
    Returns: True c is a valid turtle color; False otherwise
    
    Parameter c: the value to check
    Precondition: NONE (c can be any value)
    """
    from cornell.colors.tkcolor import is_tkcolor
    return (type(c) == cornell.RGB or type(c) == cornell.HSV or
            (type(c) == str and is_tkcolor(c)))


def is_valid_speed(sp):
    """
    Returns: True if sp is an int in range 0..10; False otherwise.
    
    Parameter sp: the value to check
    Precondition: NONE (sp can be any value)
    """
    return (type(sp) == int and 0 <= sp and sp <= 10)


def is_valid_length(side):
    """
    Returns: True if side is a number >= 0; False otherwise.
    
    Parameter side: the value to check
    Precondition: NONE (side can be any value)
    """
    return (is_number(side) and 0 <= side)


def is_valid_iteration(n):
    """
    Returns: True if n is an int >= 1; False otherwise.
    
    Parameter n: the value to check
    Precondition: NONE (n can be any value)
    """
    return (type(n) == int and 1 <= n)


def is_valid_depth(d):
    """
    Returns: True if d is an int >= 0; False otherwise.
    
    Parameter d: the value to check
    Precondition: NONE (d can be any value)
    """
    return (type(d) == int and d >= 0)


def is_valid_turtlemode(t):
    """
    Returns: True t is a Turtle with drawmode True; False otherwise.
    
    Parameter t: the value to check
    Precondition: NONE (t can be any value)
    """
    return (type(t) == cornell.Turtle and t.drawmode)


def is_valid_penmode(p):
    """
    Returns: True t is a Pen with fill False; False otherwise.
    
    Parameter p: the value to check
    Precondition: NONE (p can be any value)
    """
    return (type(p) == cornell.Pen and not p.fill)


def report_error(message, value):
    """
    Returns: An error message about the given value.
    
    This is a function for constructing error messages to be used in assert statements.  
    We find that students often introduce bugs into their assert statement messages, and 
    do not find them because they are in the habit of not writing tests that violate 
    preconditions.
    
    The purpose of this function is to give you an easy way of making error messages 
    without having to worry about introducing such bugs. Look at the function 
    draw_two_lines for the proper way to use it.
    
    Parameter message: The error message to display
    Precondition: message is a string
    
    Parameter value: The value that caused the error
    Precondition: NONE (value can be anything)
    """
    return message+': '+repr(value)



#################### DEMO: Two lines ####################


def draw_two_lines(w,sp):
    """
    Draws two lines on to window w.
    
    In the middle of the window w, this function draws a green line 100 pixels to the 
    west, and then a red line 200 pixels to the south.  It uses a new turtle that moves 
    at speed sp, 0 <= sp <= 10, with 1 being slowest and 10 fastest (and 0 being "instant").
    
    Parameter w: The window to draw upon.
    Precondition: w is a cornell Window object.
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    # Assert the preconditions
    assert is_window(w), report_error('w is not a valid window',w)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)
    
    t = cornell.Turtle(w)
    t.speed = sp
    t.color = 'green'
    t.forward(100) # draw a line 100 pixels in the current direction
    t.left(90)     # add 90 degrees to the angle
    t.color = 'red'
    t.forward(200)




#################### TASK 1: Triangle ####################

def draw_triangle(t, s, c):
    """
    Draws an equilateral triangle of side s and color c at currenct position.
    
    The direction of the triangle depends on the current facing of the turtle.
    If the turtle is facing west, the triangle points up and the turtle starts
    and ends at the east end of the base line.
    
    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    position (x and y, within round-off errors), heading, color, and drawmode.
    If you changed any of these in the function, you must change them back.
    
    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter s: The length of each triangle side
    Precondition: s is a valid side length (number >= 0)
    
    Parameter c: The triangle color
    Precondition: c is a valid turtle color (see the helper function above)
    """
    # Assert the preconditions
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(s), report_error('Invalid side length', s)
    assert is_valid_color(c), report_error('Invalid color', c)
    
    # Hint: each angle in an equilateral triangle is 60 degrees.
    # Note: In this function, DO NOT save the turtle position and heading
    # in the beginning and then restore them at the end. The turtle moves
    # should be such that the turtle ends up where it started and facing
    # in the same direction, automatically.

    t.color = c
    for x in range(3):
        t.forward(s)
        t.right(120)
    t.color = 'red'

    # Also, 3 lines have to be drawn. Does this suggest a for loop that
    # processes the range 0..2?




#################### TASK 2: Hexagon ####################

def draw_hex(t, s):
    """
    Draws six triangles using the color 'orange' to make a hexagon.
    
    The triangles are equilateral triangles, using draw_triangle as a helper.
    The drawing starts at the turtle's current position and heading. The
    middle of the hexagon is the turtle's starting position.
    
    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    position (x and y, within round-off errors), heading, color, and drawmode.
    If you changed any of these in the function, you must change them back.
    
    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter s: The length of each triangle side
    Precondition: s is a valid side length (number >= 0)
    """
    # Assert the preconditions
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(s), report_error('Invalid side length', s)

    # Note: Do not save any of the turtle's properties and then restore them
    # at the end. Just use 6 calls on procedures drawTriangle and t.left. Test
    # the procedure to make sure that t's final location and heading are the
    # same as t's initial location and heading (except for roundoff error).
    
    # The procedure is supposed to draw 6 triangles. Does that suggest a loop
    # that processes the integers in 0..5?
    for i in range(6):
        draw_triangle(t,s,'orange')
        t.left(60)




#################### Task 3A: Spirals ####################

def draw_spiral(w, side, ang, n, sp):
    """
    Draws a spiral using draw_spiral_helper(t, side, ang, n, sp)
    
    This function clears the window and makes a new turtle t.  This turtle
    starts in the middle of the canvas facing east (NOT the default west).
    It then calls draw_spiral_helper(t, side, ang, n, sp). When it is done,
    the turtle is left hidden (visible is False).
    
    Parameter w: The window to draw upon.
    Precondition: w is a cornell Window object.
    
    Parameter side: The length of each spiral side
    Precondition: side is a valid side length (number >= 0)
    
    Parameter ang: The angle of each corner of the spiral
    Precondition: ang is a number
    
    Parameter n: The number of edges of the spiral
    Precondition: n is a valid number of iterations (int >= 1)
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_window(w), report_error('w is not a valid window', w)
    assert is_valid_length(side), report_error('side is not a valid length', side)
    assert is_valid_iteration(n), report_error('n is not a valid number of iterations', n)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)
    assert is_number(ang), report_error('ang is not a number', ang)
    
    # HINT: w.clear() clears window.
    # HINT: set the turtle's visible attribute to False at the end.
    w.clear()
    t = cornell.Turtle(w)
    t.speed = sp
    t.heading = 0
    draw_spiral_helper(t, side, ang, n, sp)
    t.visible = False


def draw_spiral_helper(t, side, ang, n, sp):
    """
    Draws a spiral of n lines at the current position and heading.
    
    The spiral begins at the current turtle position and heading, turning ang
    degrees to the left after each line.  Line 0 is side pixels long. Line 1
    is 2*side pixels long, and so on.  Hence each Line i is (i+1)*side pixels
    long. The lines alternate between blue, red, and green, in that order, with
    the first one blue.
    
    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED:
    color, speed, visible, and drawmode. However, the final position and
    heading may be different. If you changed any of these four in the function,
    you must change them back.
    
    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter side: The length of each spiral side
    Precondition: side is a valid side length (number >= 0)
    
    Parameter ang: The angle of each corner of the spiral
    Precondition: ang is a number
    
    Parameter n: The number of edges of the spiral
    Precondition: n is a valid number of iterations (int >= 1)
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert is_valid_iteration(n), report_error('n is not a valid number of iterations', n)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)
    assert is_number(ang), report_error('ang is not a number', ang)

    # NOTE: Since n lines must be drawn, use a for loop on a range of integers.
    side2 = side
    for x in range(1,n+1):
        if x%3 == 2:
            t.color = 'red'
        elif x%3 == 1:
            t.color = 'blue'
        else:
            t.color = 'green'

        side2 = side*x
        t.forward(side2)
        t.left(ang)

    t.color = 'red'

#################### TASK 3B: Polygons ####################


def multi_polygons(w, side, k, n, sp):
    """
    Draws polygons using multi_polygons_helper(t, side, k, n, sp)
    
    This function clears the window and makes a new turtle t.  This turtle starts in the 
    middle of the canvas facing north (NOT the default west). It then calls 
    multi_polygons_helper(t, side, k, n, sp). When it is done, the turtle is left 
    hidden (visible is False).
    
    Parameter w: The window to draw upon.
    Precondition: w is a cornell Window object.
    
    Parameter side: The length of each polygon side
    Precondition: side is a valid side length (number >= 0)
    
    Parameter k: The number of polygons to draw
    Precondition: k is an int >= 1
    
    Parameter n: The number of sides of each polygon
    Precondition: n is an int >= 1
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_window(w), report_error('w is not a valid window',w)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)
    assert (n >= 1 and type(n) == int), report_error('n is an invalid n argument', n)
    assert is_valid_iteration(k), report_error('k is an invalid number-of-iterations arg',k)
    
    # HINT: w.clear() clears window.
    # HINT: set the turtle's visible attribute to False at the end.
    w.clear()
    t = cornell.Turtle(w)
    t.speed = sp
    t.heading = 90
    multi_polygons_helper(t, side, k, n, sp)
    t.visible = False


def multi_polygons_helper(t, side, k, n, sp):
    """
    Draws k n-sided polygons of side length s.
    
    The polygons are drawn by turtle t, starting at the current position. The turtles 
    alternate colors between red and green. Each polygon is drawn starting at the same 
    place (within roundoff errors), but t turns left 360.0/k degrees after each polygon.
    
    At the end, ALL ATTRIBUTES of the turtle are the same as they were in the beginning 
    (within roundoff errors).  If you change any attributes of the turtle. then you must 
    restore them.  Look at the helper draw_polygon for more information.
    
    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter side: The length of each polygon side
    Precondition: side is a valid side length (number >= 0)
    
    Parameter k: The number of polygons to draw
    Precondition: k is an int >= 1
    
    Parameter n: The number of sides of each polygon
    Precondition: n is an int >= 1
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)
    assert n >= 1 and type(n) == int, report_error('n is an invalid n argument', n)
    assert is_valid_iteration(k), report_error('k is an invalid number-of-iterations arg',k)
    
    # HINT:  make sure that upon termination, t's color and speed are restored
    # HINT: since k polygons should be drawn, use a for-loop on a range.
    for i in range(1,k+1):
        if i % 2 == 0:
            t.color = 'green'
        else:
            t.color = 'red'
        draw_polygon(t,side,n,sp)
        t.left(360/k)


# DO NOT MODIFY
def draw_polygon(t, side, n, sp):
    """
    Draws an n-sided polygon using of side length side.
    
    The polygon is drawn with turtle t using speed sp.
    
    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED: position 
    (x and y, within round-off errors), heading, color, speed, visible, and drawmode.  
    There is no need to restore these.

    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter side: The length of each polygon side
    Precondition: side is a valid side length (number >= 0)
    
    Parameter n: The number of sides of each polygon
    Precondition: n is an int >= 1
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    # Assert the preconditions
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert (type(n) == int and n >= 3), report_error('n is an invalid # of poly sides',n)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)
    
    # Remember old speed
    oldspeed = t.speed
    t.speed = sp
    ang = 360.0/n # exterior angle between adjacent sides
    
    # t is in position and facing the direction to draw the next line.
    for _ in range(n):
        t.forward(side)
        t.left(ang)
    
    # Restore the speed
    t.speed = oldspeed




#################### TASK 3C: Radiating lines ####################

def radiate(w, side, n, sp):
    """
    Draws n straight radiating lines using radiate_helper(t, side, n, sp)
    
    This function clears the window and makes a new turtle t.  This turtle starts in the 
    middle of the canvas facing east (NOT the default west). It then calls 
    radiate_helper(t, side, n, sp). When it is done, the turtle is left hidden 
    (visible is False).
    
    Parameter w: The window to draw upon.
    Precondition: w is a cornell Window object.
    
    Parameter side: The length of each radial line
    Precondition: side is a valid side length (number >= 0)
    
    Parameter n: The number of lines to draw
    Precondition: n is an int >= 2
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_window(w), report_error('w is not a valid window',w)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)
    assert (type(n) == int and n >= 2), report_error('n is an invalid # of lines to draw',n)
    # HINT: w.clear() clears window.
    # HINT: set the turtle's visible attribute to False at the end.
    w.clear()
    t = cornell.Turtle(w)
    t.speed = sp
    t.heading = 0
    radiate_helper(t, side, n, sp)
    t.visible = False
    


def radiate_helper(t, side, n, sp):
    """
    Draws n straight radiating lines of length s at equal angles.
    
    This lines are drawn using turtle t with the turtle moving at speed sp.
    A line drawn at angle ang, 0 <= ang < 360 has HSV color (ang % 360.0, 1, 1).
    
    WHEN DONE, THE FOLLOWING TURTLE ATTRIBUTES ARE THE SAME AS IT STARTED: color, speed, 
    visible, and drawmode. However, the final position and heading may be different. If 
    you changed any of these four in the function, you must change them back.
    
    Parameter t: The drawing Turtle
    Precondition: t is a Turtle with drawmode True.
    
    Parameter side: The length of each radial line
    Precondition: side is a valid side length (number >= 0)
    
    Parameter n: The number of lines to draw
    Precondition: n is an int >= 2
    
    Parameter sp: The turtle speed.
    Precondition: sp is a valid turtle speed.
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_valid_turtlemode(t), report_error('Invalid turtle mode', t)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert is_valid_speed(sp), report_error('sp is not a valid speed',sp)
    assert (type(n) == int and n >= 2), report_error('n is an invalid # of lines to draw',n)
    # Notes:
    # 1. Drawing n lines should be done with a loop that processes
    #    a certain range of integers.
    # 2. You should keep the heading of the turtle in the range
    #    0 <= heading < 360.
    # 3. (t.heading % 360.0, 1, 1) is an HSV representation of the color
    #    determined by turtle t's heading.
    # 4. You can use an HSV object for the turtle's color attribute,
    #    even though all the examples use strings with color names
    t.heading = 0
    for i in range(1,n+1):
        t.color = (cornell.HSV(t.heading%360, 1, 1))
        t.forward(side)
        t.backward(side)
        t.left(360.0/n)

    t.color = 'red'




#################### Task 4A: Sierpinski Triangle ####################

def triangle(w, side, d):
    """
    Draws a Sierpinski triangle with the given side length and depth d.
    
    This function clears the window and makes a new graphics pen p.  This pen starts in 
    the middle of the canvas at (0,0). It draws by calling the function 
    triangle_helper(p, 0, 0, side, d). The pen is visible during drawing and should set 
    to hidden at the end.
    
    The pen should have both a 'magenta' fill color and a 'magenta' line color.
    
    Parameter w: The window to draw upon.
    Precondition: w is a cornell Window object.
    
    Parameter side: The side length of the triangle
    Precondition: side is a valid side length (number >= 0)
    
    Parameter d: The recursive depth of the triangle
    Precondition: n is a valid depth (int >= 0)
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_window(w), report_error('w is not a valid window',w)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert (type(d) == int and d >= 0), report_error('d is an invalid depth',d)

    # HINT: Remember to make the Pen visible while drawing
    w.clear()
    p = cornell.Pen(w)
    p.pencolor = 'magenta'
    p.fillcolor = 'magenta'
    triangle_helper(p, 0.0, 0.0, side, d)
    p.visible = False


def triangle_helper(p, x, y, side, d):
    """
    Draws a Sierpinski triangle with the given side length and depth d, anchored at (x, y).
    
    The triangle is draw with the current pen color and visibility attribute. Follow the 
    instructions on the course website to recursively draw the Sierpinski triangle. The
    bottom left corner of the triangle is anchored at (x,y).
    
    Parameter p: The graphics pen
    Precondition: p is a Pen with fill attribute False.
    
    Parameter x: The x-coordinate of the triangle bottom left corner
    Precondition: x is a number
    
    Parameter y: The y-coordinate of the triangle bottom left corner
    Precondition: y is a number
    
    Parameter side: The side-length of the triangle
    Precondition: side is a valid side length (number >= 0)
    
    Parameter d: The recursive depth of the triangle
    Precondition: n is a valid depth (int >= 0)
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_valid_penmode(p), report_error('Invalid pen mode', p)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert (type(d) == int and d >= 0), report_error('d is an invalid depth',d)
    assert is_number(x), report_error('x is not a valid position',x)
    assert is_number(y), report_error('x is not a valid position',y)

    # HINT: Use fill_triangle instead of setting p's position directly
    dis = ((3**0.5)/2)*side
    if d == 0:
        p.move(x,y)
        fill_triangle(p,x,y,side)
    else:
        triangle_helper(p,x,y,side/2.0,d-1)
        triangle_helper(p,x+(side/2.0),y,side/2.0,d-1)
        triangle_helper(p,x+(side/4.0),y+(dis/2.0),side/2.0,d-1)


# Useful helper function
def fill_triangle(p, x, y, side):
    """
    Fills an equilateral triangle of side length 
    
    The triangle is pointing up.
    
    Parameter p: The graphics pen
    Precondition: p is a Pen with fill attribute False.
    
    Parameter x: The x-coordinate of the triangle bottom left corner
    Precondition: x is a number
    
    Parameter y: The y-coordinate of thetriangle bottom left corner
    Precondition: y is a number
    
    Parameter side: The side length of the triangle
    Precondition: side is a valid side length (number >= 0)
    """
    # Precondition Assertions
    assert is_valid_penmode(p), report_error('Invalid pen mode', p)
    assert is_number(x), report_error('x is not a valid position',x)
    assert is_number(y), report_error('y is not a valid position',y)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    
    p.move(x, y)
    h = side * math.sqrt(.75)
    p.fill = True
    p.drawLine(side, 0)
    p.drawLine(-side/2.0, h)
    p.drawLine(-side/2.0, -h)
    p.fill = False




#################### TASK 4B: Sierpinski Snowflake ####################

def snowflake(w, side, d):
    """
    Draws a Sierpinski Snowflake with the given side length and depth d.
    
    This function clears the window and makes a new graphics pen p.  This pen starts in 
    the middle of the canvas at (0,0). It draws by calling the function 
    snowflake_helper(p, 0, 0, side, d). The pen is hidden during drawing and left 
    hidden at the end.
    
    The pen should have both a 'gray' fill color and a 'gray' line color.
    
    Parameter w: The window to draw upon.
    Precondition: w is a cornell Window object.
    
    Parameter side: The side-length of the snowflake
    Precondition: side is a valid side length (number >= 0)
    
    Parameter d: The recursive depth of the snowflake
    Precondition: n is a valid depth (int >= 0)
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_window(w), report_error('w is not a valid window',w)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert (type(d) == int and d >= 0), report_error('d is an invalid depth',d)
    # HINT: Remember to make the Pen hidden while drawing
   
    w.clear()
    p = cornell.Pen(w)
    p.visible = False
    p.pencolor = 'gray'
    p.fillcolor = 'gray'
    snowflake_helper(p, 0.0, 0.0, side, d)



def snowflake_helper(p, x, y, side, d):
    """
    Draws a snowflake with the given side length and depth d centered at (x, y).
    
    The snowflake is draw with the current pen color and visibility attribute. Follow the 
    instructions on the course website to recursively draw the Sierpinski Snowflake.
    
    Parameter p: The graphics pen
    Precondition: p is a Pen with fill attribute False.
    
    Parameter x: The x-coordinate of the snowflake center
    Precondition: x is a number
    
    Parameter y: The y-coordinate of the snowflake center
    Precondition: y is a number
    
    Parameter side: The side-length of the snowflake
    Precondition: side is a valid side length (number >= 0)
    
    Parameter d: The recursive depth of the snowflake
    Precondition: n is a valid depth (int >= 0)
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_valid_penmode(p), report_error('Invalid pen mode', p)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert (type(d) == int and d >= 0), report_error('d is an invalid depth',d)
    assert is_number(x), report_error('x is not a valid position',x)
    assert is_number(y), report_error('y is not a valid position',y)
    # HINT: Use fill_hex instead of setting p's position directly
    dis = ((3**0.5)/3)*side
    if d == 0:
        p.move(x,y)
        fill_hex(p,x,y,side)
    else:
        snowflake_helper(p,x-(2*side/3.0),y,side/3.0,d-1)
        snowflake_helper(p,x+(2*side/3.0),y,side/3.0,d-1)
        snowflake_helper(p,x-(side/3.0),y+dis,side/3.0,d-1)
        snowflake_helper(p,x-(side/3.0),y-dis,side/3.0,d-1)
        snowflake_helper(p,x+(side/3.0),y+dis,side/3.0,d-1)
        snowflake_helper(p,x+(side/3.0),y-dis,side/3.0,d-1)


# DO NOT MODIFY
def fill_hex(p, x, y, side):
    """
    Fills a hexagon of side length s with center at (x, y) using pen p.

    Parameter p: The graphics pen
    Precondition: p is a Pen with fill attribute False.
    
    Parameter x: The x-coordinate of the hexagon center
    Precondition: x is a number
    
    Parameter y: The y-coordinate of the hexagon center
    Precondition: y is a number
    
    Parameter side: The side length of the hexagon
    Precondition: side is a valid side length (number >= 0)
    """
    # Precondition Assertions
    assert is_valid_penmode(p), report_error('Invalid pen mode', p)
    assert is_number(x), report_error('x is not a valid position',x)
    assert is_number(y), report_error('y is not a valid position',y)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    
    # Move to the center and draw
    p.move(x + side, y)
    dx = side*math.cos(math.pi/3.0)
    dy = side*math.sin(math.pi/3.0)
    p.fill = True
    p.drawLine(  -dx,  dy)
    p.drawLine(-side,   0)
    p.drawLine(  -dx, -dy)
    p.drawLine(   dx, -dy)
    p.drawLine( side,   0)
    p.drawLine(   dx,  dy)
    p.fill = False




#################### TASK 5:H-True ####################

def htree(w, side, d):
    """
    Draws a H-tree with the given side length and depth d.
    
    This function clears the window and makes a new graphics pen p.  This pen starts in 
    the middle of the canvas at (0,0). It draws by calling the function 
    htree_helper(p, 0, 0, side, d). The pen is visible during drawing and but is left 
    hidden at the end.
    
    The pen should have both a 'blue' fill color and a 'blue' line color.
    
    Parameter w: The window to draw upon.
    Precondition: w is a cornell Window object.
    
    Parameter side: The side-length of the t-square
    Precondition: side is a valid side length (number >= 0)
    
    Parameter d: The recursive depth of the t-square
    Precondition: n is a valid depth (int >= 0)
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_window(w), report_error('w is not a valid window',w)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert (type(d) == int and d >= 0), report_error('d is an invalid depth',d)
    # HINT: Remember to make the Pen visible while drawing
    w.clear()
    p = cornell.Pen(w)
    p.pencolor = 'blue'
    p.fillcolor = 'blue'
    p.visible = True
    htree_helper(p,0.0,0.0,side,d,w)
    p.visible = False


def htree_helper(p, x, y, side, d,w):
    """
    Draws an H-tree with the given side length and depth d centered at (x, y).
    
    The H-tree is drawn with the current pen color and visibility attribute. Follow the 
    instructions on the course website to recursively draw the H-Tree.
    
    Parameter p: The graphics pen
    Precondition: p is a Pen with fill attribute False.
    
    Parameter x: The x-coordinate of the H-tree center
    Precondition: x is a number
    
    Parameter y: The y-coordinate of the H-tree center
    Precondition: y is a number
    
    Parameter side: The side-length of the H-tree
    Precondition: side is a valid side length (number >= 0)
    
    Parameter d: The recursive depth of the H-tree
    Precondition: n is a valid depth (int >= 0)
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_valid_penmode(p), report_error('Invalid pen mode', p)
    assert is_number(x), report_error('x is not a valid position',x)
    assert is_number(y), report_error('y is not a valid position',y)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    assert (type(d) == int and d >= 0), report_error('d is an invalid depth',d)
    assert is_window(w), report_error('w is not a valid window',w)
    # HINT: Use draw_h instead of setting p's position directly
    if d == 0:
        p.move(x,y)
        draw_h(p,x,y,side)
    else:
        htree_helper(p,x+(side/2.0), y+(side/2.0),side/2.0,d-1,w)
        htree_helper(p,x+(side/2.0), y-(side/2.0),side/2.0,d-1,w)
        htree_helper(p,x-(side/2.0), y+(side/2.0),side/2.0,d-1,w)
        htree_helper(p,x-(side/2.0), y-(side/2.0),side/2.0,d-1,w)
        htree_helper(p,x, y,side,d-1,w)



# IMPLEMENT ME
def draw_h(p, x, y, side):
    """
    Draw an H at center (x, y) of size s using pen p.
    
    Parameter p: The graphics pen
    Precondition: p is a Pen with fill attribute False.
    
    Parameter x: The x-coordinate of the H-tree center
    Precondition: x is a number
    
    Parameter y: The y-coordinate of the H-tree center
    Precondition: y is a number
    
    Parameter side: The side length of the H-tree
    Precondition: side is a valid side length (number >= 0)
    """
    # ARE THESE ALL OF THE PRECONDITIONS?
    assert is_valid_penmode(p), report_error('Invalid pen mode', p)
    assert is_number(x), report_error('x is not a valid position',x)
    assert is_number(y), report_error('y is not a valid position',y)
    assert is_valid_length(side), report_error('side is not a valid length',side)
    # HINT: Remember that (x,y) is the center of the H.
    p.move(x,y)
    dx = side*0.5
    dy = side*0.5
    p.drawLine(dx,0)
    p.drawLine(0,dy)
    p.drawLine(0,-2*dy)
    p.drawLine(0,dy)
    p.drawLine(-2*dx,0)
    p.drawLine(0,dy)
    p.drawLine(0,-2*dy)
    p.drawLine(0,dy)




################ Test Functions #################

def prompt(func):
    """
    Returns: The answer to a yes or no question.
    
    If the answer is invalid, it is treated as no.
    
    Parameter func: The function to ask about
    Precondition: func is string
    """
    ans = input('Call '+func+'? [y/n]: ')
    return ans.strip().lower() == 'y'


def depth(func):
    """
    Returns: The answer to a (recursion) depth question.
    
    If the anser is invalid, it is treated as -1.
    
    Parameter func: The function to ask about
    Precondition: func is string
    """
    ans = input('Function '+func+' depth? [-1 to skip]: ')
    try:
        return int(ans.strip())
    except:
        return -1


def main():
    """
    Runs each of the functions, allowing user to skip functions.
    """
    w = cornell.Window()
    
    if prompt('draw_two_lines'):
        draw_two_lines(w,5)
    
    if prompt('draw_triangle'):
        w.clear()
        turt = cornell.Turtle(w)
        draw_triangle(turt,50,'blue')
    
    if prompt('draw_hex'):
        w.clear()
        turt = cornell.Turtle(w)
        draw_hex(turt,50)
    
    if prompt('draw_spiral'):
        draw_spiral(w, 1, 24, 64, 0)
    
    if prompt('multi_polygons'):
        multi_polygons(w, 100, 5, 6, 0)
    
    if prompt('radiate'):
        radiate(w, 150, 45, 0)
    
    d = depth('triangle')
    if d >= 0:
        triangle(w, 200, d)
    
    d = depth('snowflake')
    if d >= 0:
        snowflake(w, 200, d)
    
    d = depth('htree')
    if d >= 0:
        htree(w, 200, d)
    
    # Pause for the final image
    input('Press <return>')


# Application code
if __name__ == '__main__':
    main()
