import time, os
from playsound import playsound

def timer_function():
    print('Timer started')
    sound_dir = os.path.join(os.getcwd(), 'Sounds')
    print(sound_dir)
    playsound(os.path.join(os.getcwd(), 'Sounds\\1.mp3'))

    time.sleep(900)
    print('Almost half way there')
    playsound('C:/Users/illia/OneDrive/Documents/Python/Monitor_Timer/2.mp3')

    time.sleep(900)
    print('Half way there')  
    playsound('C:/Users/illia/OneDrive/Documents/Python/Monitor_Timer/2.mp3')  

    time.sleep(900)
    print('More than half way there')
    playsound('C:/Users/illia/OneDrive/Documents/Python/Monitor_Timer/2.mp3')

    time.sleep(900)
    print('Do something else')
    playsound('C:/Users/illia/OneDrive/Documents/Python/Monitor_Timer/1.mp3')

    time.sleep(600)
    playsound('C:/Users/illia/OneDrive/Documents/Python/Monitor_Timer/1.mp3')

    print('Now you can use computer again')
    time.sleep(3)

    input('Start timer again?')
    os.system('cls')
    time.sleep(1.5)

while True:
    timer_function()