import pyautogui
import time

time.sleep(1)
pyautogui.hotkey('ctrl','start','left arrow key')


time.sleep(1)
pyautogui.hotkey('alt','tab')

pyautogui.moveTo(90, 258)
pyautogui.click()
pyautogui.hotkey('ctrl','c')

pyautogui.moveTo(90, 258) #번호의 좌표로 수정.
pyautogui.click()
pyautogui.hotkey('ctrl','v')
pyautogui.hotkey('alt','tab')