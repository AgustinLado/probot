import pyautogui


class DefendTheKeep(object):
    """
    Play Keep Defenders by Marccio Silva.
    https://marcciosilva.itch.io/keep-defenders

    Just click the damn buttons!
    """
    def defend(self):
        pyautogui.PAUSE = 0.01
        while True:
            pyautogui.click(860, 250)
            pyautogui.click(960, 250)
            pyautogui.click(1060, 250)


defender = DefendTheKeep()
defender.defend()
