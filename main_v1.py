import pyautogui
import subprocess
import time


def joinMeeting(meeting_id, meeting_pass):
    
    subprocess.call("your_zoom_location") # Opens Zoom
    
    joinMeetBTN = pyautogui.locateCenterOnScreen("assets/joinMeetingBTN.png") # Join Meeting
    pyautogui.moveTo(joinMeetBTN)
    pyautogui.click()
    time.sleep(1)

    meetingIdBTN = pyautogui.locateCenterOnScreen("assets/enterID.png") # Meeting ID
    pyautogui.moveTo(meetingIdBTN)
    pyautogui.write(meeting_id)
    time.sleep(2)

    joinBTN = pyautogui.locateCenterOnScreen("assets/joinBTN.png")
    pyautogui.moveTo(joinBTN)
    pyautogui.click()
    time.sleep(2)

    passBTN = pyautogui.locateCenterOnScreen("assets/passwordBTN.png") # Metting Password
    pyautogui.moveTo(passBTN)
    pyautogui.write(meeting_pass)
    time.sleep(2)

    finaljoinBTN = pyautogui.locateCenterOnScreen("assets/finalJoin.png") # Enter Meeting
    pyautogui.moveTo(finaljoinBTN)
    pyautogui.click()
    time.sleep(2)


joinMeeting(your_meeting_id, your_meeting_password)
