import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHuntingTools && clear && bash Logo.sh")

print("  \033[1;34m[ 01 ] >> \033[1;36;40mMailHack - Email hacker")
print("  \033[1;34m[ 02 ] >> \033[1;36;40mPwnedOrnot - Tool for find passworld email")
print("  \033[1;34m[ 03 ] >> \033[1;36;40mEmailPySpam - A python 3+ program to spam emails and more options!")
print("  \033[1;34m[ 04 ] >> \033[1;36;40mGmailHack - A python Easy email hacker")
print("  \033[1;34m[ 05 ] >> \033[1;36;40mEmailSpammer - The Ultimate script for spamming emails!")
print("  \033[1;34m[ 06 ] >> \033[1;36;40mExit System - log out AllHuntingTools")
print("  \033[1;34m[ 07 ] >> \033[1;36;40mBack To MainMenu")

op=int(raw_input("Ma1lHacK: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && cd hack-gmail && python3 hack-gmail.py && sleep 7 && cd && cd AllHuntingTools && python2 MainMenu.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && cd pwnedOrNot && python3 pwnedornot.py && sleep 7 && cd && cd AllHuntingTools && python2 MainMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && cd emailpyspam && cd main && python3 emailspam.py && cd && cd AllHuntingTools && python2 MainMenu.py")
elif(op==4):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && cd Gmail-Hack && python3 Mail-Hack.py && sleep 7 && cd && cd AllHuntingTools && python2 MainMenu.py")
elif(op==5):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && cd Email-Spammer && python3 main.py && cd && cd AllHuntingTools && python2 MainMenu.py")
elif(op==6):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting System...")
elif(op==7):
 os.system("cd")
 os.system("cd AllHuntingTools")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHuntingTools")
 os.system("python2 Files/MailMenu.py")
