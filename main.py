import numpy as np
import pygame as pg

cellsize = 40


def make_array(content):
    array = np.array(content)
    index = len(array) - 1
    return array, index


def rules(array, index, max_index, state, running):
    running = running
    old_symbol = array[index]
    state = state
    L = -1
    R = 1
    print(f"before: index {index}, current state {state}, current symbol {old_symbol}")
    if state == 0:
        if old_symbol == 0:
            array[index] = 1
            state = 1
            index += R
        elif old_symbol == 1:
            array[index] = 0
            state = 0
            index += L
    elif state == 1:
        if old_symbol == 0:
            array[index] = 0
            state = 1
            index += R
        elif old_symbol == 1:
            array[index] = 1
            state = 1
            index += R

    if index > max_index or index < 0:
        running = False

    print(f"in between: {array}")
    print(f"after: index {index}, state {state}, current symbol {old_symbol}")
    print()

    return array, index, state, running


def binary_to_decimal(binary):
    binary_string = ""
    for i in binary:
        binary_string += f"{i}"

    print()
    print(f"decimal number {int(binary_string, 2)}")
    print()


def graphic(display, number):
    display.fill((0))

    binary_string = ""
    for i in number:
        binary_string += f"{i}" + "   "

    font = pg.font.Font(None, 32)
    binary_visual = font.render(binary_string, True, (255,255,255),(0))
    binary_rect = binary_visual.get_rect()
    binary_rect.left = cellsize
    binary_rect.top = cellsize
    return binary_visual, binary_rect


def main(number):
    pg.init()
    index = len(number) - 1
    max_index = index

    surface = pg.display.set_mode(((len(number)+2)*cellsize, cellsize*3))
    pg.display.set_caption("Binary Increment")

    #binary, index = make_array(number) realized there is no need for an array

    print(number)
    binary_to_decimal(number)

    clock = pg.time.Clock()
    FPS = 30
    speed_count = 0
    running = True
    yes = True
    state = 0
    while True:
        text, text_rect = graphic(surface, number)
        surface.blit(text, text_rect)

        if speed_count % 30 == 0 and speed_count != 0 and running:
            binary, index, state, running = rules(number, index, max_index, state, running)
        elif not running and yes:
            print(number)
            binary_to_decimal(number)
            yes = False

        pg.display.update()
        clock.tick(FPS)
        speed_count += 1


running = True
numbers = [1,0,0,1,1,1,1,1,]
main(numbers)
