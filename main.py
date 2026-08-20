from machine import Pin, ADC, PWM
from time import sleep
import utime
adc = ADC(0)
buzzer = PWM(Pin(0))
perchance = True
digital = Pin(18,Pin.IN, Pin.PULL_UP)
button = Pin(16, Pin.IN, Pin.PULL_UP)
trigger = Pin(14, Pin.OUT)
echo = Pin(15, Pin.IN)
mid = 1.96
max = 2
greg = 12.5
accordingtoallknownlawsofaviationthereisnowayabeeshouldbeabletofly = True
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
def menu():
    while True:
        if button.value() == 0:
            print("off")
        else:
            IT = True
            if accordingtoallknownlawsofaviationthereisnowayabeeshouldbeabletofly == True:
                while IT == True:
                    ultra()
                    sond()
                    sound = sond()
                    distance = ultra()
                    print(sound)
                    print(distance)
                    if sound < mid or sound > max:
                       perchance = True
                    else:
                       perchance = False
                    if distance > greg:
                        if perchance == False:
                           while True:
                               buzzer.freq(500)
                               buzzer.duty_u16(1000)
                    if button.value() != 0:
                        IT = False
menu()