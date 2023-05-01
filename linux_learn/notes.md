# Linux Notes

Unix: Unix is a copyrighted name and IBM AIX, HP-UX and Sun Solaris are only Unix operating system remained till date. It is an operating system which can be only used by its copyrighters.

Linux: It is the clone of Unix. It is an open-source operating system which is freely available to everyone.

we have SUSE Linux Enterprise Server (SLES) and RedHat Enterprise Linux for the commercial distribution of Linux.

In Linux, everything (Directories, devices, and files) is considered a file.
There are three types of files available in a Linux system.
* General files
* Directory files
* Device files

Linux supports three types of users:
* Regular
* Administrative(root)
* Service


root -> etc, bin, sbin, usr, tmp, dev, home .....

/
bin   cdrom  etc   lib    lib64   lost+found  mnt  proc  run   snap  swapfile  tmp  var
boot  dev    home  lib32  libx32  media       opt  root  sbin  srv   sys       usr

dev = device [It appears to be an ordinary file but doesn't take up disk space. Files which are used to represent and access devices are stored here including terminal devices like usb. All the files stored in '/dev' are not related to real devices, some are related to virtual devices also]

proc = process [Same as '/dev', '/proc' also doesn't take up disk space. It contains process information. It is a pseudo filesystem that contains information about running processes. It also works as virtual filesystem containing text information about system resources.]

sys = system [Basically it contains kernel information about hardware.]

srv = service  [The '/srv' directory contains server specific data for services provided by the system like www, cvs, rysync, ftp, etc]

media = The '/media' directory acts as a mount point for removable media devices such as CD-Rom, floppy, USB devices, etc

mnt = mount [The '/mnt' directory should be empty and sysadmins can only mount temporary filesystems]

tmp = temporary [When system is rebooted, files under this directory is automatically deleted]

usr = user or Unix System Resources [bin, games, include, lib, lib32, lib64, libexec, libx32  local, pgadmin4, sbin, share, src]

var = varible [backups, cache, crash, lib, local, lock, log, mail, metrics, opt, run, snap  spool, tmp, www] Files that have an unexpected size and whose content is expected to change continuously (that's why it is named as variable) during normal operation of the system are stored here. For example, log files, spool files and cache files.

run = The '/run' directory stores run-time variable data. Run-time vriable data means, data about the running system since last boot

lost + found = During system crash or in any other situation when Linux file system checker (fsck) recovers lost data, that data is stored in this directory. Data may or may not be in a good condition.

cdrom = Ideally according to standard FHS cdrom should be mounted under '/media'

Data directory contains following directories:
    /home
    /root
    /srv
    /media
    /mnt
    /tmp

Memory directory contains the following directories:
    /dev
    /proc
    /sys

Non-standard directories are as follows:
    /cdrom
    /run
    /lost + found


An operating system is a software that enables the communication between computer hardware and software. It conveys input to get processed by the processor and brings output to the hardware to display it.

The biggest success of Linux is Android(operating system) it is based on the Linux kernel that is running on smartphones and tablets


# Linux Distribution?
Linux distribution is an operating system that is made up of a collection of software based on Linux kernel or you can say distribution contains the Linux kernel and supporting libraries and software.
Example: Ubuntu, Debian, Fedora, Linux Mint, Solus


# Architecture of Linux
Hardware <-> kernel <-> shell <-> application, utilities,compiler...etc


# What is Shell?
The terminal contains the shell; it allows us to execute the commands to interact with the system.


# What is Scripting?
Suppose we are required to execute some basic commands every day then we use scripting.

# Users & Group & Other
/etc/psswd -> all users
/etc/group -> all group


# Linux File Ownership
User: A user is the one who created the file. By default, whosoever, creates the file becomes the owner of the file. A user can create, delete, or modify the file.
Group: A group can contain multiple users. All the users belonging to a group have same access permission for a file.
Other: Any one who has access to the file other than user and group comes in the category of other. Other has neither created the file nor is a group member.


# Linux File Links
* Soft [if original file will be removed then it will lost]
* Hard [if original file will be removed then hard link file will not be affected]



# The bash shell has three standard streams in I/O redirection:

* standard input (stdin) : The stdin stream is numbered as stdin (0). The bash shell takes input from stdin. By default, keyboard is used as input.
* standard output (stdout) : The stdout stream is numbered as stdout (1). The bash shell sends output to stdout. Output goes to display.
* standard error (stderr) : The stderr stream is numbered as stderr (2). The bash shell sends error message to stderr. Error message goes to display.



# TELNET - PORT 23
This protocol has some security defects, but it is one of the most used networking protocols due to its simplicity. It is not a secure protocol because it transfers data in unencrypted form. Often Linux user prefers ssh over telnet because ssh transfers data in encrypted form.
```
>> telnet <hostname>/<IP address>
```


# SSH - PORT 22
The ssh command uses a ssh protocol, which is a secure protocol, as the data transfer between the client and the host takes place in encrypted form.

- Way-1: [OpenSSH client/server]
    SSH client and server, we can establish a secure connection with other machines. For a secure connection between two machines, they both have ssh client and server installed.

- Way-2: [ssh-keygen]
    To create a connection with the host client, we need a specific key for an encrypted connection. Logging in to remote host computer by ssh key is more secure than using a password


# Linux netstat
Linux netstat command stands for Network statistics. It displays information about different interface statistics, including open sockets, routing tables, and connection information. Further, it can be used to displays all the socket connections (including TCP, UDP). Apart from connected sockets, it also displays the sockets that are pending for connections. It is a handy tool for network and system administrators.

```
netstat- a
netstat -at
netstat -au
netstat -tnl
```

ss do the more than netstat
```
ss -ta  
ss -ua  
ss -xa 
```

# dig/nslookup - This command is also used to find DNS related query
```
>> dig javatpoint.com 
OR
>> nslookup javatpoint.com
```


# Custom CMD
So, better if we create our own cmd in bash_aliases
``` 
    >> nano ~/.bashrc
    >> nano ~/.bash_aliases
```



















https://javatpoint.com/linux-tutorial
https://www.javatpoint.com/windows
