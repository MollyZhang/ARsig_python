# CPRC_signatures
Explore Various biological signature in Castration-Resistant Prostate Cancer.
### 1. AR signature


### 2. NEPC signature


## data
### cell line data
### WCDT samples (patient)
### OHSU data (?)


# Run juypter notebook in your laptop browser from a ssh server
on server:
`jupyter notebook --no-browser`

on laptop:
`ssh -NL 8888:localhost:8888 username@remote-server-public-dns`

A prompt will ask for ssh password, and after typing in password, go to browser and go to `localhost:8888`, the browser would ask for a "token", which can be found in the remote server, after entering the token, the jupyter notebook can be used in your laptops browser which is connected to the remote server
