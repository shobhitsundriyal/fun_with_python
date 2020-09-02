import cv2
import matplotlib.pyplot as plt
import argparse
from random import choice as ch
import pandas

plt.figure(num=None, figsize=(12, 8), facecolor='w', edgecolor='k')
plt.style.use('seaborn')

parser = argparse.ArgumentParser()

parser.add_argument('-n',type=int, default=500, help='Number of sample runs')
args = parser.parse_args() 

n_samples = args.n 

switch_win, switch_lose, stay_win, stay_lose = 0,0,0,0
win_list = [switch_win,stay_win]
label = ['Switch', 'Not Switch']

for i in range(1, args.n+1):

    doors = [0,1,2]
    car_idx = ch(doors)

    guest_ch = ch(doors)

    if guest_ch == car_idx:
        switch_win += 0
        switch_lose += 1
        stay_lose += 0
        stay_win += 1
        win_list[1] = stay_win
    else:
        switch_win += 1
        switch_lose += 0
        stay_lose += 1
        stay_win += 0
        win_list[0] = switch_win
    
    plot = plt.pie(win_list, labels=label)
    plt.text(-2.1, 1, f'Experiment No.: {i}', fontsize=17, bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   ))
    plt.text(1.2, 1, f'Switch Win Ratio: {round(win_list[0]/i, 2)}', fontsize=17,bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   ))
    plt.text(1.2, 0.8, f'Not Switch Win Ratio: {round(win_list[1]/i, 2)}', fontsize=17, bbox=dict(boxstyle="round",
                   ec=(1., 0.5, 0.5),
                   fc=(1., 0.8, 0.8),
                   ))
    plt.savefig('op.png')
    plt.clf()

    img = cv2.imread('op.png')
    cv2.imshow('Should you switch?', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

cv2.waitKey()
cv2.destroyAllWindows()