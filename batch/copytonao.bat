echo purging improvise..

plink -ssh -pw nao nao@%1 -m purgeimprovise.txt

echo improvise purged
echo copying files..

pscp -pw nao c:\users\opalcat\github\improvise\startup.sh nao@%1:/home/nao/improvise
pscp -r -pw nao c:\users\opalcat\github\improvise\pkg nao@%1:/home/nao/improvise
pscp -r -pw nao c:\users\opalcat\github\improvise\html nao@%1:/home/nao/improvise

echo new files copied

plink -ssh -pw nao nao@%1 -m enablestartup.txt

echo startup executable enabled, exiting..
