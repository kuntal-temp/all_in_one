# Learn Linux

### Basic Linux command and description


### General CMD
```
>> sudo apt-get update  [The system executes the command and updates the repositories]
>> sudo apt-get upgrade [to upgrade system]

>> !!  [to repeat the last commad]
>> whoami  [current user]
>> pwd     [present working dir]  
>> htop    [users, cpu uses, ram uses all info] - [need to install]
>> bg  [backgroud]
>> fg  [foreground]
>> exit    [for exit purpose]
>> d11/d111$  [$ means normal user]
>> d11/d111#  [# means sudo user]
```

### cd
```
>> cd dir_name/  [to go into that dir]
>> cd dir_path/  [to go into particular dir]
>> cd ~   [come home from anywhere]
>> cd     [come home from anywhere]
>> cd ..  [going one step back]
>> cd ../../  [going two step back]
```

### ls
```
>> ls  [all file and dir except hidden]
>> ls -l   [file and dir as list]
>> ls -a   [all file and dir include hidden]
>> ls -al  [file and dir as list including Hidden file]
>> ls -li
>> ls -l --block-size=K or M or G or T [all size print as kb]
>> ls -d */  [print only dir]

>> ls *.txt
```

### sudo
```
>> sudo -V  [sudo, policy plugin, file grammar, I/O plugin -> version you can see]
>> sudo -l  [will print out the commands allowed (and forbidden) the user on the current host]
>> sudo su  [for super user login]
>> sudo bash  [username@host will the output] => like: root@trynow:/home/kuntal
```

### group create & delete
```
>> getent group  [list of group]

>> groupadd <groupName>
>> groupdel <group>

>> usermod -a -G <group-name> <user-name>  [add user to a group]

>> usermod -a -G <group-name-1>,<group-name-2> <user-name>  [add user to a group]
```

### create user
```
>> useradd <username> [create user]
>> passwd <username> [ser password for the user]

>> useradd -m <userName> [add username & set password at a time]

>> userdel -r <userName>  [delete user]
```

###
```
>> passwd <username> [ser password for the user]
>> passwd <userName>  [reset password for userName]
```

### su
```
>> su <username>   [The su command allows you to run a shell as another user.]
>> su root
```

### create file or dir
```
>> nano <file-name>  OR nano <file-name> -l

>> cat > <file-nane> 
>> cat <file-1> <file-2> > new.txt  [file1 & file-2 content will be copied to new]
>> cat <file-name>  OR cat -n <file-name>

>> cat >> <file-nane>  [will append the new content] 

>> vi <file-name>

>> touch <file-name>
>> touch <file-name1> <file-name2>

>> mkdir <folder-name>
>> mkdir <folder-name1> <folder-name2> 

>> head <file-name> 
>> head -4 <file-name>
>> head doc1.txt doc2.txt

>> tail <file-name> 
>> tail -2 <file-name>

>> vi <file-name>
>> esc + wq [save new data]
>> q! [exist without saving]
>> q  [exist only]
```

### copy
```
cp Source_file Destination_file
>> cp a.txt b.txt
>> cp a.txt <folder>/b.txt  [will overwrite if exist]

>> cp -i a.txt b.txt  [will ask before overwrite]

>> cp a.txt b.txt c.txt ../<folder-name>   [will create a backup file those already exist]

>> cp *.txt <folder-name>   [copy all .txt file into folder]

cp Src_file1 Src_file2 Src_file3 Dest_directory
>> cp a.txt b.txt c.txt ../<folder-name>  [will overwrite if exist]
```

### move or rename
```
mv Old_folder New_folder  [move and delete old folder]

>> mv c.txt c1.txt
>> mv <folder-1> <folder-2>
```

### delete file or dir
```
>> rm -rf <file-name>
>> rmdir <folder-name>
```

### alias
```
>> alias nn='ls -l'  ---->  >>nn
>> alias fav_path='cd /home/sssit/Downloads/sample'  ---->  >>fav_path

>> unalias nn
```

### export
```
    > export new_variable=10
    > echo $new_variable

    > unset new_variable 

    > env  [The env command is used to display all the available variables in the system]
    > export  [will print all export variable]
```

```
    > function hello  
    > {  
    > echo hello, welcome to javatpoint  
    > }
    
    > export -f function_name
    > function_name
```

### type
```
>> type pwd     ----> pwd is a shell builtin
>> type cat     ----> cat is /usr/bin/cat
```

### change permission
```
-rwxrwxrwx -> 777 for a file
drwxrwxrwx -> 777 for a dir

>> chmod 777 <file-name>
>> chmod 777 <folder>

>> chmod -R 777 <folder-name>  [permission will go for all files]   

>> chmod +x <file-name>  [execute permission]

>> chmod u=rwx,g=rw,o=r <file-name>

777 = rwxrwxrwx  
765 = rwxrw-r-x  
654 = rw-r-xr--  

7 = 4+2+1 (read/write/execute)
6 = 4+2 (read/write)
5 = 4+1 (read/execute)
4 = 4 (read)
3 = 2+1 (write/execute)
2 = 2 (write)
1 = 1 (execute)
```

### change group & owner
```
>> sudo chgrp <group-name> <file-name>

>> chown <newOwner> <fileName>
```

### Display the Disk Space Usage
```
>> df
>> df -h
```

### echo & read
```
>> echo "Enter the user name: "  
>> read first_name  
>> echo "The Current User Name is $first_name"  
```

### exit
```
>> exit
>> exit 10  [close the current terminal]
>> exit $?  [status of last cmd executed] 0 = all good
```

### Find any files
```
>> find . -name "*.txt"
>> find . -name "*.pdf"
>> find . -name "*.md"

```

### grep = global regular expression print
```
>> cat a.txt | grep pg  [file name contains with `pg`]
>> cat a.txt | grep oo
>> cat a.txt | grep 'oo\|pg'  [file name contains with `oo` & `pg`]
>> cat a.txt | grep 'oo\|pg\|url'
>> cat a.txt | grep -i oo

OR [we can write like below without | operator]
>> grep 'extra\|value\|service' sample.txt
>> grep -i 'extra\|value\|service' sample.txt [case ignore]
>> grep -c 'extra\|value\|service' sample.txt [match count]
>> grep -w "unix" geekfile.txt [exact word match]
>> grep -n "unix" geekfile.txt [line number]

>> grep "os$" geekfile.txt

>> ls | grep -in  note
```

### zip & unzip create
```
>> gzip <file1> <file2> <file3>
>> gunzip <file1> <file2> <file3>

>> tar cf - <directory> | gzip > <directoryName>

>> unzip zipped_file.zip 
```

### hard or soft link
```
>> ln <file-name-1> <file-name-2>  [hard link] - if original file will be removed then hard link file will not be affected

>> ln -s <file-name-1> <file-name-2>  [soft link] - if original file will be removed then it will lost
```

### Displaying Shell Expansion
```
>> set +x [disable shell command display]
>> set -x [enable shell command display]
```

### merge two command
```
>> ls && pwd
>> ll;pwd
>> ls;cd ~
>> cd Desktop && file jtp.txt || echo successful.  
```

### comment in linux
```
>> ls -a  # list of all list
```

### All process & To kill a process having PID 2408
```
>> top
>> ps aux
>> ps -A
>> kill -9 2408
```

### networking
```
>> ifconfig
>> ip addr


```

### 
```
>> 
```

### 
```
>> 
```

### 
```
>> 
```

