import pyperclip as pc
from random import choice as ch

def mess_it_up(txt):
    lis = ['1','3','2']
    l = len(txt)
    mod_txt = ''
    for i in range(l):
        c = ch(lis)
        mod_txt = mod_txt + c
    return mod_txt

text = pc.paste()
while True:
    new_text = pc.paste()
    if new_text != text:
        new_text = mess_it_up(new_text)
        text = new_text
        pc.copy(text)
        print(text)