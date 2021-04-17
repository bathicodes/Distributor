import os
from pathlib import Path

path = r'/Users/bathiyaseneviratne/Desktop/Distributor'

def sorter(path):
    dirpath = Path(path)
    for files in dirpath.iterdir():
        if files.suffix in [".rtfd",".rtf",".pdf",".doc",".docx",".pdf",".odt",".txt",".tex",".wpd"]:
            print("doc file")
        elif files.suffix in [".mp3",".aif",".cda",".mid",".midi",".mpa",".ogg",".wav",".wma",".wpi"]:
            print("music")
        elif files.suffix in [".png",".jpg",".jpeg",".tif", ".tiff",".bmp",".gif",".eps"]:
            print("Image")
        elif files.suffix in [".3g2",".3gp",".avi",".flv",".h264",".m4v",".mkv",".mov",".mp4",".mpg",".mpeg",".rm",".swf",".vob",".wmv"]:
            print("video")
       

    