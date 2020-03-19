import random
import webbrowser
import time

sites = ['google.com', 'fb.com', 'yahoo.com', 'bing.com', 'nokia.com', 'apple.com']

while True:
    site = random.choice(sites)
    vist = 'https://{}'.format(site)
    webbrowser.open(vist)
    sleep_for = random.randrange(5,10)
    time.sleep(sleep_for)