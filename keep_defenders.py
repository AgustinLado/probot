import pyautogui


class DefendTheKeep(object):
    """
    Play Keep Defenders by Marccio Silva.
    https://marcciosilva.itch.io/keep-defenders

    Just click the damn buttons!

    I guess hardcoding the location on the screen wasn't my best moment, hehe.
    Leave me be, it was just a test!
    TODO: Use `pyautogui.locateOnScreen` to get some reference coordinates and
    calculate where to click from there.
    TODO: Add a way to stop it.
    """
    def defend(self):
        pyautogui.PAUSE = 0.01
        while True:
            pyautogui.click(860, 250)
            pyautogui.click(960, 250)
            pyautogui.click(1060, 250)


defender = DefendTheKeep()
defender.defend()
