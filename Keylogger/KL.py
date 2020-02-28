from  pynput.keyboard import Listener, Key#read more

def on_press(key):
    print('Key {} pressed.'.format(key))

log = ''

def on_release(key):
    global log
    log = log + str(key.char)
    print(log)
    if str(key) == 'Key.esc':
        print('Exiting...')
        return False

with Listener(on_press=on_press, on_release=on_release) as listen:
    listen.join()


