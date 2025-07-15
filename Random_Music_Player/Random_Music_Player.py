import playsound
import time
import webbrowser

print('Hello This is Random_Music_Player')
a = input('Please select number (1-3) >>> ')

if a == '1':
    print('This is Salamanca by Sarah2ill')
    time.sleep(2)
    playsound.playsound('1.mp3')
    input('Press Enter to exit program')
    exit()
else:
    if a == '2':
        print('ok..')
        print('This is the best ringtone for your phone.')
        time.sleep(3)
        print('Nokia Arabic Ringtone (Remastered)')
        playsound.playsound('2.mp3')
        time.sleep(2)
        input('Press Enter to exit program')
        exit()
    else:
        if a == '3':
            print('well, this is last one')
            print('But before i end program...')
            print('I want you to know, that this program is made by NotBadli')
            time.sleep(5)
            playsound.playsound('3.mp3')
            webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
            exit()
        else:
            print('I dont see any 1, 2 or 3 number, please try again...')
            time.sleep(4)
            exit()
