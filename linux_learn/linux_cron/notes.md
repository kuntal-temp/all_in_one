# cron in linux

```
>> crontab -e
```

# Cron Syntax
```
A B C D E USERNAME /path/to/command arg1 arg2
OR
A B C D E USERNAME /root/backup.sh
```

@hourly: Run once every hour i.e. “0 * * * *“
@midnight: Run once every day i.e. “0 0 * * *“
@daily: same as midnight
@weekly: Run once every week, i.e. “0 0 * * 0“
@monthly: Run once every month i.e. “0 0 1 * *“
@annually: Run once every year i.e. “0 0 1 1 *“
@yearly: same as @annually
@reboot: Run once at every startup

```
>> @daily /path/to/backup/script.sh
```


# Example
```
>> 0 3 * * * /root/backup.sh        [3 am every day]
>> 30 16 2 * * /path/to/script.sh   [4:30 pm on the second of every month]
>> 5 4 * * sun /path/to/test.sh     [04:05 every Sunday]
```

# List of Cron
```
>> crontab -l
```

# Delete all crontab jobs
```
>> crontab -r
```

# My Example
```
>> * * * * * /home/kuntal/Desktop/GitFolder/linux_learn/linux_cron/test.sh
```
