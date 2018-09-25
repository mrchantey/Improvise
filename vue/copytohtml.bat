rmdir ..\html\js /s /q
rmdir ..\html\css /s /q
mkdir ..\html\js
mkdir ..\html\css
xcopy dist\css ..\html\css
xcopy dist\js ..\html\js

echo static files copied
del ..\html\index.html
copy dist\index.html ..\html
echo index file copied