
#Minecraft bedrock smart AFK fishing autoclicker (mbsafa)

#Readme
#pip3 install numpy pillow pyautogui mss
#Build a afkfish farm / place a block of water / find a sea, lake, any water
#In minecraft > video settings > turn off camera shaking
# ! Minecraft sould be in a windowed mode (not fullscreen) cuz iw be expierenced some troubles with fulscreen mode !
#Stand in a position with a fishing rod
#Alt+tab and launch script
#Get back to minecraft, and slightly move side to side
#When rod is active - script is working =0
#Dont touch mouse or move
#To stop script use ctrl+c hotkey
#Recomendations: Use sea luck III for maximum efficient of farm, make sure that there is no any particles(like torch) or animated block near fishing rod, 
#Script is providing AS IS, and dont guarantee that 100% work in any cases
# ! Script only tested with vanilla and faithful x32 resource packs, any other resource pack may not work properly !

#How it works?
#Script constantly monitor part of the screen where fishing rod is located (region =), and when see some moving (fish is caught) initiate the RMB click.
#After RMB click, script has a timer (2sec) to avoid false trigger
#Dont need any special constructions to use


#todo list
#Add a timer, when(if) something dont work properly (like 15 seconds for sea luck III)
#Add a sound design
#Make a exe file to work on any machine (linux still need another way to do so)
#Make a github page
#Share this script to another folks
#Maybe make code more optimized and efficient
#TEST USAGE OF SYSTEM RESOURCES (MEMORY LEAK AND OTHER CRAP)
#Add a hotkey to start working
 
import time
import numpy as np
from PIL import Image, ImageChops
import pyautogui
import mss

region = {"top": 680, "left": 1340, "width": 160, "height": 400}

def capture_screen(region):
    with mss.mss() as sct:
        return Image.frombytes("RGB", sct.grab(region).size, sct.grab(region).rgb).convert("L")

def detect_motion(prev_img, curr_img, threshold=30):
    return np.sum(np.array(ImageChops.difference(prev_img, curr_img)) > threshold) > 500

def main():
    print("AFK fishing active. Press Ctrl+C, to stop.")
    prev_frame = capture_screen(region)
    time.sleep(0.1)
    while True:
        try:
            curr_frame = capture_screen(region)
            if detect_motion(prev_frame, curr_frame):
                pyautogui.click(button="right")
                time.sleep(2)
                prev_frame = capture_screen(region)
            else:
                prev_frame = curr_frame
            time.sleep(0.1)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
