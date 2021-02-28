import numpy as np


def make_array(content):
    array = np.array(content)
    index = len(array) -1
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
    print(f"after: index {index}, state {state}, current symbol {old_symbol}")
    print(f"in between: {array}")
    print()

    return array, index, state, running


def binary_to_decimal(binary):
    binary_string = ""
    for i in binary:
        binary_string += f"{i}"

    print(f"decimal number {int(binary_string, 2)}")

def main(number):
    binary, index = make_array(number)
    max_index = index
    print(binary)
    binary_to_decimal(binary)

    running = True
    state = 0
    while running:
        binary, index, state, running = rules(binary, index, max_index, state, running)

    print(binary)
    binary_to_decimal(binary)


running = True
numbers = [1,0,0,1,1,1,1,1,]
main(numbers)
