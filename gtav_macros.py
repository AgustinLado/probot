# coding=utf-8
import sys
import threading
import time

import keyboard

# TODO: Make these unicode thingies work in Windows ┻━┻ ︵ヽ(`Д´)ﾉ︵﻿ ┻━┻
INTRO_MESSAGE = """Hotkeys activated!  (☞ﾟヮﾟ)☞

Switch the Interaction Menu mode between:
1: Normal mode (not CEO, Associate, MC President, MC Member or VIP)
2: CEO mode (take a wild guess)

Other options:
p: Set the pause between key strokes (in seconds)
ip: Set the initial pause before writing (in seconds)

You can set the values on the fly. Cheers!
"""

# DirectInput key codes
VK_UP = 200
VK_LEFT = 203
VK_RIGHT = 205
VK_DOWN = 208
# Unassigned key code in both Windows and DirectInput
VK_BOGUS = 204


class Cliffford(object):
    """
    The interaction menu sucks.
    Avoid getting lost in it with these weasom macros!

    - Are pauses between hotkeys necessary? -
    When actively using the macros they'll work fine even without a pause,
    but the first call after X time drops some inputs.
    Possible solutions:
      - A large initial pause that comes into play only after a certain time
        has passed since the last hotkey press.
        (TODO)
      - Maybe simulating a bogus key press would help in keeping the script
        "warmed up". It does seem like `keyboard` takes its time after not being
        used for a while.
        (EDIT: Feels like it helped somewhat. Maybe helps reduce the necessary
        initial pause).

    TODO: Add macro for calling Mors Mutual Insurance, which needs a pause
    for the phone to open.
    """
    pause = 0
    initial_pause = 0

    ceo_mode = False

    def __init__(self):
        keyboard.add_hotkey('f1', self.open_snack_inventory)
        keyboard.add_hotkey('f2', self.equip_body_armor)
        keyboard.add_hotkey('f3', self.request_personal_vehicle)
        keyboard.add_hotkey('f4', self.toggle_passive_mode)
        # Bogus function to keep the script warmed up
        keyboard.add_hotkey(VK_BOGUS, lambda: None)

    def write_with_keyboard(self, keys):
        """
        Wrapper around `keyboard.send` to manage many keys with pauses before
        and between the strokes.
        `keyboard.write` doesn't accept key codes (at least high numbered
        key codes) so it doesn't work.
        `pyautogui` just plain refused to work :(
        """
        if self.initial_pause:
            time.sleep(self.initial_pause)
        for key in keys:
            keyboard.send(key)
            if self.pause:
                time.sleep(self.pause)

    def open_snack_inventory(self):
        """
        Interaction Menu > Inventory > Snacks
        """
        if self.ceo_mode:
            self.write_with_keyboard([
                'm',
                VK_DOWN, VK_DOWN, 'enter',
                VK_DOWN, VK_DOWN, 'enter',
            ])
        else:
            self.write_with_keyboard([
                'm',
                VK_DOWN, 'enter',
                VK_DOWN, VK_DOWN, 'enter',
            ])

    def equip_body_armor(self):
        """
        Interaction Menu > Inventory > Body Armor > Super Heavy Armor > Exit
        """
        if self.ceo_mode:
            self.write_with_keyboard([
                'm',
                VK_DOWN, VK_DOWN, 'enter',
                VK_DOWN, 'enter',
                VK_UP, VK_UP, VK_UP, 'enter',
                'm',
            ])
        else:
            self.write_with_keyboard([
                'm',
                VK_DOWN, 'enter',
                VK_DOWN, 'enter',
                VK_UP, VK_UP, VK_UP, 'enter',
                'm',
            ])

    def request_personal_vehicle(self):
        """
        Interaction Menu > Vehicles > Request Personal Vehicle > Exit
        """
        if self.ceo_mode:
            self.write_with_keyboard([
                'm',
                VK_DOWN, VK_DOWN, VK_DOWN, VK_DOWN, 'enter',
                'enter',
                'm',
            ])
        else:
            self.write_with_keyboard([
                'm',
                VK_DOWN, VK_DOWN, VK_DOWN, 'enter',
                'enter',
                'm',
            ])

    def toggle_passive_mode(self):
        """
        Interaction Menu > Enable/Disable Passive Mode > Exit
        """
        self.write_with_keyboard([
            'm',
            VK_UP, 'enter',
            'm',
        ])

    def main(self):
        """
        Starts the `keyboard` wait, a secondary thread that listens to user
        input to update configuration and a third "keep alive" thread.
        """
        print INTRO_MESSAGE

        # `keyboard` wait for the hotkeys to work
        input_thread = threading.Thread(target=keyboard.wait)
        input_thread.daemon = True
        input_thread.start()

        # Keep alive thread to keep the script warmed up
        keep_alive_thread = threading.Thread(target=self.simulate_hotkey)
        keep_alive_thread.daemon = True
        keep_alive_thread.start()

        try:
            # Keep the input, the direct user interaction, in the main thread
            self.get_input()
        except KeyboardInterrupt:
            print '\nBye!'
            sys.exit(0)

    def get_input(self):
        """
        Intended to be used with `threading`!
        Prompts for user input indefinitely to update the config.
        """
        while 1:
            user_input = raw_input('\n$ Choose mode > ')

            # Interaction Menu modes
            if user_input == '1':
                self.ceo_mode = False
                print 'Normal mode activated'
            elif user_input == '2':
                self.ceo_mode = True
                print 'CEO mode activated'

            # Pause options
            elif user_input == 'p':
                self.pause = raw_input_positive_number(
                    '  $ Pause between strokes > ',
                    'Pause set to {0} seconds')
            elif user_input == 'ip':
                self.initial_pause = raw_input_positive_number(
                    '  $ Pause before writing > ',
                    'Initial pause set to {0} seconds')

            else:
                print '¯\_(ツ)_/¯'

    def simulate_hotkey(self):
        """
        Call a bogus hotkey periodically as to keep the process "warmed up".
        This comes from the observation that after not calling any macros for
        a while the first call fails (maybe it executes too fast, maybe it
        drops inputs, dunno).
        """
        while 1:
            time.sleep(3)
            keyboard.send(VK_BOGUS)

def raw_input_positive_number(prompt, success_message):
    """
    Ensure the raw_input is a valid positive number.
    Doesn't return a value if it's invalid.
    """
    value = raw_input(prompt)
    try:
        value = float(value)
        if value >= 0:
            print success_message.format(value)
            return value
        else:
            raise ValueError
    except ValueError:
        print "(╯°□°）╯︵ ┻━┻ That's not a valid number!"


if __name__ == '__main__':
    network_of_supercomputers = Cliffford()
    network_of_supercomputers.main()
