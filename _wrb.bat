IF DEFINED c (ECHO %c%) ELSE (set c=c:\3)
ECHO %c%
set p=%c%\python.exe
set d=%cd%
rd /s /q %d%\dist\
cd /D %c%
%p% -m pip install -U pip nuitka  wmi imageio simpleaudio  pillow
%p% -m nuitka --onefile --disable-console --windows-icon-from-ico=%d%\0up.png --include-data-files=%d%\*.png=.\ --include-data-files=%d%\*.wav=.\ --enable-plugin=tk-inter %d%\WRBalance.py
xcopy /f/y %c%\WRBalance.exe %d%\dist\
cd /D %d%
robocopy . dist\ /xf .gitignore *.py *.md *.bat /xd .git .vscode __pycache__ examples
