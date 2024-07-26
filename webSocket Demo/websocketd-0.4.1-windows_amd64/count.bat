@echo off
setlocal enabledelayedexpansion

:loop
set /p line=
if not defined line goto :eof
echo You said: !line!
goto loop
