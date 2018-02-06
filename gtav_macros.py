import sys
import time

import keyboard


# These are the actual arrow key codes in GTAV... These are not common codes.
# They seem to be present in LWJGL (and by extension Minecraft), but couldn't
# find them beyond that :S
VK_UP = 200
VK_LEFT = 203
VK_RIGHT = 205
VK_DOWN = 208


# KEY_PAUSE = 0.01

def write_with_keyboard(keys):
    """
    Wrapper around `keyboard.send` to manage many keys with pauses in the middle.
    `keyboard.write` doesn't accept key codes (at least high key codes) so it
    doesn't work.
    `pyautogui` plain didn't work :(

    Incredibly, no pause of any kind is required, contrary to what I'd heard
    about other macros on the internet and prepared for.
    If at any point in the future pauses were necessary consider making them
    key code dependent.

    NOTE: Opening and closing the Interaction Menu in a spamming manner ('m')
    takes longer than spamming the other keys and to consistently spam it a
    minimum pause of 0.1 is required, but to do those independently the 0.1
    pause is NOT required.
    """
    for key in keys:
        keyboard.send(key)


def open_snack_inventory():
    """
    Interaction Menu > Inventory > Snacks
    NOTE: If CEO is active a new option appears at the top, so two VK_DOWNs are
    necessary.
    TODO: Toggle between regular and CEO mode in the CLI (reading stdin maybe)
    instead of compiling this separately.
    """
    write_with_keyboard(['m', VK_DOWN, 'enter', VK_DOWN, VK_DOWN, 'enter'])
    #write_with_keyboard(['m', VK_DOWN, VK_DOWN, 'enter', VK_DOWN, VK_DOWN, 'enter'])

def equip_body_armor():
    """
    Interaction Menu > Inventory > Body Armor > Super Heavy Armor > Exit
    """
    write_with_keyboard(['m', VK_DOWN, 'enter', VK_DOWN, 'enter', VK_UP, VK_UP, VK_UP, 'enter', 'm'])
    #write_with_keyboard(['m', VK_DOWN, VK_DOWN, 'enter', VK_DOWN, 'enter', VK_UP, VK_UP, VK_UP, 'enter', 'm'])

def request_personal_vehicle():
    """
    Interaction Menu > Vehicles > Request Personal Vehicle > Exit
    """
    write_with_keyboard(['m', VK_DOWN, VK_DOWN, VK_DOWN, 'enter', 'enter', 'm'])
    #write_with_keyboard(['m', VK_DOWN, VK_DOWN, VK_DOWN, VK_DOWN, 'enter', 'enter', 'm'])

def toggle_passive_mode():
    """
    Interaction Menu > Enable/Disable Passive Mode > Exit
    """
    write_with_keyboard(['m', VK_UP, 'enter', 'm'])


keyboard.add_hotkey('f1', open_snack_inventory)
keyboard.add_hotkey('f2', equip_body_armor)
keyboard.add_hotkey('f3', request_personal_vehicle)
keyboard.add_hotkey('f4', toggle_passive_mode)

# TODO: Add macro for calling Mors Mutual Insurance, which requires an actual
# wait for the phone to open.
# keyboard.add_hotkey('f5', call_mors_mutual_insurance)

print('Weasom macros ready!')

try:
    keyboard.wait()
except KeyboardInterrupt:
    sys.exit(0)
