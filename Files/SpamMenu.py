import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHuntingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mSMS-Bomber-300 - bomber for 300 services")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mAnon-SMS - Send Messages Anonymously")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mSpymer - more options sms and cals bomber")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mAres-Bomb - medium Ares-bomber")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mTBomb - Is SMS And Call Bomber")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mEmailPySpam - A python 3+ program to spam emails")
print("  \033[1;34m[ 07 ] >> \033[1;36;40mExit System - log out AllHuntingTools")
print("  \033[1;34m[ 08 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("SpymER: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && cd SMS-Bomber-300-Free && python SMS-Bomber.py && cd && cd AllHuntingTools && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && cd Anon-SMS && bash Run.sh && cd && cd AllHuntingTools && python2 MainMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && cd spymer && python spammer.py && cd && cd AllHuntingTools && python2 MainMenu.py")
elif(op==4):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && cd AresBomb && python boom.py && cd && cd AllHuntingTools && python2 MainMenu.py")
elif(op==5):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && cd TBomb && ./TBomb.sh && cd && cd AllHuntingTools && python2 MainMenu.py")
elif(op==6):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && cd emailpyspam && cd main && python3 emailspam.py && cd && cd AllHuntingTools && python2 MainMenu.py")
elif(op==7):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting System...")
 sys.exit()
elif(op==8):
 os.system("cd")
 os.system("cd AllHuntingTools")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHuntingTools")
 os.system("python2 Files/SpamMenu.py")
 
