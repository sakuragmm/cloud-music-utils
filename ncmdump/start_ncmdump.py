import subprocess
import sys
from pathlib import Path
from tkinter import Tk, filedialog


# 打包命令
# pyinstaller --onefile -i .\favicon.ico --add-data ".\ncmdump.exe;." .\start_ncmdump.py


def extract_ncmdump():
    # 确定 PyInstaller 打包后的目录或者当前目录
    source_path = Path(sys._MEIPASS) / "ncmdump.exe" if hasattr(sys, "_MEIPASS") else Path("ncmdump.exe")
    return source_path


def select_directory(title):
    """弹出目录选择对话框"""
    root = Tk()
    root.withdraw()  # 隐藏主窗口
    folder_path = filedialog.askdirectory(title=title)
    root.destroy()  # 销毁主窗口
    return folder_path


def run_ncmdump():
    """选择目录并执行 ncmdump 命令"""
    input_dir = select_directory("选择ncm文件目录")
    if not input_dir:
        print("未选择ncm目录，退出脚本...")
        return

    print(f"已选择ncm目录: {input_dir}")

    output_dir = select_directory("选择输出目录")
    if not output_dir:
        print("未选择输出目录，退出脚本...")
        return
    print(f"已选择输出目录: {input_dir}")

    # 提取 ncmdump.exe
    ncmdump_path = extract_ncmdump()

    # 构造并执行命令
    cmd = [str(ncmdump_path), "-d", input_dir, "-o", output_dir]
    try:
        subprocess.run(cmd, check=True)
        print(f"命令执行成功: {' '.join(cmd)}")
    except FileNotFoundError:
        print("错误：未找到 ncmdump 命令，请检查环境变量或路径！")
    except subprocess.CalledProcessError as e:
        print(f"命令执行失败，返回码: {e.returncode}")


if __name__ == "__main__":
    run_ncmdump()
    input("\n按任意键退出...")