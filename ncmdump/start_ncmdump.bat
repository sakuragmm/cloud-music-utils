@echo off
for /f "delims=" %%i in ('powershell -NoProfile -Command ^
  "$folder = (New-Object -ComObject Shell.Application).BrowseForFolder(0, 'select ncm dir', 0).Self.Path; if ($folder) { Write-Output $folder }"') do set INPUT_DIR=%%i
echo selected ncm dir: %INPUT_DIR%

for /f "delims=" %%i in ('powershell -NoProfile -Command ^
  "$folder = (New-Object -ComObject Shell.Application).BrowseForFolder(0, 'select output dir', 0).Self.Path; if ($folder) { Write-Output $folder }"') do set OUTPUT_DIR=%%i

if "%INPUT_DIR%"=="" (
    echo ncm dir is null, exit...
    pause
    exit /b
)
echo selected out put dir: %OUTPUT_DIR%

ncmdump.exe -d "%INPUT_DIR%" -o "%OUTPUT_DIR%"


pause
