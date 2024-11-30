@echo off
for /f "delims=" %%i in ('powershell -NoProfile -Command ^
  "$folder = (New-Object -ComObject Shell.Application).BrowseForFolder(0, 'select ncm dir', 0).Self.Path; if ($folder) { Write-Output $folder }"') do set INPUT_DIR=%%i

if "%INPUT_DIR%"=="" (
    echo ncm dir is null, exit...
    pause
    exit /b
)

echo selected ncm dir: %INPUT_DIR%


set OUTPUT_DIR=output

ncmdump -d "%INPUT_DIR%" -o "%OUTPUT_DIR%"


pause
