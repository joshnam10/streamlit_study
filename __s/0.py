import pyautogui
import time
import subprocess
# time.sleep(5)
# while 1:
#     pyautogui.press('f5')
#     time.sleep(3)

url='https://www.naver.com/'
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# subprocess.Popen([chrome_path,url])

# subprocess.run(args=['mkdir','abc'], shell=True)
subprocess.run([chrome_path,url])