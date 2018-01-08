"""
The primary controller module for the Imager application

This module provides all of the image processing operations that are called whenever you 
press a button. Some of these are provided for you and others you are expected to write
on your own.

Based on an original file by Dexter Kozen (dck10) and Walker White (wmw2)

Author: Walker M. White (wmw2)
Date:    October 20, 2017 (Python 3 Version)
"""
import a6history


class Editor(a6history.ImageHistory):
    """
    A class that contains a collection of image processing methods
    
    This class is a subclass of ImageHistory.  That means it inherits all of the methods
    and attributes of that class.  We do that (1) to put all of the image processing
    methods in one easy-to-read place and (2) because we might want to change how we 
    implement the undo functionality later.
    
    This class is broken up into three parts (1) implemented non-hidden methods, (2)
    non-implemented non-hidden methods and (3) hidden methods.  The non-hidden methods
    each correspond to a button press in the main application.  The hidden methods are
    all helper functions.
    
    Each one of the non-hidden functions should edit the most recent image in the
    edit history (which is inherited from ImageHistory).
    """
    
    # PROVIDED ACTIONS (STUDY THESE)
    def invert(self):
        """
        Inverts the current image, replacing each element with its color complement
        """
        current = self.getCurrent()
        for pos in range(current.getLength()):
            rgb = current.getFlatPixel(pos)
            red   = 255 - rgb[0]
            green = 255 - rgb[1]
            blue  = 255 - rgb[2]
            rgb = (red,green,blue) # New pixel value
            current.setFlatPixel(pos,rgb)
    
    def transpose(self):
        """
        Transposes the current image
        
        Transposing is tricky, as it is hard to remember which values have been changed 
        and which have not.  To simplify the process, we copy the current image and use
        that as a reference.  So we change the current image with setPixel, but read
        (with getPixel) from the copy.
        
        The transposed image will be drawn on the screen immediately afterwards.
        """
        current  = self.getCurrent()
        original = current.copy()
        current.setWidth(current.getHeight())
        
        for row in range(current.getHeight()):
            for col in range(current.getWidth()):
                current.setPixel(row,col,original.getPixel(col,row))
    
    def reflectHori(self):
        """
        Reflects the current image around the horizontal middle.
        """
        current = self.getCurrent()
        for h in range(current.getWidth()//2):
            for row in range(current.getHeight()):
                k = current.getWidth()-1-h
                current.swapPixels(row,h,row,k)
    
    def rotateRight(self):
        """
        Rotates the current image left by 90 degrees.
        
        Technically, we can implement this via a transpose followed by a vertical
        reflection. However, this is slow, so we use the faster strategy below.
        """
        current  = self.getCurrent()
        original = current.copy()
        current.setWidth(current.getHeight())
        
        for row in range(current.getHeight()):
            for col in range(current.getWidth()):
                current.setPixel(row,col,original.getPixel(original.getHeight()-col-1,row))
    
    def rotateLeft(self):
        """
        Rotates the current image left by 90 degrees.
        
        Technically, we can implement this via a transpose followed by a vertical
        reflection. However, this is slow, so we use the faster strategy below.
        """
        current  = self.getCurrent()
        original = current.copy()
        current.setWidth(current.getHeight())
        
        for row in range(current.getHeight()):
            for col in range(current.getWidth()):
                current.setPixel(row,col,original.getPixel(col,original.getWidth()-row-1))
    
    
    # ASSIGNMENT METHODS (IMPLEMENT THESE)
    def reflectVert(self):
        """ 
        Reflects the current image around the vertical middle.
        """
        # implement me
        current = self.getCurrent()
        #print(current.getPixels()[0:25])
        for h in range(current.getHeight()//2):
            for col in range(current.getWidth()):
                k = current.getHeight()-1-h
                current.swapPixels(h,col,k,col)

    def monochromify(self, sepia):
        """
        Converts the current image to monochrome, using either greyscale or sepia tone.
        
        If `sepia` is False, then this function uses greyscale.  It removes all color 
        from the image by setting the three color components of each pixel to that pixel's 
        overall brightness, defined as 
            
            0.3 * red + 0.6 * green + 0.1 * blue.
        
        If sepia is True, it makes the same computations as before but sets green to
        0.6 * brightness and blue to 0.4 * brightness.
        
        Parameter sepia: Whether to use sepia tone instead of greyscale.
        Precondition: sepia is a bool
        """
        # implement me
        current  = self.getCurrent()
        for i in range(current.getLength()):
            brightness = 0.3 * current.getFlatPixel(i)[0] + \
            0.6 * current.getFlatPixel(i)[1] + 0.1 * current.getFlatPixel(i)[2]
            if sepia:
                current.setFlatPixel(i,(int(brightness),int(0.6*brightness),
                    int(0.4*brightness)))
            else:
                current.setFlatPixel(i,(int(brightness),int(brightness),
                    int(brightness)))
    
    def jail(self):
        """
        Puts jail bars on the current image
        
        The jail should be built as follows:
        * Put 3-pixel-wide horizontal bars across top and bottom,
        * Put 4-pixel vertical bars down left and right, and
        * Put n 4-pixel vertical bars inside, where n is (number of columns - 8) // 50.
        
        The n+2 vertical bars should be as evenly spaced as possible.
        """
        # implement me
        current  = self.getCurrent()
        for i in range(current.getWidth()):
            for m in range(3):
                current.setPixel(m,i,(255,0,0))
        for i in range(current.getWidth()):
            for m in range(3):
                current.setPixel(current.getHeight()-1-m,i,(255,0,0))
        for i in range(current.getHeight()):
            for m in range(4):
                current.setPixel(i,m,(255,0,0))
        for i in range(current.getHeight()):
            for m in range(4):
                current.setPixel(i,current.getWidth()-1-m,(255,0,0))

        a = current.getWidth()
        n = (a-8)//50
        b = a//(n+2)
        pos = 3
        for i in range(n+1):
            pos += b
            for m in range(4):
                for k in range(current.getHeight()):
                    current.setPixel(k,pos+m,(255,0,0))
    
    def vignette(self):
        """
        Modifies the current image to simulates vignetting (corner darkening).
        
        Vignetting is a characteristic of antique lenses. This plus sepia tone helps
        give a photo an antique feel.
        
        To vignette, darken each pixel in the image by the factor
        
            1 - (d / hfD)^2
        
        where d is the distance from the pixel to the center of the image and hfD 
        (for half diagonal) is the distance from the center of the image to any of 
        the corners.
        """
        current = self.getCurrent()
        for i  in range(current.getWidth()):
            for k in range(current.getHeight()):
                d = ((i - current.getWidth()//2)**2 + \
                    (k - current.getWidth()//2)**2)**0.5
                hfD = ((0 - current.getWidth()//2)**2 + \
                    (0 - current.getWidth()//2)**2)**0.5
                change = 1 - (d / hfD)**2
                a = current.getPixel(k,i)
                d = (min(max(int(a[0]*change),0),255), \
                    min(max(int(a[1]*change),0),255), \
                    min(max(int(a[2]*change),0),255))
                current.setPixel(k,i,d)
        # implement me
    
    def pixellate(self,step):
        """
        Pixellates the current image to give it a blocky feel.
        
        To pixellate an image, start with the top left corner (e.g. the first row and
        column).  Average the colors of the step x step block to the right and down
        from this corner (if there are less than step rows or step columns, go to the
        edge of the image). Then assign that average to ALL of the pixels in that block.
        
        When you are done, skip over step rows and step columns to go to the next 
        corner pixel.  Repeat this process again.  The result will be a pixellated image.
        
        Parameter step: The number of pixels in a pixellated block
        Precondition: step is an int > 0
        """
        isinstance(step,int)
        assert step > 0
        
        current = self.getCurrent()
        a = 0
        b = 0
        c = 0
        e = 0
        for i in range((current.getWidth()//step)+1):
            for k in range((current.getHeight()//step)+1):
                for m in range(i*step,(i+1)*step):
                    for n in range(k*step,(k+1)*step):
                        if m > current.getWidth()-1:
                            pass
                        else:
                            if n > current.getHeight()-1:
                                pass
                            else:
                                d = current.getPixel(n,m)
                                a += d[0]
                                b += d[1]
                                c += d[2]
                                e += 1
                for m in range(i*step,(i+1)*step):
                    for n in range(k*step,(k+1)*step):
                        if m > current.getWidth()-1:
                            pass
                        else:
                            if n > current.getHeight()-1:
                                pass
                            else:
                                current.setPixel(n,m,((int(a/(e))), \
                                    int(b/(e)),int(c/(e))))
                a = 0
                b = 0
                c = 0
                e = 0




        # implement me

    def encode(self, text):
        """
        Returns: True if it could hide the given text in the current image; False otherwise.
        
        This method attemps to hide the given message text in the current image.  It uses
        the ASCII representation of the text's characters.  If successful, it returns
        True.
        
        If the text has more than 999999 characters or the picture does not have enough
        pixels to store the text, this method returns False without storing the message.
        
        Parameter text: a message to hide
        Precondition: text is a string
        """
        isinstance(text, str)

        label_length = 11
        if label_length + len(text) > 999999 or label_length + \
        len(text) > self.getCurrent().getLength():
            return False
        else:
            self._start(len(text))

            for i in range(len(text)):
                self._encode_pixel(ord(text[i]), label_length+i-1)

            self._encode_pixel(ord(':'),label_length+len(text))
            return True
        # implement me

    
    def decode(self):
        """
        Returns: The secret message stored in the current image. 
        
        If no message is detected, it returns None
        """
        current = self.getCurrent()
        accum = ''
        for i in range(4, 10):
            accum += chr(self._decode_pixel(i))
            #print('decode for loop for length is {}'.format(accum))
        length = int(accum)
        #print(length)
        msg = ''
        for i in range(10, 10 + length):
            msg += chr(self._decode_pixel(i))
        #print(msg)
        return msg

    
    # HELPER FUNCTIONS
    def _drawHBar(self, row, pixel):
        """
        Draws a horizontal bar on the current image at the given row.
        
        This method draws a horizontal 3-pixel-wide bar at the given row of the current
        image. This means that the bar includes the pixels row, row+1, and row+2.
        The bar uses the color given by the pixel value.
        
        Parameter row: The start of the row to draw the bar
        Precondition: row is an int, with 0 <= row  &&  row+2 < image height
        
        Parameter pixel: The pixel color to use
        Precondition: pixel is a 3-element tuple (r,g,b) where each value is 0..255
        """
        current = self.getCurrent()
        for col in range(current.getWidth()):
            current.setPixel(row,   col, pixel)
            current.setPixel(row+1, col, pixel)
            current.setPixel(row+2, col, pixel)
    
    def _decode_pixel(self, pos):
        """
        Returns: the number n that is hidden in pixel pos of the current image.
        
        This function assumes that the value was a 3-digit number encoded as the
        last digit in each color channel (e.g. red, green and blue).
        
        Parameter pos: a pixel position
        Precondition: pos is an int with  0 <= p < image length (as a 1d list)
        """
        rgb = self.getCurrent().getFlatPixel(pos)
        red   = rgb[0]
        green = rgb[1]
        blue  = rgb[2]
        return  (red % 10) * 100  +  (green % 10) * 10  +  blue % 10

    def _encode_pixel(self, n, p):
        """
        Encode integer n in pixel number p of the current image.

        This function encodes a three digit number by adding (or otherwise
        changing) a single digit to each color channel (i.e., red, green and blue).

        Parameter n: a number to hide
        Precondition: an int with 0 <= n < 1000
        
        Parameter p: a pixel position
        Precondition: pixel position is valid (i.e. 0 <= p < self.current.len)
        """
        assert p < self.getCurrent().getLength()
        isinstance(n,int)
        assert n >= 0 and n < 1000
        old_pixel = self.getCurrent().getFlatPixel(p)
        old_red   = old_pixel[0]
        old_green = old_pixel[1]
        old_blue  = old_pixel[2]
        
        #Compute new red channel:
        first_digit = int(n/100)
        
        new_red = (int(old_red/10))*10 + first_digit
        
        if new_red - old_red > 5:       # Ensures that the difference between
            new_red -= 10               # new_red and old_red is never greater
                                        # than 5, preserving color quality
        
        if new_red > 255:
            new_red = new_red - 10
        elif new_red < 0:
            new_red += 10
        
        #Compute new green channel:
        second_digit = int((n-100*first_digit)/10)
        
        new_green = (int(old_green/10))*10 + second_digit
        
        if new_green - old_green > 5: 
            new_green -= 10               
        
        if new_green > 255:
            new_green = new_green - 10
        elif new_green < 0:
            new_green += 10
            
        #Compute new blue channel:
        third_digit = n-100*first_digit-10*second_digit
        
        new_blue = (int(old_blue/10))*10 + third_digit
        
        if new_blue - old_blue > 5: 
            new_blue -= 10               
        
        if new_blue > 255:
            new_blue = new_blue - 10
        elif new_blue < 0:
            new_blue += 10
        
        #Change pixel
        new_pixel = (int(new_red), int(new_green), int(new_blue))
        #print(new_pixel)
        self.getCurrent().setFlatPixel(p, new_pixel)

    def _start(self,lab):
        """
        Changes the first few pixels of an image to indicate a hidden message
        
        The first 5 + (number of digits in lab) are modified so that decode, when
        run with these pixels as arguments, yields a string of characters in
        the format "MSG_<lab>:" where <lab> is the length of the message. For
        example of message of length 100 would modify the image so that the
        first 8 pixels of the message would create the string "MSG_100:" when
        fed through decode.
        
        Parameter lab: lab is an integer value that describes the length of the text
        Precondition: lab is an int < 999999 and (the number of digits is lab) +
        5 + lab <= the number of pixels in the image
        """
        # Since this method is called only by hide, and hide guarantees that
        # the preconditions are met, there is no need to check preconditions
        #print(lab)
        
        a = str(lab)
        if len(a) < 6:
            b = 6 - len(a)
            lab = b*'0'+ str(lab)
        label = 'MSG_' + str(lab) + ':'
        #print('label is: {}'.format(label))

        for i in range(len(label)):
            self._encode_pixel(ord(label[i]), i)
    