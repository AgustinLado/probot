# PRObot
Tiny bot that plays stuff or makes stuff easier. Or maybe eventually some DeepMind knockoff thingie that is able to play any game better than any human or otherwise!


## Scripts

### Grand Theft Auto V
Tired of using that damn Interaction Menu? Avoid it completely with these sick macros! You won't believe number 4!

*NOTE: Notice it working weird? It seems that after not calling any hotkeys for a while Windows de-prioritizes the script or something, garbling the next hotkey presses.
Attempts to minimize the issue are WIP.*

### Plants vs Zombies
Avoid tendinitis with this simple keyboard plant selector. Doctors hate it!


## Addendum

### How to run
`keyboard` requires root privileges to run on Linux, so after installing with [Pipenv](https://pipenv.readthedocs.io/en/latest/) run

    sudo pipenv run python gtav_macros.py

### How to use on Windows *(without installing Python)*
I wanted to make a portable Windows version of these scripts to avoid installing Python and any other project dependencies on it.

The simplest way I found was using [PyInstaller](http://www.pyinstaller.org/) to create the executable. There's a caveat, though: cross-platform compilation was removed on a previous version, so to build an executable for Windows PyInstaller has to be running on Windows -\_\-

Of course I was not to give up, so I installed [Wine](https://www.winehq.org) to be able to build the .exe on Linux, which hilariously I'm running in a virtual machine. So to avoid installing Python on Windows I wound up calling PyInstaller inside Wine inside Linux inside a VM inside Windows.

Anyway, if you're stupid like me install Wine, install the project dependencies and PyInstaller in a Wine prefix and run

    wine pyinstaller -F --clean -p ~/.virtualenvs/probot/lib/python2.7/site-packages/ gtav_macros.py

### How to unbind keys in GTAV
Keys normally cannot be unbound in GTAV, which bothers me to no end. But I found a way: binding them to non-existent keys!

    import keyboard
    def send_key(code):
        # For some reason GTA doesn't catch the keys unless they're sent in quick succession.
        while True:
            keyboard.send(code)

The keys I use:
* Yes, F13 through 15
* 100 - DIK_F13
* 101 - DIK_F14
* 102 - DIK_F15
* ???s
* 112 - DIK_KANA
* 121 - DIK_CONVERT
* 123 - DIK_NOCONVERT
* 125 - DIK_YEN
* 148 - DIK_KANJI
