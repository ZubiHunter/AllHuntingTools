import requests
import os
import time
import random
import sys

os.system("clear")
os.system("cd && cd AllHuntingTools && clear && bash Logo.sh")
os.system("cd && bash AllHuntingTools/.desing/SettingMenu3.sh")

op=int(raw_input("Sett1Ngs: "))

if(op==1):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && cd .settings && python2 DesingLogo.py")
elif(op==2):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && cd .settings && python2 DesingMenu.py")
elif(op==3):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && cd src && mv AnimationLoad1.sh /data/data/com.termux/files/home/AllHuntingTools/.temp/ && cd && cd AllHuntingTools && cd .settings && mv AnimationLoad1.sh /data/data/com.termux/files/home/AllHuntingTools/src/ && cd && cd AllHuntingTools && cd .temp && mv AnimationLoad1.sh /data/data/com.termux/files/home/AllHuntingTools/.settings/ && cd && cd AllHuntingTools && bash .settings/Applined.sh")
elif(op==4):
 os.system("cd && cd AllHuntingTools && cd src && mv AnimationLoad1.sh /data/data/com.termux/files/home/AllHuntingTools/.temp/DesingTemp4/ && mv AnimationLoad2.sh AnimationLoad1.sh && cd && cd AllHuntingTools && cd .temp && cd DesingTemp4 && mv AnimationLoad1.sh AnimationLoad2.sh && mv AnimationLoad2.sh /data/data/com.termux/files/home/AllHuntingTools/src/")
elif(op==5):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && cd .settings && python2 SpecialOpportunities.py")
elif(op==6):
 os.system("clear")
 os.system("cd && nano .zsh_history")
elif(op==7):
 os.system("clear")
 os.system("cd && rm -rf AllHuntingTools/.settings/deletedfiles/.zsh_history && cd && mv .zsh_history AllHuntingTools/.settings/deletedfiles/ && cd && cd AllHuntingTools && python2 MainMenu.py")
elif(op==8):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && bash Logo.sh")
 time.sleep(0.2)
 print("\033[1;31;40mRestoring AllHuntingTools backup...")
 os.system("cd /sdcard/ && cp -r AllHuntingTools /data/data/com.termux/files/home/")
 os.system("cd && bash AllHuntingTools/.settings/RestoreAllHuntingToolsBackup.sh")
 print("successfully restored backup in: sdcard...")
elif(op==9):
 os.system("clear")
 os.system("cd && cd AllHuntingTools && bash Logo.sh")
 time.sleep(0.2)
 print("\033[1;31;40mWait A Bit For The Backup To Be Created...")
 os.system("cd && cd && cp -r AllHuntingTools /sdcard/")
 print("successfully created a backup in: sdcard...")
elif(op==10):
 time.sleep(0.2)
 print("\033[1;31;40mQuiting System...")
 sys.exit()
elif(op==11):
 os.system("cd")
 os.system("cd AllHuntingTools")
 os.system("python2 MainMenu.py")
else:
 print("\033[1;31;40mInvalid input. Reloading Tools") 
 time.sleep(1.6)
 os.system("cd")
 os.system("cd AllHuntingTools")
 os.system("python2 MainMenu.py")
