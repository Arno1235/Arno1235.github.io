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
ssh TODO
```

Secure copy
```
scp TODO
```

SFTP
```
sftp TODO
```

Rename all files with a for loop
```
for x in *; do mv $x S000001_$(printf "%06d" ${x%_img.png}+1).jpg; done
```

Extracting large zip files on Ubuntu
```
dtrx <name-of-zip-file>
```
