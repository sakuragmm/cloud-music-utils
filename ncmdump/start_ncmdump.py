import subprocess
from tkinter import Tk, filedialog


def select_directory():
    """弹出目录选择对话框"""
    root = Tk()
    root.withdraw()  # 隐藏主窗口
    folder_path = filedialog.askdirectory(title="选择ncm文件目录")
    root.destroy()  # 销毁主窗口
    return folder_path


def run_ncmdump():
    """选择目录并执行 ncmdump 命令"""
    input_dir = select_directory()
    if not input_dir:
        print("未选择目录，退出脚本...")
        return

    print(f"已选择目录: {input_dir}")
    output_dir = "output"  # 输出目录，可根据需要修改

    # 构造并执行命令
    cmd = ["ncmdump", "-d", input_dir, "-o", output_dir]
    try:
        subprocess.run(cmd, check=True)
        print(f"命令执行成功: {' '.join(cmd)}")
    except FileNotFoundError:
        print("错误：未找到 ncmdump 命令，请检查环境变量或路径！")
    except subprocess.CalledProcessError as e:
        print(f"命令执行失败，返回码: {e.returncode}")


if __name__ == "__main__":
    run_ncmdump()
