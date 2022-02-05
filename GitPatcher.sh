#!/bin/sh
clear
echo Would you like to continue installing/updating PyDOS?
read continue
if [ $continue == 'y' ]
then
	cd ~
	rm -r PyDOS
	git clone https://github.com/BabRoosss/PyDOS
	echo Done!
	read -sp 'Press enter to exit!'
	echo
	clear
	echo ===============================================
	echo                    PyDOS
	echo               Made by Bab Rooss
	echo ===============================================
else
	echo Ok. Goodbye!
	sleep 5
	echo
fi
