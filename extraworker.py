import os, sys
import uuid
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.compositing.concatenate import concatenate_videoclips
from loader import uploader

def exw(nameclip, nametxttoload):
    tempname = f"content\Temp\{str(uuid.uuid4())}"
    namecliptoload = f"{tempname}done.mp4"

    video = VideoFileClip(nameclip)
    dur = video.duration
    print(round(dur))
    logo = (ImageClip("wm.png")
              .set_duration(dur)
              .set_pos(("center","bottom")))

    final = CompositeVideoClip([video, logo])
    final.write_videofile(f"{tempname}done.mp4", audio=True)

    if round(dur) < 600:
        sys.exit(1)
    elif round(dur) < 1200:
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(15, 17)
        final1.write_videofile(f'{tempname}cut.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(70, 72)
        final1.write_videofile(f'{tempname}cut1.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(100, 102)
        final1.write_videofile(f'{tempname}cut2.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(160, 162)
        final1.write_videofile(f'{tempname}cut3.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(200, 202)
        final1.write_videofile(f'{tempname}cut4.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(300,302)
        final1.write_videofile(f'{tempname}cut5.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(400, 402)
        final1.write_videofile(f'{tempname}cut6.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(500, 502)
        final1.write_videofile(f'{tempname}cut7.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(600, 602)
        final1.write_videofile(f'{tempname}cut8.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(700, 702)
        final1.write_videofile(f'{tempname}cut9.mp4', audio=False)

    elif round(dur) < 2460:
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(15, 17)
        final1.write_videofile(f'{tempname}cut.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(70, 72)
        final1.write_videofile(f'{tempname}cut1.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(200, 202)
        final1.write_videofile(f'{tempname}cut2.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(360, 362)
        final1.write_videofile(f'{tempname}cut3.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(400, 402)
        final1.write_videofile(f'{tempname}cut4.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(500,502)
        final1.write_videofile(f'{tempname}cut5.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(600, 602)
        final1.write_videofile(f'{tempname}cut6.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(700, 702)
        final1.write_videofile(f'{tempname}cut7.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(800, 802)
        final1.write_videofile(f'{tempname}cut8.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(900, 902)
        final1.write_videofile(f'{tempname}cut9.mp4', audio=False)

    elif round(dur) < 3600:
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(35, 37)
        final1.write_videofile(f'{tempname}cut.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(100, 102)
        final1.write_videofile(f'{tempname}cut1.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(300, 302)
        final1.write_videofile(f'{tempname}cut2.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(560, 562)
        final1.write_videofile(f'{tempname}cut3.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(700, 702)
        final1.write_videofile(f'{tempname}cut4.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(900, 902)
        final1.write_videofile(f'{tempname}cut5.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(1200, 1202)
        final1.write_videofile(f'{tempname}cut6.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(1400, 1402)
        final1.write_videofile(f'{tempname}cut7.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(1600, 1602)
        final1.write_videofile(f'{tempname}cut8.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(1800, 1802)
        final1.write_videofile(f'{tempname}cut9.mp4', audio=False)

    else:
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(55, 57)
        final1.write_videofile(f'{tempname}cut.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(100, 102)
        final1.write_videofile(f'{tempname}cut1.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(300, 302)
        final1.write_videofile(f'{tempname}cut2.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(560, 562)
        final1.write_videofile(f'{tempname}cut3.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(700, 702)
        final1.write_videofile(f'{tempname}cut4.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(900, 902)
        final1.write_videofile(f'{tempname}cut5.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(1200, 1202)
        final1.write_videofile(f'{tempname}cut6.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(1400, 1402)
        final1.write_videofile(f'{tempname}cut7.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(1600, 1602)
        final1.write_videofile(f'{tempname}cut8.mp4', audio=False)
        final1 = VideoFileClip(f"{tempname}done.mp4").subclip(1700, 1702)
        final1.write_videofile(f'{tempname}cut9.mp4', audio=False)


    clip1 = VideoFileClip(f"{tempname}cut.mp4")
    clip2 = VideoFileClip(f"{tempname}cut1.mp4")
    clip3 = VideoFileClip(f"{tempname}cut2.mp4")
    clip4 = VideoFileClip(f"{tempname}cut3.mp4")
    clip5 = VideoFileClip(f"{tempname}cut4.mp4")
    clip6 = VideoFileClip(f"{tempname}cut5.mp4")
    clip7 = VideoFileClip(f"{tempname}cut6.mp4")
    clip8 = VideoFileClip(f"{tempname}cut7.mp4")
    clip9 = VideoFileClip(f"{tempname}cut8.mp4")
    clip10 = VideoFileClip(f"{tempname}cut9.mp4")
    final_clip = concatenate_videoclips([clip1,clip2,clip3,clip4,clip5,clip6,clip7,clip8,clip9,clip10])
    final_clip.write_videofile(nameclip)
    print(nameclip)
    print(namecliptoload)
    print(nametxttoload)
    os.remove(f"{tempname}cut.mp4")
    os.remove(f"{tempname}cut1.mp4")
    os.remove(f"{tempname}cut2.mp4")
    os.remove(f"{tempname}cut3.mp4")
    os.remove(f"{tempname}cut4.mp4")
    os.remove(f"{tempname}cut5.mp4")
    os.remove(f"{tempname}cut6.mp4")
    os.remove(f"{tempname}cut7.mp4")
    os.remove(f"{tempname}cut8.mp4")
    os.remove(f"{tempname}cut9.mp4")
    uploader(nameclip, namecliptoload,nametxttoload)
    subprocess.Popen(['loader.exe', nameclip, "content/Temp/1.mp4", nametxttoload])

if __name__ == '__main__':
    if len(sys.argv[1:]) < 0:
        print("[ERROR] Argument expected")
        sys.exit(1)
    else:
        main()