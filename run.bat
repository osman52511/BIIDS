@echo off
chcp 65001 > nul
title BIIDS - Bomb & IED Identification System

echo ============================================================
echo   বোম্ব ও আইইডি সনাক্তকরণ সিস্টেম (BIIDS)
echo   Bomb & IED Identification System
echo   Bangladesh Armed Forces
echo ============================================================
echo.

REM Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found. Please install Python 3.9+
    pause
    exit /b 1
)

REM Install requirements
echo Installing/checking requirements...
pip install -r requirements.txt -q

echo.
echo [INFO] Starting server...
echo [INFO] URL: http://localhost:5000
echo [INFO] Demo Login: DEMO001 / demo123
echo.
echo [TIP] Set ANTHROPIC_API_KEY for full AI scanning functionality
echo.

REM Set API key if available (edit this line)
REM set ANTHROPIC_API_KEY=your_api_key_here

python app.py

pause
