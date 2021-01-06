@echo off

set filename=%date:~0,4%%date:~5,2%%date:~8,2%%time:~0,2%%time:~3,2%%time:~6,2%
echo %filename%

copy tmp.csv %filename%.txt

::由于cmd会自动忽略单引号中的^，因此必须用双引号
sed -i "s/^3/qqqqq3/g" %filename%.txt
sed -i ':label;N;s/\n//g;b label' %filename%.txt
sed -i ':label;N;s/\r//g;b label' %filename%.txt
sed -i "s/qqqqq/\r\n/g" %filename%.txt

start %filename%.txt

pause