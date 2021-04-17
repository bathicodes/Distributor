import os
from pathlib import Path

path = r'/Users/bathiyaseneviratne/Desktop/Distributor'

def sorter(path):
    dirpath = Path(path)
    for files in dirpath.iterdir():
        if files.suffix in [".rtfd",".rtf",".pdf",".doc",".docx",".pdf",".odt",".txt",".tex",".wpd"]:
            os.replace(files,f"/Users/bathiyaseneviratne/Documents/{files.name}")
        elif files.suffix in [".mp3",".aif",".cda",".mid",".midi",".mpa",".ogg",".wav",".wma",".wpi"]:
            os.replace(files,f"/Users/bathiyaseneviratne/Music/{files.name}")
        elif files.suffix in [".png",".jpg",".jpeg",".tif", ".tiff",".bmp",".gif",".eps"]:
            os.replace(files,f"/Users/bathiyaseneviratne/Pictures/{files.name}")
        elif files.suffix in [".3g2",".3gp",".avi",".flv",".h264",".m4v",".mkv",".mov",".mp4",".mpg",".mpeg",".rm",".swf",".vob",".wmv"]:
            os.replace(files,f"/Users/bathiyaseneviratne/Movies/{files.name}")
       

    