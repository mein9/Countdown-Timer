import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r", flush=True)
        time.sleep(1)
        t -= 1
    print('Blast off!!!')

user_time = int(input("Enter the number of seconds: "))
countdown(user_time)