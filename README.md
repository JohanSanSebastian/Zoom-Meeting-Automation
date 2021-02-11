# Zoom-Meeting-Automated-Joiner

## Overview
This code uses pyautogui and subprocess modules to automate joining zoom meeting. I have included two versions where one just joins a meeting and version-2 has the option to join multiple meeting based on choice

### How does it work?
The code firstly uses the subprocess module to open Zoom Application from your device.

#### **Windows**
```python
    subprocess.call("C:\\Users\\your_name_in_computer\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe") # Where Zoom is normally located
```

Then from the assets folder, pyautogui looks for the various buttons & input boxes (like join meeting, enter passords etc.) and clicks or enters data as required.

### How to use it?
Using it is simple, firstly download the code and assets folder onto you computer and add the various Ids and passwords required in variables in the file (*Please note to avoid sharing these credentials online*), and then call those variables in the function and also remember to add your zoom path to the subprocess call line.

### Credits
If you are posting this online, please consider crediting this repo.
