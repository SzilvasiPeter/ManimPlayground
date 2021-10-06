# ManimPlayground
Manim playground to create educational videos for college students.

## Environment setup
First we need couple of packages for example the **_manim_** package.
```
pip install requirements.txt
```
Then we need ffmpeg in order to create the media files.
- Installing ffmpeg for windows: [ffmpeg windows](https://www.wikihow.com/Install-FFmpeg-on-Windows)
- Installing ffmpeg for linux: [ffmpeg windows](https://linuxize.com/post/how-to-install-ffmpeg-on-ubuntu-18-04/)

Now we are able to create animation. Change the directory to the scene.py script. The following command will create a media file under _/media/videos/_ folder:
```
manim -pql .\scene.py BouncingBacteria
```
Change the _l_ (low) parameter to _h_ (high) for better quality.

Bouncing Bacteriums in action 😊
![](BouncingBacteria.gif)
