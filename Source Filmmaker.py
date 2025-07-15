import os
import time

import pywintypes
import win32api
import win32con

devmode = pywintypes.DEVMODEType()
devmode.PelsWidth = 1280
devmode.PelsHeight = 720
devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT
win32api.ChangeDisplaySettings(devmode, 0)

time.sleep(2)

os.startfile('C:\\Program Files (x86)\\Steam\\steamapps\\common\\SourceFilmmaker\\game\\sfm.exe')

input('Press Enter >>> ')
win32api.ChangeDisplaySettings(None, 0)

time.sleep(1)

exit()
