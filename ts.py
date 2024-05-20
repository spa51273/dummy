import time


for i in range(10):
    print("",end='\r')
    print(f'Countdown to zero: {9-i}')
    time.sleep(0.3)

