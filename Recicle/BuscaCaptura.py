import pyautogui
import time

img = 'Papel.png'
img1 = 'Papelao.png'
img2 = 'Plastico.png'
img3 = 'vidro.png'

while True:
    if pyautogui.locateOnScreen(img, confidence=0.80):
        print('Papel')
        time.sleep(1)
    elif pyautogui.locateOnScreen(img1, confidence=0.80):
        print('Papelao')
        time.sleep(1)
    elif pyautogui.locateOnScreen(img2, confidence=0.80):
        print('Plastico')
        time.sleep(1)
    elif pyautogui.locateOnScreen(img3, confidence=0.80):
        print('Vidro')
        time.sleep(1)
    else:
        print('Não encontrado')
