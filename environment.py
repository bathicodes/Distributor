from pathlib import Path

# -------------------- path_osx for mac os -------------------- #
home_osx = str(Path.home())

def path_osx():
    return f"{home_osx}/Desktop/Distributor"
     
def documents_osx():
    return f"{home_osx}/Documents/"

def music_osx():
    return f"{home_osx}/Music/"

def pictures_osx():
    return f"{home_osx}/Pictures/"

def movies_osx():
    return f"{home_osx}/Movies/"