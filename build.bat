SET VERSION="1.1.0"
python -m nuitka main.pyw --show-progress --onefile --windows-disable-console --windows-icon-from-ico=assets/icon.png --plugin-enable=tk-inter -o FractionsQuizApp_%VERSION%_64bit.exe
