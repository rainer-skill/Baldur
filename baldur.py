#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from neopixel import *
import argparse
import json
import requests
import server



# LED strip configuration:
LED_COUNT      = 600     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=300, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def baldur(strip, color, wait_ms=50, iterations=10):
    """XXXX BALDUR XXXX."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def baldurV0(strip, color, color1, wait_ms=50):
    """BALDUR - MovGREEN"""
    for i in range (strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.setPixelColor(i+1, color)
        strip.setPixelColor(i+2, color1)
        strip.setPixelColor(i+3, color1)
        strip.setPixelColor(i+4, color1)
        strip.show()
        time.sleep(wait_ms/1000.0)

def baldurV1(strip, color, color1, wait_ms=50):
    """BALDUR - MovGREEN"""
    i = 0
    while i < strip.numPixels():
        for i in range (i,i+10):
            strip.setPixelColor(i, color1)
        for i in range (i,i+4):
            strip.setPixelColor(i, color) 
    strip.show()

def baldurV2(strip, color, color1, wait_ms=50):
    """BALDUR - ChrismasTree"""
    i = 0
    while i < strip.numPixels():
        for i in range (i,i+5):
            strip.setPixelColor(i, Color(0,0,0))
        for i in range (i,i+4):
            strip.setPixelColor(i, Color(255,140,0)) 
    strip.show()

def baldurV3(strip, color, wait_ms=50):
    """BALDUR - Glimmer"""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()


def colorConstant(strip, color):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()

def monotheater(strip, color, wait_ms=300, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def duotheater(strip, color, wait_ms=300, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def triotheater(strip, color, wait_ms=300, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)
        
# Main program logic follows:
if __name__ == '__main__':

    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:
        
        
        while True:
           
            #colorWipe(strip, Color(255, 0, 0)
            #reading current Parameters from Parameters.txt
            #with open('Parameters.txt') as json_file:
            #    data = json.load(json_file)
            #for p in data['RGB']:
            #    r = int(p['R'])
            #    g = int(p['G'])
            #    b = int(p['B'])   

            #Def with Parameters starts
            #theaterChase(strip, Color(200, 240, 20))
            colorConstant(strip, Color(50,50,50))
            #rainbowCycle(strip)
            #print ('XXXX BALDUR XXXX')
            #baldurV2(strip, Color(255,255,255),Color(50,255,50),255)
            #baldurV1(strip, Color(255,255,255),Color(50,255,50),255)
            #print ()

            #writing current Parameters from Parameters.txt
            #data = {}
            #data['RGB'] = []
            #data['RGB'].append({'R': r,'G': g,'B': b})
            #with open('Parameters.txt', 'w') as outfile:
            #    json.dump(data, outfile)    
    except KeyboardInterrupt:
        
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)
