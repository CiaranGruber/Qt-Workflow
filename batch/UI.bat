@echo off
call ../testenv/Scripts/activate

Call :Convert,".",""
EXIT /B %ERRORLEVEL%
:Convert
for %%f in (%~1/*.ui) do (
    echo %~2Processing %%~nf.ui
    pyside6-uic %~1/%%f > %~1/ui_%%~nf.py
)

for %%f in (%~1/*.qrc) do (
    echo %~2Processing %%~nf.qrc
    pyside6-rcc %~1/%%f -o %~1/rc_%%~nf.py
)

for /D %%i in (%~1/*) do (
    echo %~2Accessing %%i
    Call :Convert,%~1/%%i,"    %~2"
)
EXIT /B 0