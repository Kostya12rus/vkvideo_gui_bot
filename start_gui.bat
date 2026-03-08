@echo off
chcp 65001

cd /d "%~dp0"
python -m venv .venv
call ".venv\Scripts\activate.bat"

echo [WIP] Now don`t work GUI using start_gui.bat

pause
