# !/bin/bash


<<com
if...then...fi statements
if...then...else...fi statements
if..elif..else..fi
if..then..else..if..then..fi..fi.. (Nested Conditionals)
com


# If else example
MY_Shell="csh"

if [ ${MY_Shell} = "xxx" ]
then
    echo "cond1 match"
elif [ ${MY_Shell} = "csh" ]
then
    echo "cond2 match"
else
    echo "no match"
fi


# Example 2
if [ $# == 0 ]
then
    echo "No args params"
else
    echo "with args params"
fi


if [ $a != $b ]
then
    echo "a is not equal to b"
fi


a=5
b=6

if (( $a==$b ))
then
    echo a is equal to b.
else
    echo a is not equal to b.
fi
if (( $a!=$b ))
then
    echo a is not equal to b.
else
    echo a is equal to b.
fi
   
if (( $a<$b ))
then
    echo a is less than b.
else
    echo a is not less than b.
fi
   
if (( $a<=$b ))
then
    echo a is less than or equal to b.
else
    echo a is not less than or equal to b.
fi
   
if (( $a>$b ))
then
    echo a is greater than b.
else
    echo a is not greater than b.
fi
   
if (( $a>=$b ))
then
    echo a is greater than or equal to b.
else
    echo a is not greater than or equal to b.
fi




if (($a == "true" & $b == "true" ))
then
    echo Both are true.
else
    echo Both are not true.
fi
  
if (($a == "true" || $b == "true" ))
then
    echo Atleast one of them is true.
else
    echo None of them is true.
fi
  
if (( ! $a == "true"  ))
then
    echo "a" was initially false.
else
     echo "a" was initially true.
fi





##########################################3

read -p 'Enter file name : ' FileName
  
if [ -e $FileName ]
then
    echo File Exist
else
    echo File doesnot exist
fi
  
if [ -s $FileName ]
then
    echo The given file is not empty.
else
    echo The given file is empty.
fi
  
if [ -r $FileName ]
then
    echo The given file has read access.
else
    echo The given file does not has read access.
fi
  
if [ -w $FileName ]
then
    echo The given file has write access.
else
    echo The given file does not has write access.
fi
  
if [ -x $FileName ]
then
    echo The given file has execute access.
else
    echo The given file does not has execute access.
fi

if [ -f notes.md ]
then 
    echo "111111" 
else 
    echo "22222" 
fi


if [ $x -gt $y ]
then
echo X is greater than Y
elif [ $x -lt $y ]
then
echo X is less than Y
elif [ $x -eq $y ]
then
echo X is equal to Y
fi


<< com
-a = and
-o = or
com


read a
read b
read c

if [ $a == $b -a $b == $c -a $a == $c ]
then
echo EQUILATERAL

elif [ $a == $b -o $b == $c -o $a == $c ]
then 
echo ISOSCELES
else
echo SCALENE

fi