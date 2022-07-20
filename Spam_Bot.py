# Automated text messaging

# Import relevant modules
import time
import pyautogui


# code
def sendmessage():
    time.sleep(10)
    text = open('testdoc.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press('enter')


sendmessage()

# (mac)To use it, go to System Preferences
# Then goto Security & Privacy - Privacy tab
# open Accessibility, Click unlock to make changes - Then add PyCharm CE and click the box
# Then run, And you have ten seconds(or you can change the timer) to place
