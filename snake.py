from microbit import *
from random import randint

snake = [[0,0]]
food = [randint(1,4), randint(1,4)]

directions = [[1,0],[0,-1],[-1,0],[0,1]]
direction = 0

while True:
    if button_a.was_pressed():
        direction = (direction + 1)%4
    if button_b.was_pressed():
        direction = (direction - 1)%4

    next_block = [(snake[0][0] + directions[direction][0])%5, (snake[0][1] + directions[direction][1])%5]

    if next_block in snake:
        display.scroll("Game Over! Result: %s" %(len(snake)))
        break
    snake = [next_block] + snake

    if len(snake) == 25:
        display.scroll("You Win!")
        break

    if next_block == food:
        while food in snake:
            food = [randint(0,4), randint(0,4)]
    else:
        snake.pop()

    display.clear()
    display.set_pixel(food[0], food[1], 9)
    for i in range(len(snake)):
        display.set_pixel(snake[i][0], snake[i][1], int(5 -(i/len(snake)*5)%5 + 2))
    sleep(800)
