import subprocess
import sys

DEPENDENCIES = [
    "pyfiglet",
    "psutil",
    "requests",
    "speedtest-cli",
    "qrcode",
    "pillow",           
    "windows-curses"   
]

def install(package):
    try:
        print(f"[+] Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"[OK] {package} installed.\n")
    except subprocess.CalledProcessError:
        print(f"[ERR] Failed to install {package}.\n")

def main():
    print("Installing required dependencies for HessOS packages...\n")
    for dep in DEPENDENCIES:
        install(dep)

    print("All dependencies installation attempted.")
    print("If you're on Linux, you can ignore 'windows-curses' install errors.")

if __name__ == "__main__":
    main()
