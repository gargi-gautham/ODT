from machine import Pin
import time


IN1=Pin(5,Pin.OUT)
IN2=Pin(13,Pin.OUT)
IN3=Pin(14,Pin.OUT)
IN4=Pin(4,Pin.OUT)



# to rotate the motor (put in while loop for it to go on forever)

while(True):
    IN1.value(1)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)
    time.sleep_ms(2)   # timw.sleep_ms(1) basically makes the delay VERY small thats why it spins. greater the delay slower it moves therefore we cant see it well.
    #the ms means millisecond


    IN1.value(0)
    IN2.value(1)
    IN3.value(0)
    IN4.value(0)
    time.sleep_ms(2)


    IN1.value(0)
    IN2.value(0)
    IN3.value(1)
    IN4.value(0)
    time.sleep_ms(2)


    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(1)
    time.sleep_ms(2)









# Write your code here :-)
