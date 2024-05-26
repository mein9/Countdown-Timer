import time

def countdown(time_input):
    if isinstance(time_input, int):
        while time_input:
            mins, secs = divmod(time_input, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r", flush=True)
            time.sleep(1)
            time_input -= 1
        print('Blast off!!!')
    else:
        print("Please enter a number")
while True:
    user_time = input("Enter the number of seconds: ")
    if user_time.isdigit():
        user_time = int(user_time)
        countdown(user_time)
        break
    else:
        print("Please enter a valid number.")