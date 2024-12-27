import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHuntingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mXSSCon - Simple XSS Scanner tool")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mXanXSS - A simple XSS finding tool")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mXSStrike - Most advanced XSS scanner")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mExit System - log out AllHuntingTools")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("XSSattACk: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && cd Files && bash XSScon.sh && cd && cd AllHuntingTools && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && cd Files && bash XanXSS.sh && cd && cd AllHuntingTools && python2 MainMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && cd Files && bash XSStrike.sh && cd && cd AllHuntingTools && python2 MainMenu.py")
elif(op==4):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting System...")
 sys.exit()
elif(op==5):
 os.system("cd")
 os.system("cd AllHuntingTool")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHuntingTools")
 os.system("python2 Files/AnalistickMenu.py")
