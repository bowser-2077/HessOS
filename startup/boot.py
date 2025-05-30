import os
import time
import subprocess
import shutil

LOGO = r"""
  _    _ ______  _____ _____  ____   _____ 
 | |  | |  ____|/ ____/ ____|/ __ \ / ____|
 | |__| | |__  | (___| (___ | |  | | (___  
 |  __  |  __|  \___ \\___ \| |  | |\___ \ 
 | |  | | |____ ____) |___) | |__| |____) |
 |_|  |_|______|_____/_____/ \____/|_____/ 
"""

CONFIG_DIR = "config"
FIRST_BOOT_FILE = os.path.join(CONFIG_DIR, "first_boot_done")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_size():
    return shutil.get_terminal_size()

def print_centered_logo():
    cols, _ = get_terminal_size()
    for line in LOGO.strip("\n").split("\n"):
        padding = (cols - len(line)) // 2
        print(" " * max(padding, 0) + line)

def loading_bar(duration=6, message=None):
    cols, lines = get_terminal_size()
    bar_width = min(40, cols - 20)
    loading_line = lines // 2

    for i in range(bar_width + 1):
        percent = i / bar_width
        bar = "#" * i + "_" * (bar_width - i)
        loading_text = f"Loading: [{bar}] {int(percent * 100)}%"
        info_text = "HessOS - 4.0 | Kernel - 7.4"
        loading_offset = (cols - len(loading_text)) // 2
        info_offset = (cols - len(info_text)) // 2

        clear_screen()
        print_centered_logo()
        print("\n" * (loading_line - 7))
        print(" " * loading_offset + loading_text)
        print(" " * info_offset + info_text)

        if message:
            msg_offset = (cols - len(message)) // 2
            print("\n" + " " * msg_offset + message)

        time.sleep(duration / bar_width)
    print()

def install_dependencies():
    packages = ["requests", "paramiko", "GitPython", "psutil", "pyfiglet", "windows-curses", "qrcode", "speedtestcli"]
    print("\nChecking System Integrity...\n")
    for pkg in packages:
        subprocess.run([os.sys.executable, "-m", "pip", "install", pkg],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("\nDone\n")

def boot():
    clear_screen()
    print_centered_logo()

    if not os.path.exists(CONFIG_DIR):
        os.mkdir(CONFIG_DIR)

    if not os.path.exists(FIRST_BOOT_FILE):
        loading_bar(duration=7, message="1st boot may take a while.")
        install_dependencies()
        with open(FIRST_BOOT_FILE, "w") as f:
            f.write("done")
    else:
        loading_bar()

clear_screen()
