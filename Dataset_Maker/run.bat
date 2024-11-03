SET DIRECTORY_NAME="D:\OneDrive\Documents\Christopher\Projects\CanYouFish\CanYouFish"
TAKEOWN /f %DIRECTORY_NAME% /r /d y
ICACLS %DIRECTORY_NAME% /grant administrators:F /t
ICACLS %DIRECTORY_NAME% /reset /T
PAUSE