#!/bin/bash

read -p " Where do you want to save your work ? Enter the path  " rand4file

read -p " Enter the file name " fl
empty=$fl
#echo " ${empty:6} " 
string_len="${#fl}" #getting the length of a fl input
echo "length of the string $string_len "
for (( i=$string_len-1 ; i>=0 ; i-- )); do   # use logical or operator to allow sh extension like if ( condition or condition)
	var_cap=${empty:$i}
	echo " this is var_cap variable ==> $var_cap "
	if [ "$var_cap" == ".txt" ]
	then
		echo " $var_cap found .txt here it should break "
	        	
		break
	else
		continue
        fi
	#echo " [+]  This is what you are looking for ${empty:4} "
done	


#1 to print unique characters of a line 


function awk_com () {
	awk '{for(i=1;i<=length($0);i++){a[substr($0,i,1)]=1} for(i in a){printf("%s",i)} print "";delete a}' $fl >> $rand4file
	var_c_check=


#under construction 
#working with files.
