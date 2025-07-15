import os
import time

import pywintypes
import win32api
import win32con

time.sleep(3)

devmode = pywintypes.DEVMODEType()
devmode.PelsWidth = 1600
devmode.PelsHeight = 900
devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
win32api.ChangeDisplaySettings(devmode, 0)

time.sleep(2)

os.startfile('C:\\Users\\notbadli\\Downloads\\Red.Dead.Redemption.2.Fixed\\Red.Dead.Redemption.2.Fixed\\Red Dead Redemption 2\\RDR2.exe')

input('Press Enter >>> ')
win32api.ChangeDisplaySettings(None, 0)

time.sleep(1)

exit()
