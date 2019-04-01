import sys

import keyboard
import pyautogui

PLANT_SLOTS = {
    '1': (114, 43),
    '2': (114 + 51, 43),
    '3': (114 + 51 * 2, 43),
    '4': (114 + 51 * 3, 43),
    '5': (114 + 51 * 4, 43),
    '6': (114 + 51 * 5, 43),
    '7': (114 + 51 * 6, 43),
    '8': (114 + 51 * 7, 43),
    '9': (114 + 51 * 8, 43),
    '10': (114 + 51 * 9, 43),
    'shovel': (644, 36),
}

GARDEN_SLOTS = {
    'q': (35, 35),
    'w': (35 + 70, 35),
    'e': (35 + 70 * 2, 35),
    'r': (35 + 70 * 3, 35),
}

pyautogui.PAUSE = 0.01


def click_and_return(position):
    mouse_position = pyautogui.position()
    pyautogui.click(position)
    pyautogui.moveTo(mouse_position)


def select_plant(slot):
    print(slot)
    click_and_return(PLANT_SLOTS[slot])


def select_garden_tool(slot):
    print(slot)
    click_and_return(GARDEN_SLOTS[slot])


keyboard.add_hotkey('1', select_plant, args=['1'])
keyboard.add_hotkey('2', select_plant, args=['2'])
keyboard.add_hotkey('3', select_plant, args=['3'])
keyboard.add_hotkey('4', select_plant, args=['4'])
keyboard.add_hotkey('5', select_plant, args=['5'])
keyboard.add_hotkey('6', select_plant, args=['6'])
keyboard.add_hotkey('7', select_plant, args=['7'])
keyboard.add_hotkey('8', select_plant, args=['8'])
keyboard.add_hotkey('9', select_plant, args=['9'])
keyboard.add_hotkey('0', select_plant, args=['10'])
keyboard.add_hotkey('grave', select_plant, args=['10'])
keyboard.add_hotkey('tab', select_plant, args=['shovel'])

keyboard.add_hotkey('q', select_garden_tool, args=['q'])
keyboard.add_hotkey('w', select_garden_tool, args=['w'])
keyboard.add_hotkey('e', select_garden_tool, args=['e'])
keyboard.add_hotkey('r', select_garden_tool, args=['r'])

keyboard.add_hotkey('backslash', pyautogui.click)

print('Plants away!')

try:
    keyboard.wait()
except KeyboardInterrupt:
    print('No more zombies on your lawn!')
    sys.exit(0)
