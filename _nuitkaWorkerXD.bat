set c=E:\ProgramFiles\Python-3.8.10
set p=%c%\python.exe
set d=%cd%
cd %c%
%p% -m pip install -U pip nuitka  wmi openpyxl

%p% -m nuitka --onefile --disable-console --enable-plugin=tk-inter %d%\workerXD.py
rd /s /q %d%\dist\

xcopy /f/y %c%\workerXD.exe %d%\dist\
xcopy /f/y %d%\*.json %d%\dist\
xcopy /f/y %d%\*.xlsx %d%\dist\
