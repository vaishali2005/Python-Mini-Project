import time
from datetime import datetime

def countdown():
    t = int(input('Enter you time limit : '))
    while t:
        mins , secs = divmod(t , 60)
        #print('{mins} : {secs}')
        print('{:02d} : {:02d}'.format(mins,secs))
        time.sleep(1)
        t -= 1
    #print(display)

now = datetime.now()
print(now)
cTime = now.strftime('%H : %M : %S')
print(cTime)
countdown()
        