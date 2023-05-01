# Shell Scripting

1. https://www.javatpoint.com/shell-scripting-tutorial
2. https://www.javatpoint.com/bash-introduction
3. https://www.tutorialspoint.com/unix/index.htm
4. https://devhints.io/bash



The Unix operating system is a set of programs that act as a link between the computer and the user. Users communicate with the kernel through a program known as the shell. The shell is a command line interpreter; it translates commands entered by the user and converts them into a language that is understood by the kernel.

> Hardware <----> Kernel <-----> [we can talk to kernel using shell programming]

> The sign #! is called she-bang and is written at top of the script


- which shell types your operating system supports
```
cat /etc/shells
which bash
```

The ksh and zsh seems about seven times faster than bash
```
>> sudo apt install mksh
```

shell scripting is scripting in any shell, whereas Bash scripting is scripting specifically for Bash


# shebang statement
```
>> #! /bin/bash
```