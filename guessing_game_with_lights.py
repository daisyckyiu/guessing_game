# guessing_game.py
# 
import random
import time
import RPi.GPIO as GPIO

def main():

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7,GPIO.OUT)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
 
    n = random.randint(1,99)
    guess = int(input("Enter an integer from 1 to 99: "))
    while n != "guess":
        print()
        if guess < n:
            GPIO.output(11,True)
            time.sleep(1)
            GPIO.output(11,False)
            guess =int(input("Enter an integer from 1 to 99: "))
        elif guess > n:
            GPIO.output(7,True)
            time.sleep(1)
            GPIO.output(7,False)
            guess = int(input("Enter an integer from 1 to 99: "))
        else:
            GPIO.output(13,True)
            time.sleep(1)
            GPIO.output(13,False)
            break
        print()
            
    GPIO.cleanup()

main()
