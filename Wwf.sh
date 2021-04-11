#!/bin/bash
#This script will cut off long awk command and you can get your work done with script name and few arguments. will be updating......
#This script will check .txt extension of a first filename. will implement few more security patches in coming days
# wwf ==> working with files 
#More ideas are aprreciated as this project will benefit for the new comers who work with long awk commands. 



#function 2
function unique_words_in_a_file() {
	cat $fl | grep -o -e '\w+' | tr '[a-z]' '[a-z]' | sort | uniq -c | sort -nr >> $rand4file
}


#function 1
function unique_words_in_line () {
        echo " [+] Printing Unique words in a line. " 	
	awk '{for(i=1;i<=length($0);i++){a[substr($0,i,1)]=1} for(i in a){printf("%s",i)} print "";delete a}' $fn_txt >> $savefilework 
	var_c_check=$(echo $?)
	echo " $var_c_check "
	variable=0
	if [ $var_c_check == $variable ]
	then
		echo " [+] Output has successfully printed to $savefilework  " #keep track of this line
	else
		error
	fi
}

#case 
function entry () {
	echo " [+] choosed $argument_case_num " 
	case $argument_case_num in
		1) unique_words_in_line ;;
		2) unique_words_in_a_file ;;
		*) echo " Nothing to do "
		   exit ;;
        esac

}


function help_function () {
	echo " [1] Prints unique words of a LINE " 
        echo " [2] Prints unique words in a FILE "
} 

argument_case_num=$1
fn_txt=$2
savefilework=$3   # This is where you save your work.

if [ "$argument_case_num" == "--help" -o "$argument_case_num" == "-h" ]
then
	help_function
	echo " ./scriptname.sh 1 workingfilename savingfilename "
        exit	
else
	continue
fi

#echo " $fn_txt " working file 
 
string_len="${#fn_txt}" #getting the length of a argument_2 which is txt file

echo " [+] length of the string $string_len "

for (( i=$string_len-1 ; i>=0 ; i-- )); do   # use logical or operator to allow sh extension like if ( condition or condition)
	var_ext_chk=${fn_txt:$i} 
	#echo " [+] This is var_ext_chk variable ==> $var_ext_chk "
	if [ "$var_ext_chk" == ".txt" ]
	then
		echo " [+] File name Verified "
		#echo " [+] First Function should run here "
	        entry	
		break
	else
		continue
        fi
done	



#contact huddar26@gmail.com for more info
