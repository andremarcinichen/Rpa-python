import pyautogui as p


#Localizacao do mouse

# while True:
#     p.sleep(0.1)
#     print(p.position());


# movimentacao do mouse
# p.moveTo(19,35,duration=3)

#ativar teclado
p.hotkey('win','r')
p.typewrite('notepad')
p.press('enter')
p.sleep(0.1)
p.typewrite("hello world!")
# valor= p.getActiveWindow()
# valor.close()
p.sleep(0.1)
p.getActiveWindow().close()
p.sleep(0.1)
p.press('right')
p.sleep(0.1)
p.press('enter')