import re
import math

def time_to_text(words, time):
    """
    Convert time to words
    """

    H = time.hour
    M = time.minute

    # Start Text
    text = "ES IST"
    word_leds = [words['TEXT']['HET'], words['TEXT']['IS']]
    corner_leds = []
    minutes = 0

    # Space
    text += " "

    # Minutes
    if 0 <= M < 5:
        text += ""
        minutes = M
    elif 5 <= M < 10 or 55 <= M <= 59:
        text += "VIJF"
        word_leds.append(words['MINUTES']['VIJF'])
        if M < 10:
            minutes = M - 5
        else:
            minutes = M - 55
    elif 10 <= M < 15 or 50 <= M < 55:
        text += "TIEN"
        word_leds.append(words['MINUTES']['TIEN'])
        if M < 15:
            minutes = M - 10
        else:
            minutes = M - 50
    elif 15 <= M < 20 or 45 <= M < 50:
        text += "KWART"
        word_leds.append(words['MINUTES']['KWART'])
        if M < 20:
            minutes = M - 15
        else:
            minutes = M - 45
    elif 20 <= M < 25:
        text += "TIEN VOOR HALF"
        word_leds.append(words['MINUTES']['TIEN'])
        word_leds.append(words['TEXT']['VOOR'])
        word_leds.append(words['TEXT']['HALF'])
        if M < 25:
            minutes = M - 20
    elif 40 <= M < 45:
        text += "TIEN OVER HALF"
        word_leds.append(words['MINUTES']['TIEN'])
        word_leds.append(words['TEXT']['OVER'])
        word_leds.append(words['TEXT']['HALF'])
        if M < 45:
            minutes = M - 40
    elif 25 <= M < 30:
        text += "VIJF VOOR HALF"
        word_leds.append(words['MINUTES']['VIJF'])
        word_leds.append(words['TEXT']['VOOR'])
        word_leds.append(words['TEXT']['HALF'])
        minutes = M - 25
    elif 30 <= M < 35:
        text += "HALF"
        word_leds.append(words['TEXT']['HALF'])
        minutes = M - 30
    elif 35 <= M < 40:
        text += "VIJF OVER HALF"
        word_leds.append(words['MINUTES']['VIJF'])
        word_leds.append(words['TEXT']['OVER'])
        word_leds.append(words['TEXT']['HALF'])
        minutes = M - 35

    # Space
    text += " "

    # Sign
    if 5 <= M < 14 | 35 <= M < 44:
        text += "OVER"
        word_leds.append(words['TEXT']['OVER'])
    elif 20 <= M <= 29 | 50 <= M < 59:
        text += "VOOR"
        word_leds.append(words['TEXT']['VOOR'])

    # Space
    text += " "

    # Hours
    if M >= 25:
        H += 1

    if H > 12:
        H = H - 12

    if H == 1 and M >= 5:
        text += "EEN"
        word_leds.append(words['HOURS']['EEN'])
    elif H == 1 and M < 5:
        text += "EEN"
        word_leds.append(words['HOURS']['EEN'])
    elif H == 2:
        text += "TWEE"
        word_leds.append(words['HOURS']['TWEE'])
    elif H == 3:
        text += "DRIE"
        word_leds.append(words['HOURS']['DRIE'])
    elif H == 4:
        text += "VIER"
        word_leds.append(words['HOURS']['VIER'])
    elif H == 5:
        text += "VIJF"
        word_leds.append(words['HOURS']['VIJF'])
    elif H == 6:
        text += "ZES"
        word_leds.append(words['HOURS']['ZES'])
    elif H == 7:
        text += "ZEVEN"
        word_leds.append(words['HOURS']['ZEVEN'])
    elif H == 8:
        text += "ACHT"
        word_leds.append(words['HOURS']['ACHT'])
    elif H == 9:
        text += "NEGEN"
        word_leds.append(words['HOURS']['NEGEN'])
    elif H == 10:
        text += "TIEN"
        word_leds.append(words['HOURS']['TIEN'])
    elif H == 11:
        text += "ELF"
        word_leds.append(words['HOURS']['ELF'])
    elif H == 12 or H == 0:
        text += "TWAALF"
        word_leds.append(words['HOURS']['TWAALF'])

    # UHR
    if M < 5:
        # Space
        text += " "
        text += "UUR"
        word_leds.append(words['TEXT']['UUR'])

    # Space
    if minutes != 0:
        text += " "

    # Dots
    if minutes == 1:
        text += "PUNT1"
        corner_leds.append(words['MINUTES']['PUNT1'])
    if minutes == 2:
        text += "PUNT2"
        corner_leds.append(words['MINUTES']['PUNT2'])
    if minutes == 3:
        text += "PUNT3"
        corner_leds.append(words['MINUTES']['PUNT3'])
    if minutes == 4:
        text += "PUNT4"
        corner_leds.append(words['MINUTES']['PUNT4'])

    text = re.sub(' +', ' ', text)
    word_leds = [item for sublist in word_leds for item in sublist]
    corner_leds = [item for sublist in corner_leds for item in sublist]
    return text, word_leds, corner_leds


def calculate_brightness(config, brightness):
    max_brightness_percentage = config['opt3001']['max_brightness_percentage']
    min_brightness_percentage = config['opt3001']['min_brightness_percentage']
    max_brightness_threshold = config['opt3001']['max_brightness_threshold']
    min_brightness_threshold = config['opt3001']['min_brightness_threshold']

    percentage = (brightness - min_brightness_threshold) / \
        (max_brightness_threshold - min_brightness_threshold)

    if percentage > 1:
        return max_brightness_percentage
    elif percentage < 0:
        return min_brightness_percentage
    else:
        return (max_brightness_percentage - min_brightness_percentage) * percentage + min_brightness_percentage


def get_leds_xy(x, y, length = 1, direction = "y"):
    leds = []

    led = 0
    if y % 2 == 0:
        led = y * 11 + x
    else:
        led = (y + 1) * 11 - x - 1

    if led <= 109:
        leds.append(led)
    else:
        return leds

    if direction == "y":
        for i in range(length - 1):
            led = 0
            if (y + i) % 2 == 0:
                led = leds[i] + 21 - 2 * x
            else:
                led = leds[i] + 21 - 2 * (10 - x)

            if led <= 109:
                leds.append(led)
            else:
                break

    leds = list(filter(lambda x: x >= 0, leds))
    return leds


def get_xy_led(led):
    # because led starts at 0
    led += 1
    x = 0
    y = math.ceil(led / 11) - 1
    rest = led % 11

    if y % 2 == 0:
        x = rest - 1 if rest > 0 else 10
    else:
        x = 11 - rest if rest > 0 else 0

    return (x,y)