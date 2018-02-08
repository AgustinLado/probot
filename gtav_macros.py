# coding=utf-8
import sys
import thread
import threading
import time

import keyboard

INTRO_MESSAGE = """Hotkeys activated!  ¯\_(ツ)_/¯

Choose the Interaction Menu mode to switch between:
1: Normal mode (not CEO, Associate, MC President, MC Member or VIP)
2: CEO mode (take a wild guess)
You can toggle on the fly. Cheers!
"""

# These non-standard arrow key codes are DirectInput key codes
VK_UP = 200
VK_LEFT = 203
VK_RIGHT = 205
VK_DOWN = 208


class Cliffford(object):
    """
    The interaction menu sucks.
    Avoid getting lost in it with these weasom macros!

    Are pauses between hotkeys necessary?
    When actively using the macros they'll work fine even without a pause,
    but the first call after X time drops some inputs.
    Maybe a pause will help there.
    TODO: Check if an initial pause or pauses in-between solve that weird issue

    NOTE: Opening and closing the Interaction Menu in a spamming manner ('m')
    takes longer than spamming the other keys and to consistently spam it a
    minimum pause of 0.1 is required, but to do those independently
    the 0.1 pause is NOT required.

    TODO: Add macro for calling Mors Mutual Insurance, which needs a pause
    for the phone to open.
    """
    pause = 0

    ceo_mode = False

    def __init__(self):
        keyboard.add_hotkey('f1', self.open_snack_inventory)
        keyboard.add_hotkey('f2', self.equip_body_armor)
        keyboard.add_hotkey('f3', self.request_personal_vehicle)
        keyboard.add_hotkey('f4', self.toggle_passive_mode)

    def write_with_keyboard(self, keys):
        """
        Wrapper around `keyboard.send` to manage many keys with pauses in the
        middle.
        `keyboard.write` doesn't accept key codes (at least high numbered
        key codes) so it doesn't work.
        `pyautogui` just plain refused to work :(
        """
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
        Starts the `keyboard` wait and a secondary thread that listens to user
        input to update configuration.
        """
        print INTRO_MESSAGE

        # Start input thread
        input_thread = threading.Thread(target=self.get_input)
        input_thread.daemon = True
        input_thread.start()

        try:
            # `keyboard` wait for the hotkeys to work
            keyboard.wait()
        except KeyboardInterrupt:
            print '\nBye!'
            sys.exit(0)

    def get_input(self):
        """
        Intended to be used with `threading`!
        Prompts for user input indefinitely to update the config.
        """
        while 1:
            try:
                user_input = raw_input('$ Choose mode > ')
            except EOFError:
                thread.interrupt_main()

            if user_input == '1':
                self.ceo_mode = False
                print 'Normal mode activated'
            elif user_input == '2':
                self.ceo_mode = True
                print 'CEO mode activated'
            else:
                print '¯\_(ツ)_/¯ Unknown option'


if __name__ == '__main__':
    network_of_supercomputers = Cliffford()
    network_of_supercomputers.main()
