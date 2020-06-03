@echo off

:: get date
set d=%date:~0,10%
echo %d%
set d1=%date:~0,4%
set d2=%date:~5,2%
set d3=%date:~8,2%
echo d1=%d1%
echo d2=%d2%
echo d3=%d3%

:: get time
set t=%time%
echo %t%
set t1=%time:~0,2%
set t2=%time:~3,2%
set t3=%time:~6,2%
echo t1=%t1%
echo t2=%t2%
echo t3=%t3%

sed -i "s/date = .*/date = \"%d1%-%d2%-%d3% %t1%:%t2%:%t3%\"/g" D:\QIN\exercise\tmp.txt
sed -i "s/<action android:name=\"android.intent.action.MAIN\" \/>/<action android:name=\"aaabbb\" \/>/g" D:\QIN\exercise\tmp.txt
sed -i "/date =/a\<action android:name=\"android.intent.action.MAIN\" \/>" D:\QIN\exercise\tmp.txt
sed -i "/123/r D:\QIN\exercise\666.txt" D:\QIN\exercise\tmp.txt

pause