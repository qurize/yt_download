v = "v.0-"
# print(v)
from pytube import YouTube

url = "https://music.youtube.com/watch?v=J1xXu-18Zb0&list=OLAK5uy_mNuiuW4Eg8WiWEDY4r8Tjrh6CiinagQvg"

vdo = YouTube(url)

print(vdo.title)
print(vdo.thumbnail_url)

#vdo = vdo.streams.get_highest_resolution()
audio = vdo.streams.get_audio_only()
# vdo = vdo.streams.first()
# vdo = vdo.streams.last()

#vdo.download()
audio.download()
print("End")
