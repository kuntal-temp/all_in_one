# !/bin/bash

#Note: The ksh and zsh seems about seven times faster than bash

echo "Learn Linux Scripting"

# single line comment
<<com 
 Multiline comment
com


MY_VAR="I am from base file"

# basic
echo "${HOME} - > It home dir"
echo "${PWD} - > It PWD"
echo "${OSTYPE} - > It OS Type"
echo "${BASH_VERSION} - > It Bash Version"


# Args Pass [$1 to $9]
echo "printing from params ${0} ${1} ${2}" 5 7 9
echo "Represent all the arguments as a single string : $*" 25 "fd"
echo "total number of params : $#"
echo "PID of this script = $$"

# promt user input
read -p "Enter a user name : " USER1
echo "user is = ${USER1}"


# Ouput of cmd store in variable
VAR1=$( ls )
VAR1=$( mkdir <folder-name> )
echo "output of ls = ${VAR1}"


var=$((3+9))
echo $var


# differnet SheBang
#!/bin/bash  
echo "Hello World"
#!/bin/ksh  
echo "Hello World"


# Let is an arithmetic operator
let x="100+5"
let x=${x}+5
let x+=5 
echo "${x}"
