import pyautogui, sys, time

i = 0
x = 1475
y = 785
time.sleep(2)
try:
    while i < 100:
        # pyautogui.click(929,202)
        # 点击开始
        pyautogui.click(x, y)
        print("第" + str(i + 1) + "次")
        time.sleep(0.5)
        pyautogui.click(x, y)
        # 预计打完需要42s
        time.sleep(45)
        # 点击出御魂
        pyautogui.click(x, y)
        time.sleep(3)
        pyautogui.click(x, y)
        time.sleep(2)
        pyautogui.click(x, y)
        time.sleep(1)
        pyautogui.click(x, y)
        i += 1
except Exception as e:
    print(e)
    sys.exit(0)

