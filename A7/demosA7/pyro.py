"""
An Invaders-like Controller module for lecture demos.

You should refer to this file to see how to had and remove laser bolts.

Authors: Walker White (wmw2), Lillian Lee (ljl2), and Steve Marschner (srm2)
Date:    November 10, 2017 (Python 3 Version)
"""
import cornell
import random
import math
from game2d import *

############# CONSTANTS #############
# Window Size
WINDOW_WIDTH  = 512
WINDOW_HEIGHT = 512

# Gravity of surface
GRAVITY = -0.2
# Upward velocity
ROCKET_VY = 1.2
# For the explosion
PARTICLE_DIAMETER = 5
MAX_INIT_VEL = 5
PARTICLES_PER_SHELL = 50


############# CONTROLLER CLASS #############
class Pyro(GameApp):
    """
    This class is a controller for lecture demos about interaction and animation.

    This class extends GameApp and implements the various methods necessary for 
    an interactive application.

    * Method start() is called once at the beginning.

    * Method update() is called repeatedly to do animation.

    * Attribute _state keeps track of the current game state.
    
    * The on_touch methods handle mouse (or finger) input.
        
    INSTANCE ATTRIBUTES (Not hiding any):
        view :    the view (inherited from Game)    [GView]
        input :   the input (inherited from Game)   [GInput]
        _rockets: the list of rockets to animate    [list of Rocket]
        _sparks:  the list of sparks to animate     [list of Spark]
        _last:    the last position clicked [GPoint, None if mouse not down last frame]
    """
    
    # THREE MAIN METHODS
    
    def start(self):
        """
        Initializes the program state.
        """
        self._rockets = []
        self._sparks  = []
        self._last = None # Have not clicked mouse yet.
    
    def update(self,dt):
        """
        Animates a single frame. Called every 1/60 of a second.
        
        Parameter dt: The time since the last animation frame.
        Precondition: dt is a float.
        """
        # helper method to process the mouse click
        self._checkClick() 
        # Helper method to move rockets
        self._moveRockets()
    
    def draw(self):
        """
        Draws all particles in the view.
        """
        for rocket in self._rockets:
            rocket.draw(self.view)
        
        for spark in self._sparks:
            spark.draw(self.view)
    
    
    # HELPER METHODS
    def _explodeRocket(self, rocket):
        """
        Explodes the ship rocket.
        
        Parameter rocket: The rocket to explode
        Precondition: rocket must be of type Rocket.
        """ 
        color = cornell.RGB(random.randrange(256),
                            random.randrange(256),
                            random.randrange(256))
        for i in range(PARTICLES_PER_SHELL):
            spark = Spark(rocket.x, rocket.y, color)
            self._sparks.append(spark)
    
    def _checkClick(self):
        """
        Checks for a click and add a Rocket if necessary.
        
        A 'click' is the animation frame after the mouse is pressed for the first
        time in a while (so _lastclick is None).
        """
        # Input stores the touch information
        touch = self.input.touch
        
        if self._last is None and not touch is None:
            # Click happened.  Add rocket to particle list.
            rocket = Rocket(touch.x, touch.y)
            self._rockets.append(rocket)
        
        # Update lastclick
        self._last = touch

    
    def _moveRockets(self):
        """
        Moves all the rockets and explodes them when they get to high.
        """
        for rocket in self._rockets:
            rocket.move()
            # Handle a rocket if it explodes
            if rocket.isExploded():  # MUST use getter here
                self._explodeRocket(rocket)
        
        # Delete any exploded rockets
        i = 0
        while i < len(self._rockets):
            if self._rockets[i].isExploded():  # MUST use getter here
                del self._rockets[i]
            else:
                i += 1
        
        # move all the sparks
        for spark in self._sparks:
            spark.move()
        
        # Delete any sparks out of view
        i = 0
        while i < len(self._sparks):
            if self._sparks[i].y < -10:
                del self._sparks[i]
            else:
                i += 1


############# MODEL CLASSES #############
class Spark(GEllipse):
    """
    This class represents particles created in shell explosions.
    
    INSTANCE ATTRIBUTES (Beyond those in GEllipse):
        _vx: velocity in x direction    [float]
        _vy: velocity in y direction    [float]
    """
    
    def __init__(self, x, y, color=cornell.WHITE):
        """
        Initializer: Creates particle at (x,y) with random velocity and given color.
        
        Parameter x: the starting x-coordinate
        Precondition: x is a number (int or float)
        
        Parameter y: the starting y-coordinate
        Precondition: y is a number (int or float)
        
        Parameter color: the spark color
        Precondition: color is a valid color object or name (e.g. a string)
        """
        GEllipse.__init__(self, x=x, y=y, 
                          width=PARTICLE_DIAMETER, height=PARTICLE_DIAMETER,
                          fillcolor=color)        
        self._vy = random.uniform(-MAX_INIT_VEL,MAX_INIT_VEL)
        self._vx = math.sqrt(MAX_INIT_VEL**2 - self._vy**2) * math.sin(random.uniform(0,2*math.pi))
    
    def move(self):
        """
        Moves the spark by the current velocity
        """
        self.x += self._vx
        self.y += self._vy
        self._vy += GRAVITY


class Rocket(GEllipse):
    """
    This class represents rockets that will generate explosions later.
    
    INSTANCE ATTRIBUTES (Beyond those in GEllipse):
        _trigger_y: the y coordinate at which rocket will explode    [float]
        _exploded:  True if the rocket has exploded 
                    [bool, True if self.y > self.trigger_y]
    """
    
    # Must use getters to access with an object of another class
    def isExploded(self):
        """
        Returns: True if rocket has exploded, False otherwise
        """
        return self._exploded
    
    def __init__(self, x, y):
        """
        Initializer: Creates a rocket headed for an explosion at (x,y).
        
        Parameter x: the starting x-coordinate
        Precondition: x is a number (int or float)
        
        Parameter y: the y=threshold for the explosion
        Precondition: y is a number (int or float)
        """
        GEllipse.__init__(self, x=x, y=0, 
                          width=PARTICLE_DIAMETER, height=PARTICLE_DIAMETER,
                          fillcolor=cornell.GRAY)    
        self._trigger_y = y
        self._exploded = False
    
    def move(self):
        """
        Moves the rocket and sets it to explode as necessary.
        """
        self.y += ROCKET_VY
        if self.y > self._trigger_y:
            self._exploded = True


# Script Code
if __name__ == '__main__':
    Pyro(width=WINDOW_WIDTH,height=WINDOW_HEIGHT,fps=30.0).run()
