import time
import utils
import numpy as np


# def start(ctrl, old_leds, target_leds):
#     while True:
#         new_leds = []
#         for led in old_leds:
#             if led in target_leds:
#                 new_leds.append(led)
#                 continue
#             bLed = getBottomLed(led)
#             if bLed < 111:
#                 new_leds.append(bLed)
#         ctrl.turn_on(new_leds)
#         old_leds = new_leds

#         # Transition is finished if all leds are in target_led
#         if all(elem in target_leds for elem in new_leds):
#             ctrl.turn_on(target_leds)
#             break
#         time.sleep(0.1)

#     return target_leds


def start(ctrl, target_leds):
    direction = 'y'
    length = np.random.randint(5, 9, 11)
    start = list(map(lambda x: -1 * (x + np.random.randint(0,5)), length))
    max_length = np.max(length)
    active_clock_leds = []

    for y in range(11 + max_length):
        leds = active_clock_leds
        for x in range(len(start)):
            start_x = x
            start_y = start[x] + y + 1
            strip_length = length[x]

            leds = leds + utils.get_leds_xy(start_x, start_y, strip_length, direction)
        active_clock_leds = list(set(leds).intersection(target_leds))
        leds = list(dict.fromkeys(leds))
        colors = get_green_values(len(leds))
        ctrl.turn_on(leds, colors)
        time.sleep(0.5)


def get_green_values(n):
    colors = np.tile(np.array([0, 255, 0]),(n,1))
    for color in colors:
        random1 = np.random.random_sample()
        if random1 < 0.8:
            continue
        random2 = np.random.random_sample()
        color[1] = random2 * color[1]
    return colors
