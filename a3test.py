""" 
Unit Test for Assignment A3

This module implements several test cases for a3.  It is complete.  You should look 
though this file for places to add tests.

Junghwan Oh, jo299
Magd Bayoumi, mb2363
*DATE COMPLETED HERE
""" 
import cornell
import a3


def test_complement():
    """
    Test function complement
    """
    cornell.assert_equals(cornell.RGB(255-250, 255-0, 255-71),
                          a3.complement_rgb(cornell.RGB(250, 0, 71)))


def test_round():
    """
    Test function round (a3 version)
    """
    cornell.assert_equals(130.6,   a3.round(130.59,1))
    cornell.assert_equals(130.5,   a3.round(130.54,1))
    cornell.assert_equals(100.0,   a3.round(100,1))
    cornell.assert_equals(100.6,   a3.round(100.55,1))
    cornell.assert_equals(99.57,   a3.round(99.566,2))
    cornell.assert_equals(99.99,   a3.round(99.99,2))
    cornell.assert_equals(100.00,  a3.round(99.995,2))
    cornell.assert_equals(22.00,   a3.round(21.99575,2))
    cornell.assert_equals(21.99,   a3.round(21.994,2))
    cornell.assert_equals(10.01,   a3.round(10.013567,2))
    cornell.assert_equals(10.00,   a3.round(10.000000005,2))
    cornell.assert_equals(10.00,   a3.round(9.9999,3))
    cornell.assert_equals(9.999,   a3.round(9.9993,3))
    cornell.assert_equals(1.355,   a3.round(1.3546,3))
    cornell.assert_equals(1.354,   a3.round(1.3544,3))
    cornell.assert_equals(0.046,   a3.round(.0456,3))
    cornell.assert_equals(0.045,   a3.round(.0453,3))
    cornell.assert_equals(0.006,   a3.round(.0056,3))
    cornell.assert_equals(0.001,   a3.round(.0013,3))
    cornell.assert_equals(0.000,   a3.round(.0004,3))
    cornell.assert_equals(0.001,   a3.round(.0009999,3))


def test_str5():
    """
    Test function str5
    """
    cornell.assert_equals('130.6',  a3.str5(130.59))
    cornell.assert_equals('130.5',  a3.str5(130.54))
    cornell.assert_equals('100.0',  a3.str5(100))
    cornell.assert_equals('100.6',  a3.str5(100.55))
    cornell.assert_equals('99.57',  a3.str5(99.566))
    cornell.assert_equals('99.99',  a3.str5(99.99))
    cornell.assert_equals('100.0',  a3.str5(99.995))
    cornell.assert_equals('22.00',  a3.str5(21.99575))
    cornell.assert_equals('21.99',  a3.str5(21.994))
    cornell.assert_equals('10.01',  a3.str5(10.013567))
    cornell.assert_equals('10.00',  a3.str5(10.000000005))
    cornell.assert_equals('10.00',  a3.str5(9.9999))
    cornell.assert_equals('9.999',  a3.str5(9.9993))
    cornell.assert_equals('1.355',  a3.str5(1.3546))
    cornell.assert_equals('1.354',  a3.str5(1.3544))
    cornell.assert_equals('0.046',  a3.str5(.0456))
    cornell.assert_equals('0.045',  a3.str5(.0453))
    cornell.assert_equals('0.006',  a3.str5(.0056))
    cornell.assert_equals('0.001',  a3.str5(.0013))
    cornell.assert_equals('0.000',  a3.str5(.0004))
    cornell.assert_equals('0.001',  a3.str5(.0009999))


def test_str5_color():
    """
    Test the str5 functions for cmyk and hsv.
    """
    cornell.assert_equals('(98.45, 25.36, 72.80, 1.000)',
                          a3.str5_cmyk(cornell.CMYK(98.448, 25.362, 72.8, 1.0)))
    
    # Tests for str5_hsv (add two)


def test_rgb_to_cmyk():
    """
    Test translation function rgb_to_cmyk
    """
    # We use a3.str5 to handle round-off error in comparisons
    rgb = cornell.RGB(255, 255, 255);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornell.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornell.assert_equals('0.000', a3.str5(cmyk.magenta))
    cornell.assert_equals('0.000', a3.str5(cmyk.yellow))
    cornell.assert_equals('0.000', a3.str5(cmyk.black))
    
    rgb = cornell.RGB(0, 0, 0);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornell.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornell.assert_equals('0.000', a3.str5(cmyk.magenta))
    cornell.assert_equals('0.000', a3.str5(cmyk.yellow))
    cornell.assert_equals('100.0', a3.str5(cmyk.black))
        
    rgb = cornell.RGB(217, 43, 164);
    cmyk = a3.rgb_to_cmyk(rgb);
    cornell.assert_equals('0.000', a3.str5(cmyk.cyan))
    cornell.assert_equals('80.18', a3.str5(cmyk.magenta))
    cornell.assert_equals('24.42', a3.str5(cmyk.yellow))
    cornell.assert_equals('14.90', a3.str5(cmyk.black))


def test_cmyk_to_rgb():
    """
    Test translation function cmyk_to_rgb
    """
    #Test 1
    cmyk = cornell.CMYK(0.000,0.000,0.000,0.000)
    rgb = a3.cmyk_to_rgb(cmyk)
    cornell.assert_equals(255, rgb.red)
    cornell.assert_equals(255, rgb.green)
    cornell.assert_equals(255, rgb.blue)

    #Test 2
    cmyk = cornell.CMYK(29.00, 40.00, 32.00, 60.00)
    rgb = a3.cmyk_to_rgb(cmyk)
    cornell.assert_equals(72, rgb.red)
    cornell.assert_equals(61, rgb.green)
    cornell.assert_equals(69,  rgb.blue)


def test_rgb_to_hsv():
    """
    Test translation function rgb_to_hsv
    """
    pass # ADD TESTS TO ME


def test_hsv_to_rgb():
    """
    Test translation function hsv_to_rgb
    """
    pass # ADD TESTS TO ME







# Script Code
# THIS PREVENTS THE TESTS RUNNING ON IMPORT
if __name__ == '__main__':
    test_complement()
    test_round()
    test_str5()
    #test_str5_color()
    test_rgb_to_cmyk()
    test_cmyk_to_rgb()
    #test_rgb_to_hsv()
    #test_hsv_to_rgb()
    print('Module a3 is working correctly')
