import time
import webbrowser
import random

def Link():
    if x == 1:
        webbrowser.open('https://www.youtube.com/watch?v=0-Tm65i96TY&list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI&index=1')
    else:
        if x == 2:
            webbrowser.open('https://www.youtube.com/watch?v=oh64haEP9g8&list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI&index=7')
        else:
            if x == 3:
                webbrowser.open('https://www.youtube.com/watch?v=KIK3azN4w34&list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI&index=11')
            else:
                if x == 4:
                    webbrowser.open('https://www.youtube.com/watch?v=3niVHCdB1wA&list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI&index=13')
                else:
                    if x == 5:
                        webbrowser.open('https://www.youtube.com/watch?v=5-FGxUINL-Q&list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI&index=42')
                    else:
                        if x == 6:
                            webbrowser.open('https://www.youtube.com/watch?v=qevfciMnCS4&list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI&index=40')
                        else:
                            if x == 7:
                                webbrowser.open('https://www.youtube.com/watch?v=g_GKoivutyU&list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI&index=36')
                            else:
                                if x == 8: 
                                    webbrowser.open('https://www.youtube.com/watch?v=vBHild0PiTE&list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI&index=34')
                                else:
                                    if x == 9:
                                        webbrowser.open('https://www.youtube.com/watch?v=L0X03zR0rQk&list=PLFgquLnL59alCl_2TQvOiD5Vgm1hCaGSI&index=35')
                                    else:
                                        if x == 10:
                                            webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
                                        else:
                                            print('Something Went Wrong')
                                            time.sleep(2)
                                            exit()

print('Welcome to Random_Music player, By Illia Semochko')
time.sleep(3)
input('Press Enter to Continue')

x = random.randrange(1, 10)

Link()

exit()