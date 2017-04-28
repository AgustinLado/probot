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
            pyautogui.moveTo(860, 250)
            pyautogui.click()
            pyautogui.moveTo(960, 250)
            pyautogui.click()
            pyautogui.moveTo(1060, 250)
            pyautogui.click()


defender = DefendTheKeep()
defender.defend()
