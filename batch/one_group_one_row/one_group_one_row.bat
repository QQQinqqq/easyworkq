@echo off & setlocal enabledelayedexpansion

for /f "tokens=*" %%i in ('dir /a-d /b D:\Book1.csv') do call :out "%%i"
gawk "{printf $0}"  new_files.txt > new_files2.txt
sed -i "s/\r//g" new_files2.txt
sed -i "s/aaa/,/g" new_files2.txt
sed -i "s/bbb/\r\n/g" new_files2.txt
ren new_files2.txt new_files2.csv
start "" "new_files2.csv"
pause

:out
set "n=0"
set "m=0"
echo 123
for /f "usebackq tokens=*" %%j in ("%~1") do (
    set /a n+=1
	set /a m=n%%4
    if !m! equ 1 echo %%jaaa
	if !m! equ 2 echo %%jaaa
	if !m! equ 3 echo %%jaaa
	if !m! equ 0 echo %%jbbb
)>>new_files.txt
goto :eof