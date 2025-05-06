@echo off
echo Setting up GlamMate development environment...

REM Check if Python is installed
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Python is not installed or not in PATH. Please install Python and try again.
    exit /b 1
)

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing required libraries...
pip install -r requirements.txt

echo.
echo Setup complete! Virtual environment has been created and dependencies installed.
echo.
echo To activate the virtual environment:
echo   venv\Scripts\activate
echo.
echo To run the application:
echo   python run.py
echo.
echo Don't forget to create a .env file with your AWS credentials for email notifications.