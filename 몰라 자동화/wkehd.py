print(pyautogui.size())

time.sleep(2)
print(pyautogui.position())

# mac = 손쉬운 사용 vscode 사용 권한 설정
pyautogui.moveTo(100, 200) # x 100, y 200 위치로 바로 이동
pyautogui.moveTo(100, 200, 2) # x 100, y 200 위치로 2초동안 이동

pyautogui.click()
pyautogui.click(button='right')
pyautogui.doubleClick()
pyautogui.click(clicks=3, interval=1) # 3번 클릭할건데 1초마다

# 816,81 -> 539,80
pyautogui.moveTo(816,81, 2)
pyautogui.dragTo(539,80, 2)