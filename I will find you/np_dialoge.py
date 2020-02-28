from  pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(2)

keyboard.press(Key.cmd)
keyboard.release(Key.cmd)

time.sleep(1)
for c in 'note':
    keyboard.press(c)
    keyboard.release(c)
    time.sleep(0.15)  

keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(2)

for c in 'I will find you and I will hack you':
    keyboard.press(c)
    keyboard.release(c)
    time.sleep(0.09)
