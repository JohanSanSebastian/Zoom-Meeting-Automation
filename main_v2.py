import pyautogui
import subprocess
import time

check = True


1_id = "" 
1_pass = ""

2_id = ""
2_pass = ""

3_id = ""
3_pass = ""

4_id = ""
4_pass = ""


def joinMeeting(meeting_id, meeting_pass):

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

while check is True:

    subprocess.call("your_zoom_location")
    checkMeeting = input('Which meeting would you like to join? ').lower()

    if checkMeeting == "1":
        print('Joining 1st Meeting.......')
        joinMeeting(1_id, 1_pass)
        check = False

    elif checkMeeting == "2":
        print('Joining 2nd Meeting.......')
        joinMeeting(2_id, 2_pass)
        check = False

    elif checkMeeting == "3":
        print('Joining 3rd Meeting.......')
        joinMeeting(3_id, 3_pass)
        check = False

    elif checkMeeting == "4":
        print('Joining 4th Meeting.......')
        joinMeeting(4_id, 4_pass)
        check = False

    else:
        print('Sorry Meeting not found!')
