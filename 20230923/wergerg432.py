import pyautogui
import time

pyautogui.moveTo(1070, 1050)
pyautogui.click()

time.sleep(1)
pyautogui.moveTo(717, 54)
pyautogui.click()

time.sleep(0.3)
pyautogui.typewrite('https://warthunder.com/ko/', interval=0.008)

time.sleep(0.3)
pyautogui.press('enter')

time.sleep(1)
pyautogui.moveTo(780, 500)
pyautogui.click()

time.sleep(1)
pyautogui.scroll(-1400)

time.sleep(0.5)
pyautogui.moveTo(780, 500)
pyautogui.click()

time.sleep(2)
pyautogui.scroll(-700)

time.sleep(0.05)
pyautogui.moveTo(486, 608)

time.sleep(0.05)
pyautogui.dragTo(750, 701, 1)

#메모
time.sleep(0.3)
pyautogui.moveTo(683, 54)
pyautogui.click()

time.sleep(0.3)
pyautogui.moveTo(671, 1054)
pyautogui.click()

time.sleep(0.3)
pyautogui.moveTo(717, 465)
pyautogui.click()

time.sleep(0.3)
pyautogui.moveTo(911, 614)
pyautogui.click()
