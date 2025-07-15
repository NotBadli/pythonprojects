import time, pafy, vlc

print('Timer started')
time.sleep(5)
print('Half way there')
time.sleep(5)

url = 'https://www.youtube.com/watch?v=UIBsSo0wSsU&ab_channel=FreeToUseSound%E2%80%94Royaltyfreesoundeffects'                                                                                         
video = pafy.new(url)                                                                                                                       
best = video.getbestaudio()                                                                                                                 
playurl = best.url                                                                                                                          
player = vlc.MediaPlayer(playurl) 
player.play()
time.sleep(17)