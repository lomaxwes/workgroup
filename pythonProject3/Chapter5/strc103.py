names = ['olya', 'ema', 'petya', 'admin', 'tupic', 'egor', 'sasha']
if len(names) == 0:
    print('We need to ind some users!')
for name in names:
    if name == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {name}, thank you for logging in again')
