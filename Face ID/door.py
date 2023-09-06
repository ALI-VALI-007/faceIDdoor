#Importing stuff, Pin is pins for the raspberry, UART and PWM is fequencey stuff for bluetooth
from machine import pin,UART,PWM
import time

OPENTIME=5
LOCKTIME=4

#Uart channel and Baud rate
uart=UART(0,9600)

#left Motor variables
In1=Pin(6,Pin.OUT) 
In2=Pin(7,Pin.OUT)  
EN_A=PWM(Pin(8))

#Right Motor variables
In3=Pin(4,Pin.OUT)  
In4=Pin(3,Pin.OUT)  
EN_B=PWM(Pin(2))

#In1 and 3 are forward, In2 and 4 are backward, EN is power/speed of motor
#Sets the speed to high.
EN_A.high()
EN_B.high()

#Sets feq for the pins
EN_A.freq(1500)
EN_B.freq(1500)

#Sets duty cycle for max speed
EN_A.duty_u16(65025)
EN_B.duty_u16(65025)

def open():
    unlock()
    In1.high()
    In2.low()
    sleep(OPENTIME)
    close()

def close():
    In1.low()
    In2.high()
    sleep(OPENTIME)
    lock()

def lock():
    In3.high()
    In4.low()
    sleep(LOCKTIME)


def unlock():
    In4.high()
    In3.low()
    sleep(LOCKTIME)

def button():
    open()