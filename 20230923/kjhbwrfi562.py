import pyautogui
import time

# 클릭할 위치를 지정합니다.
x, y = 500, 500

# 클릭 간격 (초)을 지정합니다.
click_interval = 1

try:
    while True:
        # 마우스를 지정된 위치로 이동합니다.
        pyautogui.moveTo(x, y)
        
        # 마우스를 클릭합니다.
        pyautogui.click()
        
        # 클릭 간격만큼 대기합니다.
        time.sleep(click_interval)
except KeyboardInterrupt:
    print("프로그램을 종료합니다.")
