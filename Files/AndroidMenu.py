import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHuntingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mPyshell - Remote Access Trojan - RAT")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mWishfish - Powerful Tool For Grab Front Camera Snap Using A Link")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mLockPhish - Tool for phishing attacks on the lock screen")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mHatCloud - Tool for find website real IP behind cloudflare")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mExit System - Log out AllHuntingTools")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("R6moteTRo1anR8t: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && cd pyshell && ./Pyshell && cd && cd AllHuntingTools && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && cd WishFish && ./wishfish.sh && cd && cd AllHuntingTools && python2 MainMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && cd lockphish && bash lockphish.sh && cd && cd AllHuntingTools && python2 MainMenu.py")
elif(op==4):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && cd Files && bash HatCloud.sh && cd && cd AllHuntingTools && python3 src/Timer2.py && python2 MainMenu.py")
elif(op==5):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting System...")
 sys.exit()
elif(op==6):
 os.system("cd")
 os.system("cd AllHuntingTools")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHuntingTools")
 os.system("python2 Files/AndroidMenu.py")
