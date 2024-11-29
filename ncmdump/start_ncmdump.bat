@echo off
chcp 65001 >nul
for /f "delims=" %%i in ('powershell -NoProfile -Command ^
  "$folder = (New-Object -ComObject Shell.Application).BrowseForFolder(0, '选择ncm音乐文件夹', 0).Self.Path; if ($folder) { Write-Output $folder }"') do set INPUT_DIR=%%i

if "%INPUT_DIR%"=="" (
    echo 未选文件夹，退出程序...
    pause
    exit /b
)

echo 选择的文件夹: %INPUT_DIR%


set OUTPUT_DIR=output

ncmdump -d "%INPUT_DIR%" -o "%OUTPUT_DIR%"


pause
