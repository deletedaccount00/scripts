#!/bin/bash


echo " ######################################"
echo " # [caution] Run this script in root ##"
echo " ######################################"


function check_user() {
	check1=$(whoami)
	expec="root"
	if [ $check1 == $expec ]
	then
		echo "[+] Detected root "
		creator
	else
		echo "[-] FAILED ! hello $check1"
	fi

}


function creator() {
	echo " [ + ] This script will create a user with strong password "	
	read -p " Enter a path to save username associated to passwords " path 
	read -p" Enter the number of users you want to create " user_num
	user_num2=$user_num
	index=0
	read -p " Enter the length of the password " pass_len
	while [ $index -lt $user_num2 ] 
	do
		read -p " Enter a user name here ==> " user_name
		password=$(openssl rand -base64 $pass_len)
		sudo useradd -p $password $user_name
		echo " $user_name ===> $password " >> $path 
		index=$((index + 1))
	done
}

check_user
