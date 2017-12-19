# CPRC_signatures
Explore Various biological signature in Castration-Resistant Prostate Cancer.

## Jupyter Notebook:
### 1. AR signature
see ARsig.ipynb

### 2. NEPC signature
see NEPCsig.ipynb

## Data (on server bop.soe.ucsc.edu)
RNA-seq: `/projects/sysbio/users/WCDT/Data/mRNA_Seq/CombatCorrection/out.tsv`  
Pathology calls: `/projects/sysbio/users/WCDT/Data/SampleInfo/Clinical/Wcdt/cleaned_up_pathology_calls.tsv`

## How to run juypter notebook in your laptop browser from a ssh server
1. on server:
`jupyter notebook --no-browser`

2. on laptop:
`ssh -NL 8888:localhost:8888 username@remote-server-public-dns`

> A prompt will ask for ssh password, and after typing in password, go to browser and go to `localhost:8888`, the browser would ask for a "token", which can be found in the remote server, after entering the token, the jupyter notebook can be used in your laptops browser which is connected to the remote server
