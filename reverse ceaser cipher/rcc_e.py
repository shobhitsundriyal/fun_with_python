message = 'This is simpler than normal Ceaser chipher.'
translated = ''
i = len(message) - 1

while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)