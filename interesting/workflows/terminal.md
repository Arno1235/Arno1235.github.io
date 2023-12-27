# Useful terminal commands

Get my ip address
```
ifconfig
```

Scan used ip addresses
```
nmap 192.168.0.0/24
```

Rename all files with a for loop
```
for x in *; do mv $x S000001_$(printf "%06d" ${x%_img.png}+1).jpg; done
```

