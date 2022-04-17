"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    for i in range(11):
        jump()

def jump():
    up()
    cross()
    down()
def up():
    turn_left()
    while not right_is_clear():
        move()



def cross():
    turn_right()
    move()
    turn_right()

def down():
    while front_is_clear():
        move()
    turn_left()





def turn_right():
    turn_left()
    turn_left()
    turn_left()














####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
