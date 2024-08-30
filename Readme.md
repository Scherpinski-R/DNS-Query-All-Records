# DNS - Query All Records

## Motivation

When I was doing dnslookup/host/dig an server to gather more info, I did't found a way to get all records,
since the option -type any isn't answered by all dns servers. 

So I created this script to get all records for me.

## Usage 

```
python dns-qar.py "server" "dns-server"

python dns-qar.py www.github.com 8.8.8.8

```

## TODO

- [ ] Create Config File to User add what DNS Records makes sense to User
- [ ] Implement Validations in Server input
- [ ] Implement Validations in Dns-Server input

if you have any suggestions, please send an Issue.
