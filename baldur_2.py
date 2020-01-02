from neopixel import *
import time

 # LED strip configuration:
LED_COUNT      = 60     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

 
class Baldur: 

    running = False

    @staticmethod
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


    @staticmethod
    def rainbowCycle(wait_ms=20, iterations=5):
        """Draw rainbow that uniformly distributes itself across all pixels."""
        Baldur.running = True
        for j in range(256*iterations):
            if(not Baldur.running):
                break
            for i in range(strip.numPixels()):
                strip.setPixelColor(i, Baldur.wheel((int(i * 256 / strip.numPixels()) + j) & 255))
            strip.show()
            time.sleep(wait_ms/1000.0)


    @staticmethod
    def theaterChaseRainbow(wait_ms=50):
        """Rainbow movie theater light style chaser animation."""
        for j in range(256):
            for q in range(3):
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, Baldur.wheel((i+j) % 255))
                strip.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, 0)

    @staticmethod
    def colorWipe(color):
        """Wipe color across display a pixel at a time."""
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
        strip.show()

    @staticmethod
    def monotheater(color, wait_ms=300, iterations=10):
        """Movie theater light style chaser animation."""
        Baldur.running = True
        for j in range(iterations):
            for q in range(3):
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, color[0])
                strip.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, 0)

    @staticmethod
    def duotheater(color, wait_ms=300, iterations=10):
        """Movie theater light style chaser animation."""
        Baldur.running = True
        for j in range(iterations):
            for q in range(3):
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, color)
                strip.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, 0)

    @staticmethod
    def triotheater(color, wait_ms=300, iterations=10):
        """Movie theater light style chaser animation."""
        Baldur.running = True
        for j in range(iterations):
            for q in range(3):
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, color)
                strip.show()
                time.sleep(wait_ms/1000.0)
                for i in range(0, strip.numPixels(), 3):
                    strip.setPixelColor(i+q, 0)

    @staticmethod
    def stop():
        Baldur.running = False