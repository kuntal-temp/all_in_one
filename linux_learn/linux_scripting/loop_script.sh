# !/bin/bash

# For Loop
for i in x y z
do
    echo "ITEM is = ${i}"
done

ITEMS="x y z"
for i in ${ITEMS}
do
    echo "ITEM is = ${i}"
done

for i in {2..20..2}
do
    echo "${i}"
done


for i in {1..10}  
do  
    touch $i.txt;  
done 


for i in *.txt
do  
    echo $i;  
done;  


V=$( find . -name "*.md" )
for i in ${V} 
{ 
    echo "${i}";
}


# While Loop
i=10
while [ ${i} -gt 1 ]
do
    echo "${i}"
    let i--;
done

while [ $a -lt 10 ]
do
    # Print the values
    echo $a
     
    # increment the value
    a=`expr $a + 1`
done


i=1
while [[ $i -le 10 ]]
do
   echo "$i"
  (( i += 1 ))
done

####################################################

for (( i=1; i<10; i++ ))
do
    echo "${i}"
done


for a in 1 2 3 4 5 6 7 8 9 10
do
    # if a is equal to 5 break the loop
    if [ $a == 5 ]
    then
        break
    fi
    # Print the value
    echo "Iteration no $a"
done

for a in 1 2 3 4 5 6 7 8 9 10
do
    # if a = 5 then continue the loop and
    # don't move to line 8
    if [ $a == 5 ]
    then
        continue
    fi
    echo "Iteration no $a"
done




