@echo off
chcp 65001

echo Go to script directory
cd /d "%~dp0"

echo [1/4] Creating virtual environment...
if not exist ".venv" (
    python -m venv .venv
) else (
    echo .venv already exists, skipping creation.
)

echo [2/4] Activating environment...
call ".venv\Scripts\activate.bat"

echo [3/4] Upgrading pip tools...
python -m pip install --upgrade pip setuptools wheel

echo [4/4] Installing project from GitHub...
python -m pip install --force-reinstall "git+https://github.com/Kostya12rus/vkvideo_gui_bot.git"

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Installation failed.
    pause
    exit /b 1
)

echo.
echo [SUCCESS] All packages installed!
pause