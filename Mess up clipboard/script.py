import pyperclip as pc
from random import choice as ch

def mess_it_up(txt):
    lis = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
    l = len(txt)
    mod_txt = ''
    for i in range(l):
        if txt[i] != ' ':
            c = ch(lis)
            mod_txt = mod_txt + c
        else:
            mod_txt = mod_txt + ' '
    return mod_txt

text = pc.paste()
while True:
    new_text = pc.paste()
    if new_text != text:
        new_text = mess_it_up(new_text)
        text = new_text
        pc.copy(text)
        print(text)