PyInstaller -y --add-data "main.kv;."  --hiddenimport pkg_resources.py2_warn --hiddenimport win32timezone gui.py
echo Looking for libpng16-16.dll in current venv
copy %VIRTUAL_ENV%\share\sdl2\bin\libpng16-16.dll .\dist\gui\libpng16-16.dll
.\dist\gui\gui.exe