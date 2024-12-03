
import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc
import time
# Создаем объект плеера и указываем ссылку на аудио
player = vlc.MediaPlayer("https://storage.yandexcloud.net/mediacloud/3AD3966F-4DF7-42D7-8138-007094E7D61C/F0965479-5763-4DAF-BAE7-0165CADA1155.MP3")

# Воспроизведение аудио
player.play()

# Основной цикл для ожидания завершения воспроизведения
while True:
    state = player.get_state()
    # Если плеер находится в состоянии воспроизведения или буферизации, продолжаем цикл
    if state in [vlc.State.Playing, vlc.State.Buffering]:
        continue
    # Если воспроизведение закончено или произошла ошибка, выходим из цикла
    elif state in [vlc.State.Ended, vlc.State.Error]:
        break