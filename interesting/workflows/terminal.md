# Useful terminal commands

Run multiple commands

```
# No matter the first command cmd1 run successfully or not, always run the second command cmd2
# cmd1; cmd2

# Only when the first command cmd1 run successfully, run the second command cmd2
# cmd1 && cmd2

# Only when the first command cmd1 failed to run, run the second command cmd2
cmd1 || cmd2
```

Get my ip address
```
ifconfig
```

Scan used ip addresses
```
nmap 192.168.0.0/24
```

SSH
```
ssh username@hostname
```

Stop SSH command and run it in the background
```
Ctrl + Z
disown -h %x # where x is the job number
bg

ps -ef # to see the running job
```

Linux screen commands
```
# Starting Named Session
$ screen -S session_name
# Close screen (with id)
$ screen -X -S 12345 quit
#All screen list
$ screen -ls
#Reattach to a Linux Screen
$ screen -r 12345 (screen id)
#Detach from Linux Screen Session
$ Ctrl+a d
```

Secure copy
```
scp source_file_path destination_username@destination_hostname:destination_path
```

SFTP
```
sftp username@hostname
```

Rename all files with a for loop
```
for x in *; do mv $x S000001_$(printf "%06d" ${x%_img.png}+1).jpg; done
```

Extracting large zip files on Ubuntu
```
dtrx <name-of-zip-file>
```

Unlinking files
```
mkdir tmp && for x in *; do cp -L $x tmp/ && rm $x && mv tmp/$x .;done; rmdir tmp
```
