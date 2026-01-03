import pyautogui
import time
import subprocess

notepad="notepad.exe"
subprocess.Popen([notepad])
print('d')

time.sleep(1)
pyautogui.press('a')
time.sleep(1)
pyautogui.press('b')
time.sleep(1)
pyautogui.press('c')
time.sleep(1)
pyautogui.hotkey('ctrl','s')
time.sleep(1)
pyautogui.press('a')
pyautogui.press('.')
pyautogui.press('t')
pyautogui.press('x')
pyautogui.press('t')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)

pyautogui.hotkey('alt','f4')

