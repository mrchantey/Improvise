echo purging improvise..

plink -ssh -pw nao nao@%1 -m purgeimprovise.txt

echo improvise purged
echo copying files..

pscp -r -pw nao c:\users\jaspercat\github\improvise\data nao@%1:/home/nao/improvise
echo data copied
pscp -r -pw nao c:\users\jaspercat\github\improvise\pkg nao@%1:/home/nao/improvise
echo python copied
pscp -r -pw nao c:\users\jaspercat\github\improvise\html nao@%1:/home/nao/improvise
echo html copied
pscp -pw nao c:\users\jaspercat\github\improvise\startup.sh nao@%1:/home/nao/improvise
echo startup.sh copied
pscp -pw nao c:\users\jaspercat\github\improvise\batch\autoload.ini nao@%1:/home/nao/naoqi/preferences
echo autoload.ini copied

plink -ssh -pw nao nao@%1 -m enablestartup.txt
echo startup executable enabled
