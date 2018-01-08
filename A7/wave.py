"""
Subcontroller module for Alien Invaders

This module contains the subcontroller to manage a single level or wave in the Alien
Invaders game.  Instances of Wave represent a single wave.  Whenever you move to a
new level, you are expected to make a new instance of the class.

The subcontroller Wave manages the ship, the aliens and any laser bolts on screen.  
These are model objects.  Their classes are defined in models.py.

Most of your work on this assignment will be in either this module or models.py.
Whether a helper method belongs in this module or models.py is often a complicated
issue.  If you do not know, ask on Piazza and we will answer.

# YOUR NAME(S) AND NETID(S) HERE
# DATE COMPLETED HERE
"""
from game2d import *
from consts import *
from models import *
import random

# PRIMARY RULE: Wave can only access attributes in models.py via getters/setters
# Wave is NOT allowed to access anything in app.py (Subcontrollers are not permitted 
# to access anything in their parent. To see why, take CS 3152)


class Wave(object):
    """
    This class controls a single level or wave of Alien Invaders.
    
    This subcontroller has a reference to the ship, aliens, and any laser bolts on screen. 
    It animates the laser bolts, removing any aliens as necessary. It also marches the
    aliens back and forth across the screen until they are all destroyed or they reach
    the defense line (at which point the player loses). When the wave is complete, you 
    should create a NEW instance of Wave (in Invaders) if you want to make a new wave of 
    aliens.
    
    If you want to pause the game, tell this controller to draw, but do not update.  See 
    subcontrollers.py from Lecture 24 for an example.  This class will be similar to
    than one in how it interacts with the main class Invaders.
    
    #UPDATE ME LATER
    INSTANCE ATTRIBUTES:
        _ship:   the player ship to control [Ship]
        _aliens: the 2d list of aliens in the wave [rectangular 2d list of Alien or None] 
        _bolts:  the laser bolts currently on screen [list of Bolt, possibly empty]
        _dline:  the defensive line being protected [GPath]
        _lives:  the number of lives left  [int >= 0]
        _time:   The amount of time since the last Alien "step" [number >= 0]
    
    As you can see, all of these attributes are hidden.  You may find that you want to
    access an attribute in class Invaders. It is okay if you do, but you MAY NOT ACCESS 
    THE ATTRIBUTES DIRECTLY. You must use a getter and/or setter for any attribute that 
    you need to access in Invaders.  Only add the getters and setters that you need for 
    Invaders. You can keep everything else hidden.
    
    You may change any of the attributes above as you see fit. For example, may want to 
    keep track of the score.  You also might want some label objects to display the score
    and number of lives. If you make changes, please list the changes with the invariants.
    
    LIST MORE ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    
        _direction: the direction that the aliens are going [0 (right) or 1 (left)]
        -randomness: the chances that an alien fires a bolt [int]
        -count
    """
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    
    # INITIALIZER (standard form) TO CREATE SHIP AND ALIENS
    def __init__(self):
        self._aliens = []
        self._time = 0
        self._direction = 0
        self._bolts = []
        self.makeAliens()
        self._ship = self.makeShip()
        self._dline = self.makeDLine()
        self._randomness = random.randint(1, BOLT_RATE)
        self._count = 0
        self._lives = SHIP_LIVES


    # UPDATE METHOD TO MOVE THE SHIP, ALIENS, AND LASER BOLTS
    def update(self, input, dt):
        
        if (input.is_key_down('left')):
            self._ship.x -= SHIP_MOVEMENT
            self._ship.x = max(0 + (SHIP_WIDTH//2), self._ship.x)
        if (input.is_key_down('right')):
            self._ship.x += SHIP_MOVEMENT
            self._ship.x = min(GAME_WIDTH - (SHIP_WIDTH//2), self._ship.x)
        if (input.is_key_down('spacebar')):
            if (self.checkPlayerBolts() == True):
                k = self.makeBolt(self._ship.x, self._ship.y + 3*(SHIP_HEIGHT//2),'Player', BOLT_SPEED)
                self._bolts.append(k)
            else:
                pass

        self._time += dt
        self.moveAliens(self._time)
        self.fireAliens(self._time)
        self.moveBolts()
        self.checkCollisions()
        


    # DRAW METHOD TO DRAW THE SHIP, ALIENS, DEFENSIVE LINE AND BOLTS
    def draw(self, view):
        for row in self._aliens:
            for alien in row:
                if (alien != None):
                    alien.draw(view)

        if(self._ship != None):
            self._ship.draw(view)
        self._dline.draw(view)
        for x in self._bolts:
            x.draw(view)


    # HELPER METHODS
    def makeAliens(self):
        for x in range(ALIEN_ROWS):
            t = []
            for y in range(ALIENS_IN_ROW):
                z = Alien((ALIEN_HALF + ALIEN_H_SEP) + y*(ALIEN_WIDTH + ALIEN_H_SEP), (GAME_HEIGHT - (ALIEN_HALF + ALIEN_CEILING) - x*(ALIEN_HEIGHT + ALIEN_V_SEP)), ALIEN_WIDTH, ALIEN_HEIGHT, self.alienImage(x,ALIEN_ROWS))
                t.append(z)
            self._aliens.append(t)


    def alienImage(self, w, h):
        # Returns the right image for the alien
        # w is the current row
        # h is the number of alien rows
        q = ALIEN_IMAGES_NUM

        if (h % 2 == 0):
            r = w // 2
            return ALIEN_IMAGES[-1-(r%q)]

        else:
            if (w == 0):
                return ALIEN_IMAGES[-1]
            else:
                if (w % 2 == 1):
                    r = (w+1) //2
                    return ALIEN_IMAGES[-1-(r%q)]

                else:
                    r = w // 2
                    return ALIEN_IMAGES[-1-(r%q)]

    def makeShip(self):
        z = Ship(x = GAME_WIDTH//2, y = (SHIP_BOTTOM + SHIP_HEIGHT//2), width = SHIP_WIDTH, height = SHIP_HEIGHT, source ='ship.png')
        return z

    def makeDLine(self):
        z = GPath(points = [0,DEFENSE_LINE,GAME_WIDTH,DEFENSE_LINE], linewidth = 2, linecolor = 'black')
        return z

    def moveAliens(self, time):
        if (time > ALIEN_SPEED):
            if (self._direction == 0):
                self.moveRight()

                if (self.changeDirection()):
                    self.moveDown()
                    self._direction = 1

            else:
                self.moveLeft()

                if (self.changeDirection()):
                    self.moveDown()
                    self._direction = 0

        else:
            pass

    def changeDirection(self):
        #returns true if the rightmost or leftmost alien has reached past the ALIEN_H_SEP
        y = 2.5*ALIEN_H_SEP
        #Left most Alien x position
        mostLeft = self.mostLeft()

        #right most Alien
        mostRight = self.mostRight()

        if (mostLeft < y):
            return True 
        if ((GAME_WIDTH - mostRight) < y):
            return True 
        else:
            return False

    def makeBolt(self, x, y, source, BOLT_SPEED):
        z = Bolt(x, y, BOLT_WIDTH, BOLT_HEIGHT, 'red', source, BOLT_SPEED)
        return z

    def moveBolts(self):
        for x in self._bolts:
            x.y += x.getVelocity()
            if (x.y > GAME_HEIGHT):
                self._bolts.remove(x)
            if (x.y < 0):
                self._bolts.remove(x)

    def checkPlayerBolts(self):
        i = 0
        for x in self._bolts:
            if (x.isPlayerBolt() == True):
                i += 1
        if (i == 0):
            return True
        else:
            return False

    def fireAliens(self, time):
        if (time > ALIEN_SPEED):
            self._count += 1
            if (self._count == self._randomness):
                y = random.randint(0, ALIENS_IN_ROW-1)
                z = None
                x_pos = 0
                y_pos = 0

                for x in range(ALIEN_ROWS):
                    if (self._aliens[x][y] != None):
                        z = self._aliens[x][y]
                        x_pos = z.x
                        y_pos = z.y - (ALIEN_HEIGHT//2)
                        
                if (x_pos != 0 and y_pos != 0):
                    g = self.makeBolt(x_pos, y_pos, 'Alien', BOLT_SPEED)
                    self._bolts.append(g)

                self._count = 0
                self._randomness = random.randint(1, BOLT_RATE)
            self._time = 0
            
        
        else:
            pass


    def moveRight(self):
        for row in self._aliens:
            for alien in row:
                if (alien != None):
                    alien.x += ALIEN_H_WALK

    def moveLeft(self):
        for row in self._aliens:
            for alien in row:
                if (alien != None):
                    alien.x -= ALIEN_H_WALK

    def moveDown(self):
        for row in self._aliens:
            for alien in row:
                if (alien != None):
                    alien.y -= ALIEN_V_SEP


    def collides(self,bolt):
        z = bolt

        if (self.contains(z.x - (BOLT_WIDTH//2), z.y - (BOLT_HEIGHT//2))):
            return True

        if (self.contains(z.x - (BOLT_WIDTH//2), z.y + (BOLT_HEIGHT//2))):
            return True

        if (self.contains(z.x + (BOLT_WIDTH//2), z.y - (BOLT_HEIGHT//2))):
            return True

        if (self.contains(z.x + (BOLT_WIDTH//2), z.y + (BOLT_HEIGHT//2))):
            return True

        else:
            return False


    def checkCollisions(self):
        for x in self._bolts:
            if (self._ship != None):
                if (self._ship.collides(x) == True):
                    self._ship = None
                    self._bolts.remove(x)

        for row in range(ALIEN_ROWS):
            for col in range(ALIENS_IN_ROW):
                for x in self._bolts:
                    if (self._aliens[row][col] != None):
                        if (self._aliens[row][col].collides(x) == True and self.playerBolt(x)): ######
                            self._aliens[row][col] = None
                            self._bolts.remove(x)

    def playerBolt(self, bolt):
        z = bolt
        if (z._source == 'Player'):
            return True
        else:
            return False


    def mostRight(self):
        for y in range(ALIENS_IN_ROW-1, -1, -1):
            for x in range(ALIEN_ROWS-1, -1, -1):
                if (self._aliens[x][y] != None):
                    return self._aliens[x][y].x

        return 0


    def mostLeft(self):
        for y in range(ALIENS_IN_ROW):
            for x in range(ALIEN_ROWS):
                if (self._aliens[x][y] != None):
                    return self._aliens[x][y].x

        return 0


    def checkPaused(self):
        if (self._ship == None and self._lives > 1):
            return True
        else:
            return False

    def checkGameOver(self):
        if (self._ship == None and self._lives == 1):
            return True
        else:
            return False


    def restartShip(self):
        self._ship = self.makeShip()
        self._lives -= 1


    def allAliensDead(self):
        for y in range(ALIENS_IN_ROW):
            for x in range(ALIEN_ROWS):
                if (self._aliens[x][y] != None):
                    return False

        return True

    def aliensInvaded(self):
        for y in range(ALIENS_IN_ROW):
            for x in range(ALIEN_ROWS):
                if (self._aliens[x][y] != None):
                    if (self._aliens[x][y].y < DEFENSE_LINE):
                        return True

        return False





        """
        if (ALIEN_ROWS %2 != 0):
            t = []
            for y in range(ALIENS_IN_ROW+1):
                    z = Alien((ALIEN_HALF + ALIEN_H_SEP) + y*(ALIEN_WIDTH + ALIEN_H_SEP), (ALIEN_HALF + ALIEN_CEILING), ALIEN_WIDTH, ALIEN_HEIGHT, ALIEN_IMAGES[-1])
                    t.append(z)
            self._aliens.append(t)

            for x in range (1,ALIENS_IN_ROW-2,2):
                f_row = []
                s_row = []
                for y in range(ALIENS_IN_ROW):
                    z = Alien((ALIEN_HALF + ALIEN_H_SEP) + y*(ALIEN_WIDTH + ALIEN_H_SEP), (ALIEN_HALF + ALIEN_CEILING) + (x*2)*(ALIEN_HEIGHT + ALIEN_V_SEP), ALIEN_WIDTH, ALIEN_HEIGHT, ALIEN_IMAGES[-1-(x%ALIEN_IMAGES_NUM)])
                    p = Alien((ALIEN_HALF + ALIEN_H_SEP) + y*(ALIEN_WIDTH + ALIEN_H_SEP), 2*(ALIEN_HALF + ALIEN_CEILING) + (x*2)*(ALIEN_HEIGHT + ALIEN_V_SEP), ALIEN_WIDTH, ALIEN_HEIGHT, ALIEN_IMAGES[-1-(x%ALIEN_IMAGES_NUM)])
                    f_row.append(z)
                    s_row.append(p)
                self._aliens.append(f_row)
                self._aliens.append(s_row)

        else:
            for x in range(0, ALIEN_ROWS-2, 2):
                f_row = []
                s_row = []
                for y in range(0, ALIENS_IN_ROW):
                    z = Alien((ALIEN_HALF + ALIEN_H_SEP) + y*(ALIEN_WIDTH + ALIEN_H_SEP), (ALIEN_HALF + ALIEN_CEILING) + (x*2)*(ALIEN_HEIGHT + ALIEN_V_SEP), ALIEN_WIDTH, ALIEN_HEIGHT, ALIEN_IMAGES[-1-(x%ALIEN_IMAGES_NUM)])
                    p = Alien((ALIEN_HALF + ALIEN_H_SEP) + y*(ALIEN_WIDTH + ALIEN_H_SEP), 2*(ALIEN_HALF + ALIEN_CEILING) + (x*2)*(ALIEN_HEIGHT + ALIEN_V_SEP), ALIEN_WIDTH, ALIEN_HEIGHT, ALIEN_IMAGES[-1-(x%ALIEN_IMAGES_NUM)])
                    f_row.append(z)
                    s_row.append(p)
                self._aliens.append(f_row)
                self._aliens.append(s_row)


            

            t = []
            for y in range(ALIENS_IN_ROW+1):
                    z = Alien((ALIEN_HALF + ALIEN_H_SEP) + y*(ALIEN_WIDTH + ALIEN_H_SEP), (ALIEN_HALF + ALIEN_CEILING), ALIEN_WIDTH, ALIEN_HEIGHT, ALIEN_IMAGES[-1])
                    t.append(z)
            self._aliens.append(t)

            for x in range (1,ALIENS_IN_ROW+1):
                t = []
                w = []
                for y in range(ALIENS_IN_ROW +1):
                    z = Alien((ALIEN_HALF + ALIEN_H_SEP) + y*(ALIEN_WIDTH + ALIEN_H_SEP), (ALIEN_HALF + ALIEN_CEILING) + x*(ALIEN_HEIGHT + ALIEN_V_SEP), ALIEN_WIDTH, ALIEN_HEIGHT, ALIEN_IMAGES[-1-(x%ALIEN_IMAGES_NUM)])
                    p = Alien((ALIEN_HALF + ALIEN_H_SEP) + y*(ALIEN_WIDTH + ALIEN_H_SEP), (ALIEN_HALF + ALIEN_CEILING) + x*(ALIEN_HEIGHT + ALIEN_V_SEP), ALIEN_WIDTH, ALIEN_HEIGHT, ALIEN_IMAGES[-1-(x%ALIEN_IMAGES_NUM)])
                    t.append(z)
                    w.append(p)
                self._aliens.append(t)
                self._aliens.append(w)





            for x in range(0, ALIEN_ROWS+1):
                t = []
                w = []
                for y in range(ALIENS_IN_ROW+1):
                        z = Alien((ALIEN_HALF + ALIEN_H_SEP) + y*(ALIEN_WIDTH + ALIEN_H_SEP), (ALIEN_HALF + ALIEN_CEILING) + x*(ALIEN_HEIGHT + ALIEN_V_SEP), ALIEN_WIDTH, ALIEN_HEIGHT, ALIEN_IMAGES[-1-(x%ALIEN_IMAGES_NUM)])
                        p = Alien((ALIEN_HALF + ALIEN_H_SEP) + y*(ALIEN_WIDTH + ALIEN_H_SEP), (ALIEN_HALF + ALIEN_CEILING) + x*(ALIEN_HEIGHT + ALIEN_V_SEP), ALIEN_WIDTH, ALIEN_HEIGHT, ALIEN_IMAGES[-1-(x%ALIEN_IMAGES_NUM)])
                        t.append(z)
                        w.append(p)
                self._aliens.append(t)
                self._aliens.append(w)

            """