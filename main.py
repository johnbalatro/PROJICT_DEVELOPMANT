from machine import Pin, ADC
from time import sleep
import utime
adc = ADC(0)
digital = Pin(18,Pin.IN, Pin.PULL_UP)
led = Pin(16, Pin.OUT)
trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)
def ultra():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   return distance
def sond():
    raw_value = adc.read_u16()
    # Conversion from analog value to voltage
    Volm = round(raw_value* 3.3 / 65536, 2)
    Volt = Volm
    digital_value = digital.value()
    sleep(0.5)
    return Volt
while
sond()
oliver_boliver_bolognese_greg_green_gaster_offtofindthetreasureandvaluevaluethefun = sond()
ultra()
gregoldy = ultra()