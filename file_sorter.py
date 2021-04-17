import os
from pathlib import Path
from environment import *

path = path()

def sorter(path):
    dirpath = Path(path)
    for files in dirpath.iterdir():
        # check if the file is document or not. if it is moveing it to the document folder
        if files.suffix in [".rtfd",".rtf",".pdf",".doc",".docx",".pdf",".odt",".txt",".tex",".wpd"]:
            os.replace(files,f"/Users/bathiyaseneviratne/Documents/{files.name}")
        # check if the file is audio or not. if it is moveing it to the Music folder
        elif files.suffix in [".mp3",".aif",".cda",".mid",".midi",".mpa",".ogg",".wav",".wma",".wpi"]:
            os.replace(files,f"/Users/bathiyaseneviratne/Music/{files.name}")
        # check if the file is Image or not. if it is moveing it to the Pictures folder
        elif files.suffix in [".png",".jpg",".jpeg",".tif", ".tiff",".bmp",".gif",".eps"]:
            os.replace(files,f"/Users/bathiyaseneviratne/Pictures/{files.name}")
        # check if the file is Movie or not. if it is moveing it to the Movies folder
        elif files.suffix in [".3g2",".3gp",".avi",".flv",".h264",".m4v",".mkv",".mov",".mp4",".mpg",".mpeg",".rm",".swf",".vob",".wmv"]:
            os.replace(files,f"/Users/bathiyaseneviratne/Movies/{files.name}")
       

    