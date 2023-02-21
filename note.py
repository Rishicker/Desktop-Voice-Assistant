import subprocess
import datetime

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    notepad = "C:\WINDOWS\system32\notepad.exe"
    subprocess.call(['notepad.exe', ("C:\\Users\\shukl\\Documents\\Codes\\Python\\" + file_name)])