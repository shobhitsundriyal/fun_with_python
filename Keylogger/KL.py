from  pynput.keyboard import Listener, Key#read more

#def on_press(key):
#    print(key)

log = ''

def on_release(key):
    global log
    log = log + key
    print(log)
    if str(key) == 'Key.esc':
        print('Exiting...')
        return False

with Listener(on_release=on_release) as listen:
    listen.join()


