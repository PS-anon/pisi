import os

muzi = 'Unde e ea'

os.system(f"youtube-dl  -x --audio-format mp3 -o 'muzica.%(ext)s' 'ytsearch1:{muzi}'")
