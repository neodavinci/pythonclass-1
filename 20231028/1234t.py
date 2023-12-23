import pyperclip
import time
import pyautogui

#http://www.lego-lo.com/
#pyperclip.copy

time.sleep(1)
pyautogui .moveTo(800, 1060)
pyautogui.click(button='left')

time.sleep(1)
pyautogui.write('chrome')

time.sleep(1.5)
pyautogui .moveTo(825, 430)
pyautogui.click(button='left')

time.sleep(1.5)
pyautogui .moveTo(550, 60)
pyautogui.click(button='left')

time.sleep(1.5)
pyautogui.write('http://www.lego-lo.com/')

time.sleep(1.5)
pyautogui.press( 'enter')

time.sleep(1.5)
pyautogui .moveTo(1242, 227)
pyautogui.click(button='left')

time.sleep(1.5)
pyautogui . scroll(-1500)

time.sleep(1.5)
pyautogui .moveTo(1320, 227)
pyautogui.click(button='left')

time.sleep(1.5)
pyautogui .moveTo(1250, 1060) 
pyautogui.click(button='left')

time.sleep(1.5)
pyautogui .moveTo(1087, 255) 
pyautogui.click(button='left')

pyautogui.hotkey('ctrl', 'K_DOWN')















#pygame.

#pyautogui .moveTo(100, 200) # x 100, y 280 위치로 바로 이동
#pyautogui.click(button='left') #왼쪽버튼 클릭
#pyautogui.doubleclick() #더블를릭
#pyautogui.write('text') # text를 입력
#pyautogui.press( 'enter') # enter 키를 누릅니다.
#pyautogui.dragTo(539,80, 2) # 539,80까지 드래그를 2최능 안하기.
# # 붙여넣기 (hotkey 설명은 아래어 있습니델
#pyautogui . scroll(500) #500만큼스크롤
#pyautogui.keyDown( 'ctrl') # ctr1 키를 누른 상태를 유지합니다.
#pyautogui.keyup('ctrl') # ctr1 키를 댑니다.