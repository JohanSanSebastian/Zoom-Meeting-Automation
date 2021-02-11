# Zoom-Meeting-Automated-Joiner

## Overview
This code uses pyautogui and subprocess modules to automate joining zoom meeting

### How does it work?
The code firstly uses the subprocess module to open Zoom Application from your device.

#### **Windows**
```python
    subprocess.call("C:\\Users\\your_name_in_computer\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe") \\ Where Zoom is normally located
```

Then from the assets folder, pyautogui looks for the various buttons & input boxes (like join meeting, enter passords etc.) and clicks or enters data as required.

### How to use it?
Using it is simple, firstly get the code onto you computer and add the various Ids and passwords required in variables (*Please note to avoid sharing these credentials online*) and then to call those variables in the function and also remember to add your zoom path to the subprocess call line.

### Credits
If you are posting this online, please consider crediting this repo.
