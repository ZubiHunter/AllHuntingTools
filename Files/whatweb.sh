g="\033[1;32m"
r="\033[1;31m"
b="\033[1;34m"
w="\033[0m"

clear
cd
cd AllHuntingTools
cd WhatWeb
clear
./whatweb
echo "Please enter all your required settings to run the program, for example: reddit.com"
echo -e $b">>>"$w" Consoler "$g"WhatWeb"$w
read opt
sleep 0.1
./whatweb $opt
cd
cd
cd AllHuntingTools
