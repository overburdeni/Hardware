import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
def my_callback(channel):
    print('You pressed the button')

GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(18,GPIO.FALLING,callback=my_callback,bouncetime=100)

i = 0
while True:
    # if GPIO.input(18) == False:
    #     # put the code to be actioned here
    # time.sleep(0.1)
    i = i + 1
    print(i)
    time.sleep(1)