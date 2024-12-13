# mbsafa
Minecraft bedrock smart afk fish autoclicker (mbsafa)

1. pip3 install numpy pillow pyautogui mss
2. Build a afkfish farm / place a block of water / find a sea, lake, any water
3. In minecraft > video settings > turn off camera shaking
> ! Minecraft sould be in a windowed mode (not fullscreen) cuz iw be expierenced some troubles with fulscreen mode !
4. Stand in a position with a fishing rod
5. Alt+tab and launch script
6. Get back to minecraft, and slightly move side to side
7. When rod is active - script is working =0
8. Dont touch mouse or move
9. To stop script use ctrl+c hotkey

+ Recomendations: Use sea luck III for maximum efficient of farm, make sure that there is no any particles(like torch) or animated block near fishing rod, 
Script is providing AS IS, and dont guarantee that 100% work in any cases
> ! Script only tested with vanilla and faithful x32 resource packs, any other resource pack may not work properly !

How it works?
Script constantly monitor part of the screen where fishing rod is located (region =), and when see some moving (fish is caught) initiate the RMB click. After RMB click, script has a timer (2sec) to avoid false trigger.

todo list
+ Add a timer, when(if) something dont work properly (like 15 seconds for sea luck III)
+ Add a sound design
+ Make a exe file to work on any machine (linux still need another way to do so)
+ Share this script to another folks
+ Maybe make code more optimized and efficient
+ TEST USAGE OF SYSTEM RESOURCES (MEMORY LEAK AND OTHER CRAP)
+ Add a hotkey to start working
